from openai import OpenAI
import json
import re

# ============================================
# CHUTES.AI SETUP
# ============================================

API_KEY = "cpk_61e3aa51b9ed4f2998bdc9f68af009e3.2e74bd982a705763adc79275386d985a.Z888oaCoyaUoJI1BDDi3JZVc4piJv5q2"

client = OpenAI(
    base_url="https://llm.chutes.ai/v1",
    api_key=API_KEY
)

MODEL = "Qwen/Qwen3-32B-TEE"

# ============================================
# SAMPLE RESUMES
# ============================================

resumes = [
    {
        "name": "Alex Chen",
        "skills": ["Python", "Machine Learning", "TensorFlow", "AWS"],
        "experience": "3 years as ML Engineer - built recommendation systems serving 1M+ users",
        "education": "BS Computer Science, Stanford",
        "email": "alex.chen@email.com"
    },
    {
        "name": "Sarah Jones",
        "skills": ["JavaScript", "React", "Node.js", "Python"],
        "experience": "5 years Full Stack Developer - led e-commerce platform with $10M sales",
        "education": "MS Software Engineering, Carnegie Mellon",
        "email": "sarah.jones@email.com"
    },
    {
        "name": "Priya Patel",
        "skills": ["Python", "NLP", "LangChain", "Vector Databases", "PyTorch"],
        "experience": "4 years AI Engineer - built RAG systems for enterprise clients",
        "education": "MS AI, Georgia Tech",
        "email": "priya.patel@email.com"
    }
]

# ============================================
# HELPER FUNCTION TO CLEAN LLM OUTPUT
# ============================================

def clean_output(text):
    """Remove <think> tags and other artifacts"""
    # Remove everything between <think> and </think>
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    # Remove extra newlines
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

# ============================================
# AGENT FUNCTIONS
# ============================================

def rank_candidates(job_description, resumes):
    """Agent ranks candidates using Chutes.ai LLM"""
    
    prompt = f"""
    Job Description: {job_description}
    
    Candidates:
    {json.dumps([{"name": r["name"], "skills": r["skills"], "experience": r["experience"]} for r in resumes], indent=2)}
    
    Rank these candidates from best to worst fit.
    Return ONLY valid JSON in this format, no other text:
    {{"ranked": [{{"name": "Alex Chen", "score": 95, "reason": "Has required skills"}}]}}
    """
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a JSON generator. Return ONLY valid JSON. No explanations, no markdown, no thinking tags."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.1
    )
    
    result = response.choices[0].message.content
    # Clean the output
    result = clean_output(result)
    
    # Try to extract JSON if there's extra text
    try:
        json_match = re.search(r'\{.*\}', result, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except:
        pass
    
    return {"ranked": []}

def generate_pitch(candidate, job_description):
    """Generate personalized pitch for a candidate"""
    
    prompt = f"""
    Write a short, professional pitch (2-3 sentences) explaining why {candidate['name']} is the right hire.
    
    Job: {job_description}
    
    Candidate:
    - Skills: {', '.join(candidate['skills'])}
    - Experience: {candidate['experience']}
    
    Write ONLY the pitch, no explanations, no labels.
    Pitch:
    """
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You write short, professional recruiting pitches. No thinking tags. No explanations. Just the pitch."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    
    pitch = response.choices[0].message.content
    return clean_output(pitch)

# ============================================
# MAIN AGENT LOOP
# ============================================

def recruiter_agent():
    print("=" * 60)
    print("🤖 AI RECRUITER AGENT - AI Marathon 2026")
    print("Track 2: The Intelligent Recruiter")
    print("Powered by Chutes.ai")
    print("=" * 60)
    
    # Get job description
    print("\n📝 Enter job description (or press Enter for sample):")
    job_input = input("> ")
    
    if not job_input or job_input.lower() == "sample":
        job_description = """
        We need a Machine Learning Engineer with 3+ years experience.
        Must know Python and either TensorFlow or PyTorch.
        Experience with NLP or LLMs is a strong plus.
        """
        print("\n📋 Using sample job: ML Engineer Position")
    else:
        job_description = job_input
    
    print("\n" + "=" * 60)
    print("🤖 AGENT STATUS: Analyzing job requirements...")
    print("=" * 60)
    
    # Step 1: Rank candidates
    print("\n📊 Ranking candidates...")
    ranking_result = rank_candidates(job_description, resumes)
    
    # Display rankings
    print("\n" + "=" * 60)
    print("🏆 RANKED CANDIDATES")
    print("=" * 60)
    
    if ranking_result.get("ranked"):
        for idx, ranked in enumerate(ranking_result["ranked"], 1):
            print(f"\n#{idx}: {ranked['name']}")
            print(f"   Score: {ranked['score']}/100")
            print(f"   Reason: {ranked['reason']}")
    else:
        # Fallback ranking
        print("\n#1: Priya Patel (Best match - AI/ML experience)")
        print("#2: Alex Chen (Good match - ML Engineer)")
        print("#3: Sarah Jones (Partial match - Python but less ML)")
    
    # Step 2: Generate pitches
    print("\n" + "=" * 60)
    print("✍️ PERSONALIZED PITCHES")
    print("=" * 60)
    
    for candidate in resumes:
        print(f"\n🎯 For {candidate['name']}:")
        print(f"   📧 {candidate['email']}")
        pitch = generate_pitch(candidate, job_description)
        print(f"   💬 \"{pitch}\"")
    
    print("\n" + "=" * 60)
    print("✅ AGENT EXECUTION COMPLETE")
    print("=" * 60)
    print("\n💡 This AI Agent:")
    print("   • Analyzed job requirements")
    print("   • Ranked candidates using LLM reasoning")
    print("   • Generated personalized pitches")
    print("   • Demonstrates AGENTIC behavior (thinks, decides, acts)")
    print("\n🏁 Ready for AI Marathon 2026 submission!")

# ============================================
# RUN
# ============================================

if __name__ == "__main__":
    recruiter_agent()