# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? --> 

My domain is Howard University housing advice for students. I chose this domain because finding the right housing can be difficult for students, especially when deciding between residence halls, off-campus housing, and other living arrangements. Official university resources provide important information about housing policies and the application process, but they may not include the personal experiences and advice that students are looking for. Information about dorm experiences, off-campus options, housing recommendations, and common concerns can be spread across different websites and student discussions. This guide will bring that information together so students can ask housing-related questions and receive relevant answers based on the collected sources.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->


| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Housing with Parents | Discusses living with parents while attending Howard, including commuting, housing exemptions, saving money, and the social impact of living off campus. | https://www.reddit.com/r/HowardUniversity/comments/1k9944k/housing_with_parents/ |
| 2 | Transfer Student Looking for Housing | Provides housing advice for transfer students, including finding roommates, off-campus apartments, and contacting Howard for housing assistance. | https://www.reddit.com/r/HowardUniversity/comments/1v0qd0w/transfer_student_looking_for_housing/ |
| 3 | Thoughts on Carver/Slowe Apartments | Shares student and parent experiences with Carver/Slowe Apartments regarding affordability, safety, amenities, management, and proximity to Howard. | https://www.reddit.com/r/HowardUniversity/comments/1tnu0sj/thoughts_on_carverslowe_apartments/ |
| 4 | Help Picking Dorm | Provides student opinions on Howard dorms, including bathrooms, maintenance, residence hall preferences, and dorm essentials. | https://www.reddit.com/r/HowardUniversity/comments/1cr0kyd/help_picking_dorm |
| 5 | Resident Hall Recommendations | Offers recommendations for Howard residence halls based on safety, social life, bathrooms, location, kitchens, and overall student experience. | https://www.reddit.com/r/HowardUniversity/comments/1snfwjv/resident_hall_recommendations/ |
| 6 | Apply for Housing | Explains Howard University's housing application process, including StarRez, fees, eligibility, assignments, waitlists, deposits, and exemptions. | https://studentaffairs.howard.edu/housing/apply-housing |
| 7 | 6 Tips for Finding Off-Campus Housing | Provides tips for finding off-campus housing, including choosing roommates, budgeting, location, amenities, and avoiding rental scams. | https://studentaffairs.howard.edu/articles/6-tips-finding-campus-housing |
| 8 | Off-Campus Housing & Community Engagement | Explains the resources Howard provides to help students find off-campus housing, understand leases, move in, and engage with their communities. | https://studentaffairs.howard.edu/about/departments/office-off-campus-housing-community-engagement |
| 9 | Housing | Provides an overview of Howard's on-campus and off-campus housing options, residence halls, move-in resources, and other housing services. | https://studentaffairs.howard.edu/housing |
| 10 | Find Off-Campus Housing | Explains Howard's off-campus housing options and the difference between independent off-campus properties and university-sponsored housing. | https://studentaffairs.howard.edu/housing/find-off-campus-housing |                                                                                                                       

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->


**Chunk size:500 characters

**Overlap: 100 characters

**Reasoning:My documents contain a mix of housing information, advice, and student discussions. A chunk size of 500 characters should be large enough to keep related information together while still being small enough for the system to retrieve specific housing information. I will use an overlap of 100 characters so that important information near the end of one chunk is also included at the beginning of the next chunk. This reduces the chance that a useful sentence or idea is separated across two chunks.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->



**Embedding model: all-MiniLM-L6-v2 via sentence-transformers

**Top-k:4

**Production tradeoff reflection: I chose all-MiniLM-L6-v2 because it is fast, lightweight, and can run locally without an API key, which makes it a good choice for this project. If this system were being used by real students, I would also consider whether a larger embedding model could provide more accurate search results. I would compare accuracy, response time, multilingual support, and the computing resources required. A larger model may understand more complex questions better, but it could also be slower and require more resources.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What factors should students consider when searching for off-campus housing? | Students should consider factors such as budget, location, roommates, amenities, and avoiding rental scams. |
| 2 | What should students know about applying for Howard University housing? | The answer should explain relevant parts of Howard's housing application process, such as eligibility, fees, assignments, waitlists, deposits, or exemptions based on the source. |
| 3 | What is the difference between independent off-campus housing and university-sponsored housing? | The answer should explain the distinction described in the Find Off-Campus Housing source. |
| 4 | What do students recommend when choosing a residence hall at Howard? | The answer should summarize relevant student recommendations and experiences from the residence hall and dorm discussion sources. |
| 5 | What do students say about Carver/Slowe Apartments? | The answer should summarize the experiences or opinions specifically contained in the Carver/Slowe student discussion. |
---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->     

1. Some of the student housing discussions may contain opinions, outdated information, or experiences that conflict with other sources. This could cause the system to retrieve information that does not accurately represent current Howard University housing policies. I will reduce this risk by keeping the source information attached to each chunk so users can see where the information came from.

2. Important housing information may be split between different chunks or documents. If the system retrieves only one part of the information, the generated answer could be incomplete. I will use overlapping chunks and retrieve multiple relevant chunks for each question to reduce the chance of important context being missed.
---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -- >

Howard Housing Documents (.txt files)
        |
        v
Document Ingestion
Python loads the housing text files from the documents folder
        |
        v
Chunking
Documents are split into 500-character chunks
with a 100-character overlap
        |
        v
Embedding + Vector Store
all-MiniLM-L6-v2 converts the chunks into embeddings
ChromaDB stores the chunks and embeddings
        |
        v
Retrieval
The user enters a housing-related question
The system retrieves the top 4 most relevant chunks
        |
        v
Generation
The retrieved chunks are sent to the Groq LLM
The LLM uses the retrieved information to generate a grounded answer
The answer includes the sources where the information came from

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking :**

I plan to use ChatGPT to help implement the document ingestion and chunking portion of the pipeline. I will provide ChatGPT with my Chunking Strategy and Architecture sections from planning.md and explain that my housing documents are stored as .txt files in the documents folder. I will ask it to help create Python code that loads the documents, keeps track of each source, and splits the text into 500-character chunks with a 100-character overlap. I expect the output to be Python code for loading and chunking my documents. I will verify the output by running the code and inspecting sample chunks to make sure the documents are loaded correctly, the chunk sizes follow my plan, and the source information is preserved.

**Milestone 4 — Embedding and retrieval: **

I plan to use ChatGPT to help implement the embedding and retrieval portion of the pipeline. I will provide my Retrieval Approach and Architecture sections and ask it to help use the all-MiniLM-L6-v2 embedding model with ChromaDB. I will ask it to create embeddings for my document chunks, store them in ChromaDB, and retrieve the top 4 relevant chunks for a user's housing question. I expect the output to be Python code that performs embedding, storage, and semantic retrieval. I will verify the output by testing several of my evaluation questions and checking whether the retrieved chunks are actually relevant to each question.



**Milestone 5 — Generation and interface: **

I plan to use ChatGPT to help implement the generation and user interface portion of the pipeline. I will provide my Architecture, Retrieval Approach, and Evaluation Plan and ask it to help connect the retrieved chunks to the Groq LLM and create the query interface. I will specify that the LLM should answer questions using only the retrieved housing information, include source attribution, and refuse to make up an answer when the documents do not contain enough information. I expect the output to include Python code for grounded response generation and the user interface. I will verify the output by running my five evaluation questions, checking the cited sources, and testing an out-of-scope question to make sure the system does not invent an answer.
