# backend/app/services/cover_letter.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_cover_letter(job, applicant_name: str, skills: str) -> str:
    """
    Generates a tailored cover letter for a given job and applicant info.
    
    Args:
        job (dict): Job details (title, company, description, etc.)
        applicant_name (str): Name of the applicant
        skills (str): Comma-separated skills of the applicant
    
    Returns:
        str: A professional cover letter
    """
    
    if not job.get("title") or not job.get("company"):
        raise ValueError("Job must have a title and company.")

    prompt = f"""
    Write a professional, tailored cover letter for the following job posting.
    Include the applicant's name and highlight their relevant skills.

    Applicant Name: {applicant_name}
    Skills: {skills}

    Job Title: {job.get("title")}
    Company: {job.get("company")}
    Job Description: {job.get("description", "No description provided.")}
    Location: {job.get("location", "Not specified")}

    The tone should be professional yet enthusiastic, and the length should be about 250-300 words.
    End with a polite call-to-action.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional career coach and cover letter writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        raise RuntimeError(f"OpenAI API error: {str(e)}")
