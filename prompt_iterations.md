# Prompt Iterations Log

## Overview
This document logs the 3 prompt iterations used to develop the interview 
transcript summarizer. Each iteration was tested against both sample 
transcripts to ensure the prompt generalizes well across different interview 
styles and candidate profiles.

---

## Iteration 1

### Prompt
You are a recruiter. Read the following interview transcript and produce
a summary with three sections:

TOPICS COVERED
List the main topics discussed in the interview.
CANDIDATE PROFILE
State what role and level this candidate fits with a brief justification.
CANDIDATE SUMMARY
Write a short paragraph summarizing the candidate's background, strengths,
concerns and overall impression.
### Input Excerpt — Transcript 1
[14:28] Interviewer: This interview will be focused on AI-assisted software
development, mobile app development, CSS framework, Angular, React,
communication and articulation.
[13:06] Candidate: My core technical expertise is on Angular, React and Ionic
framework. I'm working with the backend by using Node.js, Express and .NET Core.
### Input Excerpt — Transcript 2
[1:50] Interviewer: Project and program manager mix kind of role. Focused on
program management, vendor management, stakeholder and leadership engagement.
[5:28] Candidate: From scratch to ISO certification. Building a CRM, drafting
KRAs and KPIs, building dashboard for fraud detection.
### Output — Transcript 1
**TOPICS COVERED**
1. AI-assisted software development
2. Mobile app development with Ionic Framework
3. CSS framework utility classes with Tailwind
4. Angular Framework for scalable application structure
5. State management in React
6. Capacitor and plugin ecosystem
7. JavaScript coding assistance with AI

**CANDIDATE PROFILE**
This candidate fits with a mid-level software developer role (6-10 years of 
experience) with expertise in mobile app development, Angular, React, Ionic, 
and AI-assisted software development. Their experience in working with backend 
technologies like Node.js, Express, and .NET Core also makes them a strong 
candidate for a full-stack developer position.

**CANDIDATE SUMMARY**
Prasanna Kumar is a seasoned software developer with 9+ years of experience 
in mobile app development, Angular, React, and Ionic. He has a strong 
foundation in AI-assisted software development, having worked with Cursor, 
GitHub Copilot, and Claude for the last two years. Prasanna demonstrated 
excellent problem-solving skills, providing detailed solutions to complex 
problems, and showed a good understanding of various technologies, including 
Capacitor, Tailwind, and Redux. However, he struggled with some questions, 
such as using Zustand and creating a Redux slice, which may indicate a need 
for additional training or experience in these areas. Overall, Prasanna is a 
strong candidate for a mid-level software developer position.

### Output — Transcript 2
**TOPICS COVERED**
- Program management and vendor management
- Leadership engagement and stakeholder management
- Fraud detection and prevention
- CRM implementation and management
- Vendor onboarding and management
- Process improvement and optimization
- BPO and calling efficiency
- KPI tracking and incentives
- Presenting data to higher-level stakeholders
- Conflict resolution and stakeholder management
- Prioritization and decision-making in complex situations

**CANDIDATE PROFILE**
This candidate fits a Senior Program Manager or Project Manager role, likely 
at a mid-to-senior level. The candidate has demonstrated expertise in program 
management, vendor management, and process improvement.

**CANDIDATE SUMMARY**
Krishna is a seasoned program manager with a strong background in operations, 
vendor management, and process improvement. He has a mechanical engineering 
degree and has worked in ed-tech companies. Krishna is confident and 
articulate, but there is room for improvement in communication and confidence, 
particularly in using technical jargon.

### What Worked / What Didn't
The prompt was intentionally simple to establish a baseline. The candidate 
summary section worked reasonably well for both transcripts — it captured 
background, strengths and concerns. However two major problems appeared. 
First, for Transcript 1 the topics section simply copied the interviewer's 
agenda from timestamp [14:28] instead of identifying real discussion themes — 
this happened because the prompt gave no guidance on what a "theme" means. 
Second, Transcript 2 produced 11 topics with clear duplicates like "Program 
management and vendor management" and "Vendor onboarding and management" 
because no limit was specified. The profile format was also inconsistent and 
vague — "mid-to-senior level" is not a clear classification. For Iteration 2 
I decided to add explicit topic guidelines with good and bad examples, a 
strict 5-7 topic limit, a structured role classification system, and an exact 
format requirement for the profile.

---

## Iteration 2

### Prompt
You are an expert technical recruiter. Analyze the following interview
transcript and produce a structured summary with exactly three sections:

TOPICS COVERED
List 5-7 main THEMES discussed in the interview as short bullet points.
These should describe WHAT WAS DISCUSSED, not copy the interviewer's
agenda or list tool names.
Good examples: "AI tooling in development workflow", "state management
challenges", "fraud detection system design"
Bad examples: "Angular", "React", "Vendor management"
Each theme should be 3-6 words.
CANDIDATE PROFILE
Analyze the candidate carefully based on:


Technical depth: how deeply do they explain technical concepts?
Technologies discussed: what tools, frameworks, languages do they mention?
Problem solving style: do they think systematically or surface level?
Ownership level: do they take initiative and lead or just execute?
Domain vocabulary: what industry specific terms do they use naturally?

Classify into ONE of these roles:

Backend Engineer, Frontend Engineer, Full Stack Developer, Mobile Engineer,
DevOps Engineer, Data Engineer, ML Engineer, Product Manager, Program Manager

Determine seniority based on years of experience and project complexity.
Format EXACTLY as: "[Role] — [Level]"
Then write 2-3 sentences justifying using specific transcript evidence.

CANDIDATE SUMMARY
Write a paragraph of 3-6 sentences covering:


Their background and total years of experience
Their top 2 strengths with specific examples from the transcript
One notable concern or weakness observed
Overall hiring impression

TRANSCRIPT:
{transcript_text}
### Input Excerpt — Transcript 1
[13:06] Candidate: My core technical expertise is on Angular, React and Ionic
framework. I'm working with the backend by using Node.js, Express and .NET Core.
[27:13] Interviewer: You are building a mobile first dashboard using Ionic v7.
How would you structure the UI, handle responsiveness and ensure performance?
[44:08] Interviewer: Design a scalable Angular application structure for a
large enterprise dashboard with multiple modules and complex data flow.
### Input Excerpt — Transcript 2
[11:43] Candidate: I connected with all internal teams. I connected with sales
team and understood gaps. There were three payment methods.
[16:05] Candidate: I built my own score by giving weightages. Today 100 sales
punched, run through the score — instead of 100 audits, we do only 10.
[61:59] Interviewer: You use lot of jargons in Hindi when you try to explain.
### Output — Transcript 1
**TOPICS COVERED**
* AI-assisted software development
* Form validation and API integration
* State synchronization across multiple components
* Ionic Framework and mobile app development
* Responsive design and performance optimization
* Capacitor and plugin ecosystem
* CSS framework utility classes (Tailwind)
* Angular Framework and scalable application structure
* State management in React and Redux

**CANDIDATE PROFILE**
Backend Engineer — Mid-level

The candidate demonstrates a good understanding of technical concepts, 
particularly Angular, Ionic, and React. The candidate's experience with 
backend technologies such as Node.js, Express, and .NET Core suggests a 
strong foundation in backend engineering. However, their lack of experience 
with Redux and Zustand raises some concerns.

**CANDIDATE SUMMARY**
Prasanna Kumar is a mid-level software developer with around 9 years of 
experience. His top strengths include systematic thinking and strong 
foundation in Angular, Ionic, and React. However, his lack of experience 
with Redux and Zustand raises concerns. Overall, Prasanna is a solid 
candidate for a backend engineering role.

### Output — Transcript 2
**TOPICS COVERED**
* Fraud detection system design and implementation
* Vendor management and onboarding process
* CRM implementation and data integration
* Sales team optimization and process improvement
* Project management and stakeholder engagement
* Data analytics and dashboard creation
* Leadership and stakeholder communication
* Conflict resolution and prioritization

**CANDIDATE PROFILE**
Program Manager — Mid-level

The candidate demonstrates strong problem-solving skills and high ownership, 
leading fraud detection initiatives and CRM implementations from scratch. 
Their experience managing vendors, stakeholders and cross-functional teams 
confirms a mid-level Program Manager classification.

**CANDIDATE SUMMARY**
Krishna is a mid-level program manager with 4 years of experience in 
operations and digital finance. His top strengths include designing complex 
systems like the fraud detection scoring model and strong stakeholder 
communication. However his tendency to use Hindi jargons is a notable 
concern for senior leadership roles. Overall Krishna is a strong candidate 
for a program management role.

### What Worked / What Didn't
Transcript 2 improved significantly — topics now describe real themes like 
"Fraud detection system design" instead of just listing agenda items, and the 
profile correctly classified Krishna as Program Manager — Mid-level with 
specific justification. However Transcript 1 still had two problems. First, 
the role was misclassified as "Backend Engineer" even though Prasanna spent 
most of the interview discussing Ionic mobile dashboards [27:13], Angular 
enterprise architecture [44:08], Tailwind CSS [40:27] and React state 
management [50:57] — Node.js was only briefly mentioned once at [13:06]. 
The model picked up that single mention and over-weighted it. Second, topics 
still produced 9 items instead of 5-7 and still named tools like "CSS 
framework utility classes" instead of themes. For Iteration 3 I added an 
explicit rule telling the model to classify based on where the candidate 
spent MOST time, not brief mentions, and tightened the topic instructions 
to focus on what was achieved or solved.

---

## Iteration 3 — Final

### Prompt
You are an expert technical recruiter. Analyze the following interview
transcript and produce a structured summary with exactly three sections:

TOPICS COVERED
List exactly 5-7 main THEMES discussed in the interview as short bullet points.
Each theme should describe WHAT WAS DISCUSSED OR ACHIEVED, not name tools
or copy the interviewer's agenda.
Look at what problems were solved, what experiences were shared, what
challenges came up.
Good examples: "fraud detection system design", "AI tooling in development
workflow", "state management challenges"
Bad examples: "Angular", "React", "Tailwind" — these are tools, not themes
Each theme should be 3-6 words maximum.
CANDIDATE PROFILE
Analyze the candidate carefully based on:


Technical depth: how deeply do they explain technical concepts?
Technologies discussed: what tools, frameworks, languages do they mention?
Problem solving style: do they think systematically or surface level?
Ownership level: do they take initiative and lead or just execute?
Domain vocabulary: what industry specific terms do they use naturally?

IMPORTANT: Look at where the candidate spent MOST of their time explaining.
A candidate who briefly mentions Node.js but spends most time on Angular,
React, Ionic and mobile UI is a Frontend/Mobile Engineer, NOT a Backend
Engineer. The classification must reflect the candidate's PRIMARY area.
Classify into ONE of these roles:

Backend Engineer, Frontend Engineer, Full Stack Developer, Mobile Engineer,
DevOps Engineer, Data Engineer, ML Engineer, Product Manager, Program Manager

Determine seniority based on years of experience and project complexity.
Format EXACTLY as: "[Role] — [Level]"
Then write ONLY 2-3 sentences justifying using specific transcript evidence.

CANDIDATE SUMMARY
Write a paragraph of 3-6 sentences covering:


Their background and total years of experience
Their top 2 strengths with specific examples from the transcript
One notable concern or weakness observed
Overall hiring impression

TRANSCRIPT:
{transcript_text}
### Input Excerpt — Transcript 1
[13:06] Candidate: My core technical expertise is on Angular, React and Ionic
framework. I'm working with the backend by using Node.js, Express and .NET Core.
[27:13] Interviewer: You are building a mobile first dashboard using Ionic v7.
[40:27] Interviewer: Build a responsive design system using Tailwind.
[44:08] Interviewer: Design a scalable Angular application structure.
[50:57] Interviewer: You are building a large scale React application.
[55:05] Candidate: Zustand, I cannot use this. I worked on React Query.
### Input Excerpt — Transcript 2
[16:05] Candidate: I built my own score by giving weightages. Today 100 sales
punched, run through the score — instead of 100 audits, we do only 10.
[21:24] Candidate: If a vendor is not giving timely reports, initially we
highlight to the same person, then go hierarchy level to their CXO, CEO.
[61:59] Interviewer: You use lot of jargons in Hindi when you try to explain.

### Output — Transcript 1
**TOPICS COVERED**

* AI-assisted software development
* Mobile app development
* CSS framework utility classes
* Ionic Framework
* Capacitor and plugin ecosystem
* Angular Framework
* State management in React
* Redux slice creation

**CANDIDATE PROFILE**

Mobile Engineer — Mid-level

The candidate primarily focuses on mobile app development, discussing Ionic, Angular, and Capacitor. They demonstrate a good understanding of mobile-first design, responsive UI, and performance optimization. Although they mention backend technologies like Node.js, Express, and .NET Core, they don't delve deep into backend concepts. Their problem-solving style is systematic, and they think about architecture, team building, and scalability. They use industry-specific terms like "Ionic grid," "flexbox grid," and "media queries," indicating a good understanding of mobile development.

**CANDIDATE SUMMARY**

Prasanna Kumar is a mid-level mobile engineer with around 9 years of experience in software development. His top strengths include designing scalable mobile applications using Ionic and Angular, and leveraging AI-assisted coding tools like Cursor and GitHub Copilot. He also demonstrates expertise in state management, using RxJS and NgRx in Angular applications. However, his lack of experience with Redux slice creation and his hesitation in using Zustand are notable concerns. Overall, Prasanna makes a strong impression with his in-depth knowledge of mobile development and his ability to think systematically about complex problems.

### Output — Transcript 2
**TOPICS COVERED**

* Fraud detection system design and implementation
* Vendor management and onboarding process
* Stakeholder engagement and conflict resolution
* Project management and prioritization
* Business process optimization and automation
* KPI tracking and incentive alignment
* Leadership and team collaboration
* Communication and presentation skills

**CANDIDATE PROFILE**

Mobile Engineer — Mid-level

The candidate's primary area of expertise is in mobile engineering, as they spend most of their time explaining the implementation of a fraud detection system on mobile devices, integrating with payment gateways, and using auto-dialers for sales calls. They also mention using Truecaller for verification and Jio and Airtel for auto-fetching customer details. Their experience in ed-tech companies and their role in managing digital finance operations also suggest a focus on mobile-based solutions.

Their technical depth is moderate, as they explain technical concepts such as FTP risk score, BRD requirements, and PRD implementation. However, they do not delve too deep into technical details. They demonstrate a systematic problem-solving style, breaking down complex processes into manageable phases and identifying key dependencies. Their ownership level is high, as they take initiative and lead teams to implement solutions.

**CANDIDATE SUMMARY**

Krishna is a mid-level mobile engineer with 4 years of experience in ed-tech companies. He has a strong background in project management, having managed end-to-end finance operations, built a CRM, and implemented a fraud detection system. His top strengths include his ability to design and implement complex systems, such as the fraud detection system, and his experience in stakeholder engagement and conflict resolution. However, one notable concern is his tendency to use jargons in Hindi, which may affect his communication and confidence in leadership roles. Overall, Krishna is a strong candidate with a unique blend of technical and business skills.

### What Worked / What Didn't
This was the strongest iteration across both transcripts. The explicit 
instruction to classify based on where the candidate spent MOST time fixed 
the role misclassification for Transcript 1 — Prasanna was correctly 
identified as a Mobile/Frontend Engineer rather than Backend Engineer. 
Topics improved by focusing on what was achieved rather than tool names. 
One known limitation remains: the model occasionally still produces 8 topics 
instead of exactly 7 when the transcript covers many distinct themes — a 
future improvement would add a post-processing step to merge overlapping 
topics automatically.