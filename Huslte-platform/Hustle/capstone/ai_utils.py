import os
import json
import re
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# ✅ Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ✅ Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

def generate_quiz_questions(title, content, num_questions=5, quiz_type="chapter"):
    """
    Generates AI-powered quiz questions using Gemini API.
    - quiz_type: "chapter" for chapter quizzes, "final" for final course quiz.
    """
    quiz_description = (
        "Each question should be based on a different concept from the chapter."
        if quiz_type == "chapter"
        else "The quiz should cover all chapters broadly, testing key concepts."
    )

    prompt = f"""
    You are an expert quiz creator. Generate {num_questions} multiple-choice quiz questions 
    based on the following {quiz_type} content.

    **Title:** {title}
    **Content:** {content}

    {quiz_description}

    Return the quiz in **valid JSON format**, without markdown syntax:
    [
        {{
            "question": "What is the first principle of financial literacy?",
            "options": ["Budgeting", "Spending", "Saving", "Debt"],
            "correct_answer": "Budgeting"
        }},
        ...
    ]
    """

    try:
        response = model.invoke(prompt)
        raw_quiz_data = response.content.strip()

        # ✅ Debug: Print raw response to check format
        print("🔍 RAW GEMINI RESPONSE:", raw_quiz_data)

        # ✅ Remove markdown formatting (backticks) if present
        clean_json = re.sub(r"```json|```", "", raw_quiz_data).strip()

        # ✅ Ensure response is valid JSON
        return json.loads(clean_json)

    except json.JSONDecodeError as e:
        print("❌ JSONDecodeError: Failed to parse JSON. Raw response:", raw_quiz_data)
        print("🔍 Error details:", e)
        return None
    except Exception as e:
        print(f"❌ Error generating quiz: {e}")
        return None
