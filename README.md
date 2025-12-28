# AI-Automation-Portfolio-Website-Generator
AI Resume-to-Portfolio Website Generator
Overview

This project converts a user's PDF resume into a fully functional and professionally structured portfolio website. The system extracts the resume content, processes it through a Large Language Model, and generates complete HTML, CSS, and JavaScript files that represent the user’s skills, experience, projects, certifications, and background in a modern portfolio format.

Features

Accepts resume in PDF format

Extracts and processes resume content

Automatically generates a professional portfolio website

Produces HTML, CSS, and JavaScript files

Packages the generated website into a downloadable ZIP file

Simple and user-friendly interface built with Streamlit

Zero manual editing required from the user

Technology Stack

Python

Streamlit

LangChain

Google Gemini 2.5 Flash

PyPDF2 for PDF parsing

python-dotenv for environment variable management

How It Works

The user uploads a PDF resume.

The system extracts text using PDF parsing.

The extracted content is provided to a prompt engineered for high-quality portfolio generation.

The AI model generates complete HTML, CSS, and JavaScript files.

All files are automatically compressed into a ZIP file.

The user downloads and deploys the generated portfolio website.

Project Purpose

The primary goal of this project is to provide a fast and automated method for creating personal portfolio websites, especially for students, professionals, and job applicants. It eliminates the need for manual website designing and ensures the generated portfolio reflects the user’s actual resume content.

Usage

Upload your resume in PDF format.

Select the generate option.

Wait for the system to create the website files.

Download the ZIP file containing the portfolio.

Host the generated website using GitHub Pages, Netlify, or any static site hosting service.

Customization

The system prompt used for generating the portfolio can be modified to adjust:

Layout and design style

Section order

Theme and color preferences

Project and skills presentation

Users may fine-tune these settings based on personal or branding needs.

Limitations

Only PDF resumes are supported

Generated design depends on AI output and prompt quality

Requires a valid Gemini API key

Author

Created by Kishore Seethi
LinkedIn: https://www.linkedin.com/in/reddy-kishore-seethi

GitHub: https://github.com/reddykishore17

License

This project is open for personal, academic, and experimental use. You may modify or extend the project as required.
