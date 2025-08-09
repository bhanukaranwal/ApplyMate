import os
import openai
from typing import Dict

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_cover_letter(job: Dict, applicant_name: str, skills: str) -> str:
    """
    Generates a tailored cover letter using OpenAI GPT models.
    
    Args:
        job (Dict): Job dictionary containing title, company, location, summary.
        applicant_name (str): Applicant's full name.
        skills (str): Comma-separated skills.

    Returns:
        str: Generated cover letter text.
    """
    if not openai.api_key:
        raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")

    prompt = f"""
You are a professional career assistant.
Write a personalized, formal cover letter for the following job.
Highlight how the applicant's skills align with the job description.

Job Title: {job.get('title', 'N/A')}
Company: {job.get('company', 'N/A')}
Location: {job.get('location', 'N/A')}
Job Summary: {job.get('summary', 'N/A')}

Applicant Name: {applicant_name}
Applicant Skills: {skills}

Tone: Professional, confident, and concise.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Fast, cost-effective GPT model
        messages=[
            {"role": "system", "content": "You are a professional career coach and expert cover letter writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=600
    )

    return response["choices"][0]["message"]["content"].strip()
