from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from django.conf import settings
from capstone.models import Certificate
import PyPDF2
import docx
import os
import re
import json
import requests
from django.conf import settings
from dotenv import load_dotenv
from capstone.models import Certificate
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import PyPDF2
import docx

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def extract_json_from_text(text):
    """
    Extracts all quiz questions from the AI response, including JSON blocks and text-based questions.
    """
    all_questions = []

    try:
        # ✅ Extract JSON block if available
        json_matches = re.findall(r'\[\s*{.*?}\s*\]', text, re.DOTALL)
        for json_text in json_matches:
            try:
                parsed_json = json.loads(json_text)
                if isinstance(parsed_json, list):
                    all_questions.extend(parsed_json)
            except json.JSONDecodeError:
                print(f"⚠️ Skipping invalid JSON block: {json_text[:100]}...")

        # ✅ Extract text-based multiple-choice questions
        text_questions = re.findall(
            r'(\d+)\.\s*(.*?)\n\s*A\.\s*(.*?)\n\s*B\.\s*(.*?)\n\s*C\.\s*(.*?)\n\s*D\.\s*(.*?)\n',
            text, re.DOTALL
        )
        for match in text_questions:
            question_text = match[1].strip()
            options = [match[2].strip(), match[3].strip(), match[4].strip(), match[5].strip()]
            correct_answer = options[0]  # ✅ Assume the first option is correct
            all_questions.append({
                "question": question_text,
                "options": options,
                "correct_answer": correct_answer
            })

        # ✅ Ensure all valid questions are extracted
        if all_questions:
            return all_questions

        print("⚠️ No valid questions extracted from AI response.")
        return []

    except Exception as e:
        print(f"❌ Error extracting questions: {e}")
        return []


def generate_quiz_questions(title, content, num_questions=5):
    """
    Generates multiple-choice quiz questions using Hugging Face API.
    """
    truncated_content = " ".join(content.split()[:500])  # Reduce token usage

    prompt = f"""
    Generate {num_questions} **unique** multiple-choice quiz questions based on the content below.

    **Title:** {title}
    **Content:** {truncated_content}

    🚨 **INSTRUCTIONS (READ CAREFULLY)** 🚨  
    - DO NOT repeat the example.  
    - DO NOT copy the example.  
    - ONLY return **real** multiple-choice questions related to the content above.  
    - Your output **MUST be valid JSON** (no explanations, no extra text).  
    - Each question must be **new, original, and relevant to the content**.

    Example format (DO NOT COPY THIS, CREATE NEW QUESTIONS):
    ```json
    [
        {{"question": "What is self-confidence?",
          "options": ["A skill", "A belief", "A mindset", "A habit"],
          "correct_answer": "A belief"}},

        {{"question": "Why is setting boundaries important?",
          "options": ["To increase stress", "To prevent burnout", "To work overtime", "To reduce salary"],
          "correct_answer": "To prevent burnout"}}
    ]
    ```
    Now generate **REAL, NEW multiple-choice questions** based on the content above.
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

        # ✅ Extract JSON from AI response
        quiz_questions = extract_json_from_text(response.json()[0].get("generated_text", "").strip())

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