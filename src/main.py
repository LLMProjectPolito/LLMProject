import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Project A1 EvalPlus - Initialization Complete")
    
    if "GROQ_API_KEY" in os.environ:
        print("[OK] GROQ API Key found")
    else:
        print("[ERROR] GROQ API Key missing in .env file")
        
    if "GEMINI_API_KEY" in os.environ:
        print("[OK] GEMINI API Key found")
    else:
        print("[ERROR] GEMINI API Key missing in .env file")

if __name__ == "__main__":
    main()
