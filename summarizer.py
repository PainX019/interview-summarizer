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
List exactly 5-7 main THEMES discussed in the interview as short bullet points.
Each theme should describe WHAT WAS DISCUSSED OR ACHIEVED, not name tools or copy the interviewer's agenda.
Look at what problems were solved, what experiences were shared, what challenges came up.
Good examples: "fraud detection system design", "AI tooling in development workflow", "state management challenges"
Bad examples: "Angular", "React", "Tailwind" — these are tools, not themes
Each theme should be 3-6 words maximum.

2. CANDIDATE PROFILE
Analyze the candidate carefully based on:
- Technical depth: how deeply do they explain technical concepts?
- Technologies discussed: what tools, frameworks, languages do they mention?
- Problem solving style: do they think systematically or surface level?
- Ownership level: do they take initiative and lead or just execute?
- Domain vocabulary: what industry specific terms do they use naturally?

IMPORTANT: Look at where the candidate spent MOST of their time explaining.
A candidate who briefly mentions Node.js but spends most time on Angular, React, 
Ionic and mobile UI is a Frontend/Mobile Engineer, NOT a Backend Engineer.
The classification must reflect the candidate's PRIMARY area of expertise.

Classify the candidate into ONE of these roles:
- Backend Engineer
- Frontend Engineer
- Full Stack Developer
- Mobile Engineer
- DevOps Engineer
- Data Engineer
- ML Engineer
- Product Manager
- Program Manager

Determine seniority level based on:
- Total years of industry experience mentioned
- Complexity of projects handled
- Whether they lead teams or just execute tasks

Format EXACTLY as: "[Role] — [Level]"
Example: "Mobile Engineer — Senior" or "Program Manager — Mid-level"

Then write ONLY 2-3 sentences justifying using specific evidence from the transcript.

3. CANDIDATE SUMMARY
Write a paragraph of 3-6 sentences covering:
- Their background and total years of experience
- Their top 2 strengths with specific examples from the transcript
- One notable concern or weakness observed
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