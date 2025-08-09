import os
import openai
from typing import Dict
from ..config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def generate_cover_letter(job: Dict, resume_text: str, tone: str = "professional") -> str:
    prompt = (
        f"Write a {tone} cover letter for the job: {job['title']} at {job['company']}.\n"
        f"Job description:\n{job['description']}\n\n"
        f"Use the following resume/skills as context:\n{resume_text}\n\n"
        "Keep it concise (~250-350 words) and emphasize fit and relevant achievements."
    )
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600,
    )
    return resp.choices[0].message['content']
