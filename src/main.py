import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🚀 Progetto A1 EvalPlus - Inizializzazione Completata!")
    
    if "GROQ_API_KEY" in os.environ:
        print("✅ GROQ API Key trovata!")
    else:
        print("❌ GROQ API Key mancante nel fle .env!")
        
    if "GEMINI_API_KEY" in os.environ:
        print("✅ GEMINI API Key trovata!")
    else:
        print("❌ GEMINI API Key mancante nel fle .env!")

if __name__ == "__main__":
    main()
