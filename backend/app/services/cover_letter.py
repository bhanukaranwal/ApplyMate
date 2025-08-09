# backend/app/services/cover_letter.py

import os
from openai import OpenAI
from typing import Dict

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_cover_letter(job: Dict, applicant_name: str, skills: str) -> str:
    """
    Generate a tailored cover letter for a specific job posting.
    
    Args:
        job (Dict): Job details dictionary containing title, company, description, etc.
        applicant_name (str): Name of the applicant
        skills (str): Comma-separated list of skills

    Returns:
        str: Generated cover letter
    """

    prompt = f"""
    Write a professional and tailored cover letter for the following job:

    Job Title: {job.get("title")}
    Company: {job.get("company")}
    Location: {job.get("location")}
    Job Description: {job.get("description")}

    Applicant Name: {applicant_name}
    Skills: {skills}

    The letter should:
    - Be formal and concise
    - Highlight relevant skills
    - Mention enthusiasm for the company
    - End with a call to action
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a career coach and professional cover letter writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        raise RuntimeError(f"Error generating cover letter: {e}")
