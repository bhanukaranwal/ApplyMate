from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

class CoverLetterRequest(BaseModel):
    job_title: str
    company: str
    job_description: str
    user_name: str
    user_skills: list[str]

@router.post("/generate_cover_letter")
async def generate_cover_letter(request: CoverLetterRequest):
    """
    Generates a tailored cover letter using the OpenAI API.
    """
    try:
        skills_formatted = ", ".join(request.user_skills)

        prompt = (
            f"Write a professional, personalized cover letter for the job '{request.job_title}' "
            f"at '{request.company}'. The applicant's name is {request.user_name} and they have "
            f"the following skills: {skills_formatted}. Job description: {request.job_description}. "
            f"Make it concise, friendly, and tailored to the company, highlighting relevant skills."
        )

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional cover letter writer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )

        cover_letter = response.choices[0].message["content"].strip()
        return {"cover_letter": cover_letter}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
