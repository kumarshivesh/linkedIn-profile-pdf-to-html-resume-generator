from django import forms

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(label='Upload LinkedIn Profile PDF')
