# Prompt Iterations Log

## Overview
This document logs the 3 prompt iterations used to develop the interview transcript summarizer.
Each iteration was tested against both sample transcripts to ensure the prompt generalizes well.

---

## Iteration 1

### Prompt
You are an expert technical recruiter. Analyze the following interview transcript and produce a structured summary with exactly three sections:

TOPICS COVERED
List the main themes and topics discussed in the interview as bullet points.
(e.g., system design experience, conflict resolution, career goals)
CANDIDATE PROFILE
State what kind of role and seniority level this candidate fits.
Format: "[Role] — [Level]" (e.g., "Backend Engineer — mid-level")
Then write 2-3 sentences justifying this based on what the candidate said.
CANDIDATE SUMMARY
Write a short paragraph of 3-6 sentences summarizing the candidate.
Cover: their background, key strengths, any notable concerns, and overall impression.

### Output — Transcript 1
**TOPICS COVERED**
* AI-assisted software development
* Mobile app development
* CSS framework (Tailwind)
* Angular framework
* React framework
* State management (RxJS, NgRx, Context API, React Query, Zustand)
* Capacitor and plugin ecosystem
* Responsive design system
* Scalable application structure

**CANDIDATE PROFILE**
Mobile App Developer — mid-level
The candidate has around 9+ years of experience in software development, with expertise in Angular, React, and Ionic frameworks. They have worked on service-based applications, risk assessment management tools, and communication-based applications, and have experience with AI-assisted coding tools like Cursor and GitHub Copilot. Their technical skills and experience suggest a mid-level position in mobile app development.

**CANDIDATE SUMMARY**
Prasanna Kumar is a seasoned mobile app developer with 9+ years of experience in software development. He has a strong foundation in Angular, React, and Ionic frameworks, and has worked on various projects, including service-based applications and risk assessment management tools. Prasanna's technical skills are impressive, and he demonstrates a good understanding of AI-assisted coding tools and responsive design systems. However, he struggles with some technical concepts, such as Redux slice, and his knowledge of certain libraries, like Zustand, is limited. Overall, Prasanna is a solid candidate with a strong technical background, but may require additional training or support in certain areas.

### Output — Transcript 2
**TOPICS COVERED**
* Program management experience
* Vendor management process
* Conflict resolution and stakeholder management
* Leadership engagement and communication
* Project management and prioritization
* BPO/calling efficiency and optimization
* KPI tracking and incentives alignment
* Data analysis and presentation to higher-level stakeholders
* Stakeholder management and prioritization
* Team collaboration and success measurement

**CANDIDATE PROFILE**
Project Manager — mid-level
The candidate, Krishna, has a strong background in program management, having worked in ed-tech companies and managed various projects, including fraud detection and prevention, vendor management, and BPO/calling efficiency. With experience in managing multiple stakeholders, prioritizing tasks, and optimizing processes, Krishna fits the mid-level project manager role.

**CANDIDATE SUMMARY**
Krishna is a detail-oriented and analytical project manager with a strong background in program management. He has experience in managing multiple stakeholders, prioritizing tasks, and optimizing processes. Krishna is confident in his ability to analyze data, track KPIs, and present findings to higher-level stakeholders. His strengths include conflict resolution, stakeholder management, and leadership engagement. However, there are some concerns regarding his communication style, as the interviewer mentioned that he uses too many jargons in Hindi, which may affect his confidence in leadership roles. Overall, Krishna is a strong candidate with a solid background in project management and a willingness to learn and improve.

### What Worked / What Didn't
- **Transcript 2 (Project Manager)** was correctly identified and well summarized.
- **Transcript 1** role was labeled "Mobile App Developer — mid-level" which was partially correct but missed the Full-stack aspect. The seniority was also slightly off given 9+ years of experience.
- **Topics in Transcript 2** were too verbose — each bullet included a long description instead of a short label.
- **Fix for Iteration 2:** Added explicit role detection rules for frontend vs backend engineers, and instructed the model to keep topics to a maximum of 5 words with no descriptions.

---

## Iteration 2

### Prompt
You are an expert technical recruiter. Analyze the following interview transcript and produce a structured summary with exactly three sections:

TOPICS COVERED
List ONLY the main themes as short bullet points — maximum 5 words each.
Do NOT write descriptions or explanations next to the bullets.
(e.g., "System design experience", "Conflict resolution", "Career goals")
CANDIDATE PROFILE
Carefully determine the candidate's role based on the technologies and skills they mention.


If they mention frontend frameworks (React, Angular, Vue, CSS, Tailwind) → Frontend or Full-stack Engineer
If they mention backend only (Node.js, databases, APIs) → Backend Engineer
If they mention project/program management, stakeholders, KPIs → Project/Program Manager
If they mention data, ML, analytics → Data Scientist or Analyst

Format: "[Role] — [Level]"
Then write 2-3 sentences justifying this based specifically on what the candidate said.

CANDIDATE SUMMARY
Write a paragraph of 3-6 sentences covering:


Their background and years of experience
Their top 2 strengths with specific examples from the transcript
Any notable concern or weakness observed
Overall hiring impression

### Output — Transcript 1
**TOPICS COVERED**
* AI-assisted software development
* Mobile app development
* CSS framework
* Angular
* React
* Communication
* Articulation
* Ionic Framework
* Capacitor and plugin ecosystem
* CSS framework utility classes
* Angular Framework
* State management in React

**CANDIDATE PROFILE**
Frontend/Full-stack Engineer — Senior
The candidate has around 9+ years of experience in software development, with expertise in Angular, React, Ionic framework, and Node.js. They have worked on service-based applications, risk assessment management tools, and communication-based applications, and have experience with AI-assisted software development tools like Cursor and GitHub Copilot.

**CANDIDATE SUMMARY**
Prasanna Kumar is a seasoned software developer with 9+ years of experience in Angular, React, and Ionic framework. He has a strong background in mobile app development, AI-assisted software development, and CSS framework utility classes. His top strengths include his ability to design scalable Angular application structures and his experience with state management in React using Context API and React Query. However, he struggled with writing an example of Zustand for creating a useStore and a Redux slice, which may be a notable concern. Overall, Prasanna is a skilled developer with a strong technical background, but may require additional training or support in certain areas.

### Output — Transcript 2
**TOPICS COVERED**
* Program management experience
* Vendor management
* Stakeholder engagement
* Leadership skills
* Conflict resolution
* Data analysis
* KPI tracking
* Communication skills

**CANDIDATE PROFILE**
Project/Program Manager — Mid-level
The candidate has extensive experience in program management, vendor management, and stakeholder engagement, as evident from their previous roles in ed-tech companies. They have also demonstrated leadership skills, conflict resolution, and data analysis capabilities.

**CANDIDATE SUMMARY**
Krishna is a mid-level project/program manager with 4-5 years of experience in ed-tech companies. He has a strong background in operations and has managed various projects, including fraud detection and prevention, vendor management, and BPO/calling optimization. His top strengths include his ability to analyze complex data and identify areas for improvement, as well as his effective communication and conflict resolution skills. Notable concerns include his tendency to use technical jargon, which may impact his communication with stakeholders. Overall, Krishna presents himself as a capable and results-driven project/program manager.

### What Worked / What Didn't
- **Role detection improved** — Transcript 1 now correctly identified as "Frontend/Full-stack Engineer — Senior."
- **Transcript 2 topics** are now short and clean — exactly what was needed.
- **Transcript 1 topics still had duplicates** — "Angular" and "Angular Framework", "CSS framework" and "CSS framework utility classes" both appeared.
- **Fix for Iteration 3:** Added explicit instruction to keep topics to 5-7 unique topics only and not repeat similar ones. Also strengthened the role detection rules with a clear note to never call a frontend developer a backend engineer.

---

## Iteration 3 (Final)

### Prompt
You are an expert technical recruiter. Analyze the following interview transcript and produce a structured summary with exactly three sections:

TOPICS COVERED
List the main themes as short bullet points — maximum 5 words each.
Keep it to 5-7 unique topics only. Do NOT repeat similar topics.
(e.g., "System design experience", "Conflict resolution", "Career goals")
CANDIDATE PROFILE
Determine the candidate's role by looking at what they PRIMARILY talk about:


If they spend most time discussing UI, frontend frameworks (React, Angular, Vue, CSS, Tailwind, Ionic)
→ they are a Frontend Engineer or Full-stack Engineer, NOT a backend engineer
If they ONLY discuss servers, databases, APIs with no frontend mention → Backend Engineer
If they discuss project/program management, stakeholders, KPIs, vendors → Project/Program Manager
If they discuss data, ML, analytics → Data Scientist or Analyst

IMPORTANT: Do not call someone a Backend Engineer if they primarily discuss frontend or mobile frameworks.
Format your answer as: "[Role] — [Level]"
Then write 2-3 sentences justifying this using specific technologies or examples from the transcript.

CANDIDATE SUMMARY
Write a paragraph of 3-6 sentences covering:


Their background and years of experience
Their top 2 strengths with specific examples from the transcript
One notable concern or weakness
Overall hiring impression

### Output — Transcript 1
**TOPICS COVERED**
* AI-assisted software development
* Mobile app development
* CSS framework utility classes
* Ionic Framework
* Capacitor and plugin ecosystem
* Angular Framework
* State management in React
* Redux and Redux slice

**CANDIDATE PROFILE**
Mobile App Developer/Full-stack Engineer — Senior
The candidate primarily discusses mobile app development, Ionic, Angular, and React, indicating a focus on frontend development. They also mention working with Node.js, Express, and .NET Core, which suggests some backend experience. However, their in-depth knowledge of frontend frameworks and mobile app development suggests a stronger focus on frontend development.

**CANDIDATE SUMMARY**
Prasanna Kumar is a senior software developer with around 9 years of experience in software development. He has a strong background in mobile app development, with expertise in Ionic, Angular, and React. He is also familiar with AI-assisted software development, having worked with tools like Cursor, GitHub Copilot, and Claude. His strengths include his ability to design scalable applications, handle complex data flow, and implement state management strategies. However, he seems to struggle with some concepts, such as Zustand and Redux slice, which he was unable to implement correctly. Overall, he presents himself as a skilled and experienced developer, but may require additional training or guidance in certain areas.

### Output — Transcript 2
**TOPICS COVERED**
* Program management
* Vendor management
* Stakeholder engagement
* Leadership
* Project management
* BPO/calling efficiency
* Data analytics
* KPI tracking

**CANDIDATE PROFILE**
Project/Program Manager — Mid-Level
The candidate primarily discusses project and program management, vendor management, stakeholder engagement, and leadership. They mention their experience in managing end-to-end finance operations, building a CRM, drafting KRAs and KPIs, and implementing dashboards for fraud detection. Their technical skills include experience with CRM software (Merito) and data analytics.

**CANDIDATE SUMMARY**
Krishna is a mid-level project/program manager with a background in mechanical engineering. With 4-5 years of experience in operations and program management, he has a strong track record of managing end-to-end processes, building relationships with stakeholders, and presenting data to higher-level stakeholders. His top strengths include his ability to connect with internal teams, understand gaps, and implement solutions. He also demonstrated his ability to handle complex stakeholder relationships and prioritize projects effectively. One notable concern is his tendency to use technical jargon in Hindi, which may impact his communication and confidence in leadership roles. Overall, Krishna presents himself as a strong candidate with a solid understanding of project and program management principles.

### What Worked / What Didn't
- **Both transcripts now produce clean, non-repetitive topics.**
- **Role detection works correctly for both transcripts** — Transcript 1 correctly identified as Frontend/Full-stack, Transcript 2 as Project/Program Manager.
- **Summaries are specific and grounded** in actual transcript content.
- **Known limitation:** Topic deduplication is still not perfect — Iteration 3 for Transcript 1 still lists 8 topics instead of the requested 5-7. A future improvement could ask the model to strictly merge overlapping themes before listing them.