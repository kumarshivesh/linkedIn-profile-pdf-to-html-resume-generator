# Resume Generator Full-stack Django Application

This project is a Django-based web application that generates HTML resumes from a LinkedIn profile PDF [for testing the web app please download the sample data file (i.e., `kumar_linkedin_profile.pdf`)]. It leverages the GROQ API to process the PDF contents and return a well-formatted HTML resume with distinct sections like personal information, work experience, education, and skills.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Project Locally](#running-the-project-locally)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **File Upload**: Users can upload LinkedIn profile `PDF`.
- **PDF Processing**: The application uses PyPDF2 to extract text from the PDF.
- **Results Display**: Use GROQ API to generate an HTML-formatted resume and display the result on web page.


## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS (Basic styling)
- **API Integration**: Groq API to generate an HTML-formatted resume
- **File Handling**: `PyPDF2` to extract text from the PDF
- **Environment Management**: `dotenv` for managing API keys securely

## Project Structure

```
├── resume_generator/        # Django project directory
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project-level URL routing
│   └── ...
├── resume_app/              # Django app directory
│   ├── templates/           # HTML templates for the app
│   │   ├── upload.html      # Form for PDF upload
│   │   ├── resume.html      # Generated HTML resume display
│   ├── forms.py             # Form to handle PDF uploads
│   ├── views.py             # Main logic for handling PDF upload and GROQ API calls
│   ├── urls.py              # App-level URL routing
│   └── ...
├── .gitignore               # Ensures .env is not pushed to GitHub
├── manage.py                # Django's main management file
├── requirements.txt         # Python dependencies for the project
└── README.md                # This readme file
```

## Installation

### Prerequisites

- Python 3.10+
- Git

### Clone the Repository

```bash
git clone https://github.com/kumarshivesh/linkedIn-profile-pdf-to-html-resume-generator.git
cd resume_generator
```

### Create and Activate a Virtual Environment

```
python -m venv .venv
source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
```

### Install Dependencies

```
pip install -r requirements.txt
```

## Environment Variables

Create a .env file in the root directory of the project and add the following variable(s):

```
GROQ_API_KEY=your_groq_api_key_here
```

## Running the Project Locally

#### 1. Apply database migrations:

```
python manage.py migrate
```

#### 2. Start the development server:
```
python manage.py runserver
```

#### 3. Open your web browser and go to 

http://127.0.0.1:8000/

## Usage

### 1. Upload a PDF File:

Go to http://127.0.0.1:8000/ in your browser.
Click on the "Choose File" button and select a .pdf file that contains LinkedIn Profile of a LinkedIn user.


### 2. Text Extraction:

- Click the "Generate Resume" button to send the file for text extraction.
- The results will be displayed on a new page in a well-formatted HTML resume with distinct sections like personal information, work experience, education, and skills.

## Contributing

Contributions are welcome! To contribute:

1. Fork the project
2. Create a feature branch (git checkout -b feature/my-feature)
3. Commit your changes (git commit -m 'Add new feature')
4. Push to the branch (git push origin feature/my-feature)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. 



