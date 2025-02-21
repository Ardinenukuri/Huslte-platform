from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from django.conf import settings
from capstone.models import Certificate

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
