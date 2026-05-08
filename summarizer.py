import os
import sys
from groq import Groq
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()

# Connect to Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Read the transcript file
def read_transcript(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Send transcript to AI and get summary
def summarize_transcript(transcript_text):
    prompt = f"""
You are an expert technical recruiter. Analyze the following interview transcript and produce a structured summary with exactly three sections:

1. TOPICS COVERED
List the main themes as short bullet points — maximum 5 words each.
Keep it to 5-7 unique topics only. Do NOT repeat similar topics.
(e.g., "System design experience", "Conflict resolution", "Career goals")

2. CANDIDATE PROFILE
Determine the candidate's role by looking at what they PRIMARILY talk about:
- If they spend most time discussing UI, frontend frameworks (React, Angular, Vue, CSS, Tailwind, Ionic) 
  → they are a Frontend Engineer or Full-stack Engineer, NOT a backend engineer
- If they ONLY discuss servers, databases, APIs with no frontend mention → Backend Engineer
- If they discuss project/program management, stakeholders, KPIs, vendors → Project/Program Manager
- If they discuss data, ML, analytics → Data Scientist or Analyst

IMPORTANT: Do not call someone a Backend Engineer if they primarily discuss frontend or mobile frameworks.

Format your answer as: "[Role] — [Level]"
Then write 2-3 sentences justifying this using specific technologies or examples from the transcript.

3. CANDIDATE SUMMARY
Write a paragraph of 3-6 sentences covering:
- Their background and years of experience
- Their top 2 strengths with specific examples from the transcript
- One notable concern or weakness
- Overall hiring impression

---
TRANSCRIPT:
{transcript_text}
---

Provide only the three sections above. Be specific and base everything only on what is in the transcript.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content

# Main program
def main():
    # Check if user provided a filename
    if len(sys.argv) < 2:
        print("Usage: python summarizer.py <transcript_file.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    print(f"\n📄 Reading transcript: {file_path}")
    transcript = read_transcript(file_path)

    print("🤖 Analyzing transcript...\n")
    summary = summarize_transcript(transcript)

    print("=" * 60)
    print("INTERVIEW SUMMARY")
    print("=" * 60)
    print(summary)
    print("=" * 60)

    # Save output to a new numbered file each time
    base_name = file_path.replace(".txt", "")
    iteration = 1
    while os.path.exists(f"{base_name}_summary_v{iteration}.txt"):
        iteration += 1
    output_file = f"{base_name}_summary_v{iteration}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"\n✅ Summary saved to: {output_file}")

if __name__ == "__main__":
    main()