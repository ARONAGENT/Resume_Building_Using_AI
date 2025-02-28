import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import google.generativeai as genai 
from django.conf import settings


def home(request):
    return render(request,"index.html")

def resumeform(request):
    return render(request,"resumeform.html")


genai.configure(api_key="my api key ....") 

def resumereq(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        skills = request.POST.get("skills")
        experience = request.POST.get("experience")
        education = request.POST.get("education")
        resume_type = request.POST.get("resume_type")
        company = request.POST.get("company")
        resume_language = request.POST.get("resume_language")

        # Handling Image Upload
        profile_image = request.FILES.get("profile_image")
        profile_image_url=""
        if profile_image:
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'uploads'))
            filename = fs.save(profile_image.name, profile_image)
            profile_image_url = fs.url(f"uploads/{filename}")

        prompt = f"""
        Generate a **detailed professional resume in HTML format** with proper structure, bold section headings, lists, and clear organization. Ensure the resume follows accessibility best practices.

        Use the following structure:

        <h1>{name}</h1>

        <div class="contact-info">
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Phone:</strong> {phone}</p>
        </div>

        <div class="section">
        <h2>Summary</h2>
        <p>Passionate software engineer skilled in {skills}. Seeking an opportunity at {company} to leverage experience in {resume_type} and contribute to innovative solutions.</p>
        </div>

        <div class="section">
        <h2>Skills</h2>
        <ul>
        <li><strong>Programming Languages:</strong> {skills}</li>
        <li><strong>Experience:</strong> {experience}</li>
        </ul>
        </div>

        <div class="section">
        <h2>Experience</h2>
        <p><strong>Role:</strong> (Specify Role Here)</p>
        <p><strong>Company:</strong> {company}</p>
        <p><strong>Duration:</strong> (Start Date - End Date)</p>
        <ul>
        <li>Describe your responsibilities using action verbs.</li>
        <li>Quantify achievements (e.g., "Improved performance by 15%").</li>
        </ul>
        </div>

        <div class="section">
        <h2>Education</h2>
        <p><strong>Degree:</strong> {education}</p>
        <p><strong>Institution:</strong> (Add School/University Name)</p>
        </div>

        you still give this info ..... for giving the response 
        plz don't give this info below 
        plz i request dont give the information below it show the above resume dirty ok......

        `, `
        `, ``. * **Accessibility:** `mailto:` and `tel:` links, language attribute. * **Clearer Structure:**
         Separate sections for 10th and 12th. * **Detailed Content:** More robust skills and experience descriptions.
          * **Professional Style:** Consistent formatting and improved wording. * **Valid HTML:** Ensures the HTML structure is valid. 
          Remember to replace the placeholder information with your actual details. This improved version provides a more accessible,
         professional, 
        and well-structured resume. You can further customize it by adding CSS for styling.
        """

        # Generate resume summary using Gemini AI
        model = genai.GenerativeModel("gemini-1.5-pro")  # Use the correct model name
        response = model.generate_content(prompt)
        resume_summary = response.text if response else "Resume summary generation failed."
    
    return render(request, "success.html", {"resume_summary": resume_summary,"profile_image_url": profile_image_url})