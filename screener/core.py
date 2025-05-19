#!/usr/bin/python3 
# screener/core.py

import os
import google.generativeai as genai

def build_prompt(cv_text):
    return f"""
You are a bioinformatics hiring assistant evaluating resumes.

Score from 0 to 2:
1. Python programming
2. Workflow tools (Nextflow/Snakemake)
3. Git/version control
4. NGS familiarity (FASTQ, BAM, VCF, DNA-seq, RNA-seq)
5. Bioinformatics tools (samtools, GATK, VEP)
6. Reproducibility / clinical mindset
7. Communication/documentation clarity

Provide score and explanation for each.

Resume content:
{cv_text}
"""

def score_resume_with_gemini(cv_text, api_key):
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-2.0-flash")

    prompt = build_prompt(cv_text)
    response = model.generate_content(prompt)

    return response.text
