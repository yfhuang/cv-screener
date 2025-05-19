#!/usr/bin/python3

import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash")
response = model.generate_content("Summarize what a bioinformatics engineer does.")
print(response.text)
