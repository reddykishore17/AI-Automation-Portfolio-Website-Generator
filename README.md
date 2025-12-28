# AI-Automation-Portfolio-Website-Generator
This project demonstrates how AI automatically converts a user’s PDF resume into a complete, responsive, and professionally structured portfolio website. The goal is to provide a simple and fully automated way to turn resume data into a ready-to-host website without writing any code.

## Project Objectives
The primary objective of this project is to automate portfolio website creation using AI and resume text. The key goals of this project include:
* Automated Website Generation: Transform resume content into a fully structured personal website.
* Modern UI Design: Produce clean and professional HTML, CSS, and JavaScript.
* User-Friendly Workflow: Allow users to upload a PDF and download a complete website instantly.
* AI-Powered Processing: Use Gemini to format skills, projects, experience, and certifications into website sections.
* Zero Manual Coding: Fully automate the process with a single action.

## How It Works
The application processes a resume and generates a portfolio using the following steps:
* Resume Upload: The user uploads a PDF resume.
* Content Extraction: PyPDF2 extracts text from the resume.
* LLM Processing: The extracted text is passed to Gemini through LangChain.
* Website Creation: Gemini returns complete HTML, CSS, and JavaScript code.
* Downloadable Output: All files are saved, compressed, and provided as a ZIP download.

## Technology Stack
The project is built using:
* Python
* Streamlit
* LangChain
* Google Gemini 2.5 Flash
* PyPDF2
* python-dotenv

## Features
* Upload resume in PDF format
* Automatic extraction of resume content
* AI-generated HTML, CSS, and JavaScript
* Professional and responsive design
* Complete ZIP download of website files
* Easy-to-use interface

## Limitations
* Only PDF resumes are supported
* Requires Gemini API key
* Output quality depends on resume structure
* Internet connection is required

## Usage
1. Upload your resume (PDF).
2. Click the Generate button.
3. Wait for the system to create the website files.
4. Download the ZIP package.
5. Host the website using GitHub Pages, Netlify, or any static hosting provider.

## Author
Created by Kishore Seethi  
LinkedIn: https://www.linkedin.com/in/reddy-kishore-seethi  
GitHub: https://github.com/reddykishore17
