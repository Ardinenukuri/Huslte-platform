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
from googletrans import Translator

translator = Translator()

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
    
def translate_text(text, target_lang):
    """Translates text into the target language."""
    if text and target_lang:
        try:
            translation = translator.translate(text, dest=target_lang)
            return translation.text
        except Exception as e:
            print(f"❌ Translation error: {e}")
    return text 