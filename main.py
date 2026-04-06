import os
import json
import re
import google.generativeai as genai
from PyPDF2 import PdfReader
from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")



genai.configure(api_key=api_key)

def analyze_resume_logic(pdf_file, job_desc):
    try:
        
        reader = PdfReader(pdf_file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text()

        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt = f"""
        Analyze this Resume against the JD. Return ONLY a JSON object.
        JD: {job_desc}
        Resume: {resume_text}
        Format: {{ "match_score": 85, "matching_skills": [], "missing_skills": [], "interview_questions": [] }}
        """

        
        response = model.generate_content(prompt)
        
        
        raw_text = response.text.strip()
        json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        
        if json_match:
            return json.loads(json_match.group())
        else:
            return json.loads(raw_text)
            
    except Exception as e:
        return {"error": f"AI Error: {str(e)}"}