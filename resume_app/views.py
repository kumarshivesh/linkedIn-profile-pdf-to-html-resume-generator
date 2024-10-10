import os
import requests
from django.shortcuts import render
from django.core.exceptions import ValidationError
from .forms import PDFUploadForm
from PyPDF2 import PdfReader
from django.conf import settings  # Import settings to access the GROQ API key

def extract_text_from_pdf(pdf_file):
    """
    Extract text from the uploaded LinkedIn profile PDF.
    """
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def generate_resume_html(text):
    """
    Generate an HTML resume based on the extracted LinkedIn profile text using GROQ API.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.GROQ_API_KEY}",  # Use API key from settings
        "Content-Type": "application/json"
    }
    prompt = f"""
    Generate an HTML resume based on the following LinkedIn profile information:

    {text}

    Please format it as a clean, professional HTML document with appropriate styling.
    Do not include any markdown, code blocks, or formatting like ```html or ``` in the response.
    Just return the plain HTML content.

    Format the resume with the following requirements:
    - Position the content in the center of the page with margins on all sides.
    - Use distinct blocks for different sections such as personal information, work experience, education, skills, etc., and ensure each section is clearly highlighted.
    - Each block should have a subtle background color or border to make the sections visually distinct.
    - Ensure that the headings for each section (like Work Experience, Education, etc.) are larger and bold, to make the separation clear.
    - Make the layout clean, professional, and visually balanced, without excessive left or right alignment.
    - Add a small margin between sections to create space and make the resume easy to read.
    """

    data = {
        "model": "llama-3.1-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 2000
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        raise ValidationError(f"An error occurred while generating the resume: {str(e)}")

def upload_pdf(request):
    """
    Handle the upload of the LinkedIn profile PDF and render the generated resume.
    """
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']

            try:
                # Extract text from PDF
                pdf_text = extract_text_from_pdf(pdf_file)

                # Generate HTML resume using GROQ API
                resume_html = generate_resume_html(pdf_text)

                # Render the generated resume
                return render(request, 'resume_app/resume.html', {'resume_html': resume_html})
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = PDFUploadForm()

    return render(request, 'resume_app/upload.html', {'form': form})
