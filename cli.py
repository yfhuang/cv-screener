#!/usr/bin/python3
# cli.py

import argparse
import os
from screener.core import score_resume_with_gemini
from screener.utils import extract_text_from_pdf

def main():
    parser = argparse.ArgumentParser(description="Bioinformatics Resume Screener (Gemini)")
    parser.add_argument("cv_path", help="Path to resume file (PDF or TXT)")
    parser.add_argument("--api-key", help="Gemini API Key (or use GEMINI_API_KEY env variable)")

    args = parser.parse_args()
    api_key = args.api_key or os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ Error: API key not provided.")
        return

    ext = os.path.splitext(args.cv_path)[-1].lower()
    if ext == ".pdf":
        cv_text = extract_text_from_pdf(args.cv_path)
    elif ext == ".txt":
        with open(args.cv_path, "r", encoding="utf-8") as f:
            cv_text = f.read()
    else:
        print("❌ Error: Only .pdf or .txt files are supported.")
        return

    result = score_resume_with_gemini(cv_text, api_key)
    print("\n===== Resume Evaluation =====\n")
    print(result)

if __name__ == "__main__":
    main()

