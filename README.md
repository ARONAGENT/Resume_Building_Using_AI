# Resume Building Using AI

This is a Django-based AI-powered Resume Building project that generates professional resumes based on user inputs, including an uploaded image. The model uses an AI API key to process the inputs and generate resumes dynamically.

## Features
- Upload an image
- AI processes the image and extracts relevant data
- Generates a resume automatically based on extracted data
- Displays the generated resume as an image
- Provides a video execution demonstration

## Video Execution

https://github.com/user-attachments/assets/94f0bc81-c3bd-43d4-a3f1-6f9d6d8e2d6e


## Resume Output Sample in PDF Format

[Generated Resume.pdf](https://github.com/user-attachments/files/19032329/Generated.Resume.pdf)

---

## Installation Guide
Follow these steps to set up and run the project locally:

### Step 1: Clone the Repository
```bash
git clone https://github.com/ARONAGENT/resume-ai-django.git
cd resume-ai-django
```

### Step 2: Create a Virtual Environment
```bash
virtualenv resume_env
resume_env\Scripts\
use activate to activate the virtual environment
```

### Step 3: Install Dependencies
```bash
pip install google-generativeai
```

### Step 4: Create a Django Project
```bash
django-admin startproject resumeAI
cd resumeAI
```

### Step 5: Set Up API Key (For AI Processing)
- Obtain an API key from Google Gemini AI or another AI provider.
- Store the API key securely in the `.env` file.

### Step 6: Run the Django Server
```bash
python manage.py runserver
```

### Step 7: Access the Application
Open your browser and visit:  
**http://127.0.0.1:8000/**

---

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/resume/generate` | Uploads image and generates a resume |
| GET    | `/resume/view` | Retrieves the generated resume |

---

## How It Works
1. The user uploads an image.
2. The AI model processes the image and extracts relevant details.
3. A resume is generated based on the extracted details.
4. The generated resume is returned as an image.

---

## Contributing
If you'd like to contribute, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.

## Author
**Your Name** - [GitHub](https://github.com/ARONAGENT)

---


