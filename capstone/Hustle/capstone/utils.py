from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from django.conf import settings
from capstone.models import Certificate
import PyPDF2
import docx
from dotenv import load_dotenv
import json
import requests
import re
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


def extract_json_from_text(text):
    """
    Extract multiple JSON structures from AI-generated text and merge them into a single valid list.
    """
    json_matches = re.findall(r'\[\s*{.*?}\s*\]', text, re.DOTALL)  # ✅ Extract all JSON lists
    
    all_questions = []
    for json_text in json_matches:
        try:
            parsed_json = json.loads(json_text)
            if isinstance(parsed_json, list):
                all_questions.extend(parsed_json)  # ✅ Append all valid questions
        except json.JSONDecodeError:
            print(f"⚠️ Skipping invalid JSON block: {json_text[:100]}...")  # Debugging

    if all_questions:
        return all_questions  # ✅ Return a combined list of all questions

    print("⚠️ No valid JSON extracted from AI response.")
    return []

def generate_quiz_questions(chapter_title, chapter_content, num_questions=5):
    """
    Generates multiple-choice quiz questions using Hugging Face API.
    """
    truncated_content = " ".join(chapter_content.split()[:500])  # Reduce token usage

    prompt = f"""
    Generate {num_questions} multiple-choice quiz questions from the following content.

    **Chapter Title:** {chapter_title}
    **Content:** {truncated_content}

    ⚠️ IMPORTANT: Strictly output the response as a **single JSON list with no extra text**.

    Correct Format:
    [
        {{"question": "What is self-confidence?",
          "options": ["A skill", "A trait", "A belief", "An emotion"],
          "correct_answer": "A belief"}}
    ]
    """

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 350,
            "temperature": 0.7,
            "top_k": 50,
            "top_p": 0.9,
        }
    }

    api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

    try:
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code != 200:
            print(f"❌ API Error {response.status_code}: {response.text}")
            return []

        # ✅ Get AI response text
        ai_generated_text = response.json()[0].get("generated_text", "").strip()
        print("🔍 AI Response:", ai_generated_text)  # Debugging

        # ✅ Extract JSON from AI response
        quiz_questions = extract_json_from_text(ai_generated_text)

        # 🚨 Final fix: Force the extracted content to be a proper JSON list
        if not isinstance(quiz_questions, list):
            quiz_questions = [quiz_questions]  # Wrap as a list if needed

        return quiz_questions

    except requests.RequestException as e:
        print(f"❌ API Request Failed: {e}")
        return []
        
def generate_certificate(resource, final_score):
    # ✅ Define file path
    pdf_filename = f"certificate_{resource.id}.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, "certificates", pdf_filename)

    # ✅ Create PDF certificate
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 100, "Certificate of Completion")

    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height - 140, f"This is to certify that you have successfully completed:")
    
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 180, resource.title)

    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 220, f"Final Score: {final_score}%")

    c.drawCentredString(width / 2, height - 260, "Issued by Hustle Platform")

    # ✅ Save PDF
    c.save()

    # ✅ Save certificate path to database
    certificate = Certificate.objects.create(
        user=resource.user,  
        resource=resource,
        certificate_file=f"certificates/{pdf_filename}"
    )
    
    return certificate


def extract_text_from_file(uploaded_file):
    """
    Extracts text from a PDF or DOCX file.
    :param uploaded_file: Uploaded file object.
    :return: Extracted text as a string.
    """
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()

    if file_extension == ".pdf":
        return extract_text_from_pdf(uploaded_file)

    elif file_extension == ".docx":
        return extract_text_from_docx(uploaded_file)

    else:
        return None  # Unsupported file type


def extract_text_from_pdf(uploaded_pdf):
    """Extracts text from a PDF file."""
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_pdf)
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text() + "\n"
        return text.strip() if text else None
    except Exception as e:
        print(f"❌ Error extracting text from PDF: {e}")
        return None


def extract_text_from_docx(uploaded_docx):
    """Extracts text from a DOCX file."""
    text = ""
    try:
        doc = docx.Document(uploaded_docx)
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text.strip() if text else None
    except Exception as e:
        print(f"❌ Error extracting text from DOCX: {e}")
        return None