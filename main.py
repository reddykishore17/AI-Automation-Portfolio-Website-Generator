import streamlit as st
import dotenv 

import langchain
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

import os
import zipfile
import PyPDF2

os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")

st.set_page_config(page_title="AI Portfolio Creation",page_icon="🌐")
st.title("AI AUTOMATION PORTFOLIO WEBSITE CREATION")

uploaded_resume = st.file_uploader("Upload your resume (PDF Only)", type=["pdf"])

resume_text = ""

# ---------------- READ PDF FUNCTION ---------------- #

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# ---------------- EXTRACT TEXT ---------------- #
if uploaded_resume is not None:
    resume_text = extract_text_from_pdf(uploaded_resume)

# ---------------- GENERATE BUTTON ---------------- #
if st.button("generate"):
    if resume_text == "":
        st.error("Please upload a valid resume file.")
    else:
        message=[("system","""You are an expert full-stack web developer who creates clean, modern, visually appealing, professional portfolio websites.  
Your job is to read the full resume content provided by the user and generate a complete personal portfolio website that looks premium, elegant, and industry-standard.

Follow these rules carefully:

1. Build a fully structured website with sections:
   - Hero Section (Name, Title, Tagline)
   - About Me (Short narrative built from resume)
   - Skills (Categorized into Tech Skills, Tools, Libraries, ML/AI, Analytics, etc.)
   - Projects (Showcase projects with bullet points, tech stack, impact)
   - Education
   - Certifications
   - Publications
   - Contact Section (Email, Phone, GitHub, LinkedIn, etc.)

2. The design must be:
   - Modern, clean, minimal, and highly professional
   - Fully responsive (mobile & desktop)
   - With smooth transitions, hover effects, subtle animations
   - Beautiful typography and layout spacing
   - Use visually appealing color combinations (blue / purple / dark theme allowed)
   - Pixel-perfect portfolio look

3. Replace any missing or unclear resume details with best professional structure.
4. All links in the resume should appear as clickable buttons/cards.
5. Optimize readability, spacing, sections, and components.
6. Highlight data analytics, machine learning, GenAI, SQL, Power BI, and Python expertise.
7. Present experience and projects in a strong, industry-ready style.
   
You must strictly output code in this exact format only:

--html--
[complete professional HTML code]
--html--

--css--
[complete responsive CSS code with animations, effects, layout styles]
--css--

--js--
[JavaScript for animations, interactions, navbar toggles, scroll effects]
--js--
""")]

        message.append(("user", resume_text))

        model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

        response=model.invoke(message)

        # ---------------- SAVE FILES ---------------- #
        with open("index.html","w") as file:
            file.write(response.content.split("--html--")[1])

        with open("style.css","w") as file:
            file.write(response.content.split("--css--")[1])

        with open("script.js","w") as file:
            file.write(response.content.split("--js--")[1])

        with zipfile.ZipFile("website.zip","w") as zip:
            zip.write("index.html")
            zip.write("style.css")
            zip.write("script.js")

        st.download_button(
            "Click to download",
            data=open("website.zip","rb"),
            file_name="website.zip"
        )

        st.write("success")