# Interview Transcript Summarizer

A command-line Python script that takes an interview transcript as input and produces
a structured summary using an LLM API. The summary includes topics covered, candidate
profile, and a candidate summary.

---

## How to Run

### 1. Clone or Download the Repository
Download all files into a folder on your computer.

### 2. Install Dependencies
Open your terminal and run:
```bash
pip install groq python-dotenv
```

### 3. Set Up Your API Key
Create a file called `.env` in the same folder as `summarizer.py` and add:

Replace `your_api_key_here` with your actual Groq API key.
You can get a free key at https://console.groq.com

> ⚠️ Never share this file or commit it to GitHub. It is already listed in `.gitignore`.

### 4. Add Your Transcript
Place your transcript `.txt` file in the same folder as `summarizer.py`.

### 5. Run the Script
```bash
python summarizer.py your_transcript_file.txt
```

The summary will be printed in the terminal and also saved as a new `.txt` file
in the same folder. Each run creates a new numbered file so nothing gets overwritten:
- First run → `your_transcript_file_summary_v1.txt`
- Second run → `your_transcript_file_summary_v2.txt`

### Example
```bash
python summarizer.py sample_transcript_assignment_1.txt
```

---

## LLM Provider and Model

- **Provider:** Groq
- **Model:** `llama-3.1-8b-instant`
- **Why Groq:** Free tier with no credit card required, fast inference, and generous
  daily limits (14,400 requests/day) — more than enough for this task.

---

## Reflection

### What Surprised Me
The biggest surprise was how sensitive the model was to vague role descriptions.
In my first prompt iteration, simply asking for "the role this candidate fits" caused
the model to label a Frontend/Full-stack engineer as a "Backend Engineer" — because
the candidate also briefly mentioned Node.js. I had to explicitly tell the model to
look at what the candidate *primarily* discusses rather than what they mention in passing.

Another surprise was how well the model handled two very different transcript styles —
one was a technical engineering interview and the other was a program management interview.
With a well-structured prompt, the same script handled both without any special casing.

### What I Would Improve With Another Day
- **Stricter topic deduplication:** The model still occasionally lists similar topics
  separately (e.g., "Angular" and "Angular Framework"). I would add a post-processing
  step to merge near-duplicate bullet points.
- **Confidence scoring:** Add a section to the output that rates how confident the model
  is about the candidate profile — useful when transcripts are short or vague.
- **Multi-transcript batch mode:** Allow the script to process an entire folder of
  transcripts at once instead of one at a time.
- **Output formatting options:** Add a flag to export the summary as a PDF or structured
  JSON for easier integration into recruitment tools.

### Limitations of the Final Prompt
- The role detection relies on keyword matching logic in the prompt. If a candidate
  discusses an unusual or niche role, the model may still misclassify them.
- The prompt works best with transcripts that are at least 500 words. Very short or
  vague transcripts may produce generic summaries with little specific insight.
- The model may occasionally still list more than the requested 5-7 topics if the
  transcript covers many distinct themes.
- The prompt is in English and assumes the transcript is also in English. Mixed-language
  transcripts (e.g., Hindi + English) may produce inconsistent results.

---

## Files in This Repository

| File | Description |
|------|-------------|
| `summarizer.py` | Main script — reads transcript and produces structured summary |
| `prompt_iterations.md` | Log of 3 prompt iterations with outputs and reasoning |
| `README.md` | This file — setup instructions and reflection |
| `.gitignore` | Ensures `.env` file is never committed to GitHub |
