# 🤖 AI Recruiter Agent - AI Marathon 2026

## Track 2: The Intelligent Recruiter

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Chutes.ai](https://img.shields.io/badge/Chutes.ai-LLM-green.svg)](https://chutes.ai)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 What It Does

This AI Agent automatically screens and ranks candidates based on job descriptions. Built for **AI Marathon 2026** under the theme **"LLM Everywhere"**.

| Feature | Description |
|---------|-------------|
| 📝 **Job Analysis** | Extracts required skills, experience, and qualifications |
| 🏆 **Candidate Ranking** | Scores each candidate 0-100 with reasoning |
| 💬 **Personalized Pitches** | Generates "why hire" messages for each candidate |
| 🧠 **Agentic Reasoning** | Explains WHY each candidate got their score |

---

## 🔧 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.11+** | Programming language |
| **Chutes.ai** | LLM API provider (sponsor) |
| **Qwen3-32B-TEE** | AI model (the "brain") |
| **OpenAI Library** | API communication |
| **python-dotenv** | Environment variable management |

---

## 🚀 How to Run

### Prerequisites

- Python 3.11 or higher
- Chutes.ai API key (free with event code)

### Step 1: Clone the Repository

```bash
git clone https://github.com/tanyongming33-tech/ai-recruiter-agent-apu-ai-marathon.git
cd ai-recruiter-agent-apu-ai-marathon

Step 2: Install Dependencies
bash
pip install openai python-dotenv

Step 3: Set Up Environment Variables
Copy the example environment file:

bash
cp .env.example .env
Edit .env and add your Chutes.ai API key:

text
CHUTES_API_KEY=your_actual_api_key_here
⚠️ Never commit your .env file to GitHub! It's already ignored via .gitignore.



Step 4: Run the Agent
bash
python recruiter_clean.py
Type sample to test with a sample job description, or paste your own.



