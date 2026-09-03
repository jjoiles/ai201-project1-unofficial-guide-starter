# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

     My domain is Howard University housing advice for students. I chose this domain because finding the right housing can be difficult for students, especially when deciding between residence halls, off-campus housing, and other living arrangements. Official university resources provide important information about housing policies and the application process, but they may not include the personal experiences and advice that students are looking for. Information about dorm experiences, off-campus options, housing recommendations, and common concerns can be spread across different websites and student discussions. This guide will bring that information together so students can ask housing-related questions and receive relevant answers based on the collected sources.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

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

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 500 characters

**Overlap:** 100 characters

**Why these choices fit your documents:** I used a chunk size of 500 characters because my housing documents consist mainly of short informational pages and student discussions. This size keeps related information together while still making the chunks small enough for relevant information to be retrieved. I used a 100-character overlap so that important context is not lost when information is split between two chunks.

**Final chunk count:** 87 chunks across 10 documents.

---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->

| # | Source document | Chunk text |
|---|----------------|------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

| # | Source document | Chunk text |
|---|-----------------|------------|
| 1 | 6 Tips for Finding Off-Campus Housing.txt | Title: 6 Tips for Finding Off-Campus Housing. Source: https://studentaffairs.howard.edu/articles/6-tips-finding-campus-housing. Selecting the perfect off-campus apartment is a huge responsibility, one that should not be taken lightly. Before embarking on your search, we want to ensure that you have the steps, tips, and tools you need to help you find your next apartment home. Read our six tips below and please contact the Office of Off-Campus Housing at offcampushousing@howard.edu if you have any |
| 2 | 6 Tips for Finding Off-Campus Housing.txt | w and please contact the Office of Off-Campus Housing at offcampushousing@howard.edu if you have any questions as you embark on your search. 1. Select Your Roommate or Ride Solo. Before selecting an off-campus apartment, you need to decide whether you want to live by yourself or with others. If you decide to live with others, please ensure that all individuals involved are on the same page regarding living preferences. Are you early birds? Night owls? How often do you like to entertain gues |
| 3 | 6 Tips for Finding Off-Campus Housing.txt | garding living preferences. Are you early birds? Night owls? How often do you like to entertain guests? Remember, don't be afraid to ask questions! This will be a home that you all will share for the duration of the lease. If you need additional help, please view this list of questions to ask potential roommates. You can even listen to past episodes of our Dear Roommate Podcast to hear a number of topics our Bison have addressed regarding living with roommates. 2. Determine Your Budget Aft |
| 4 | 6 Tips for Finding Off-Campus Housing.txt | of topics our Bison have addressed regarding living with roommates. 2. Determine Your Budget. After determining who (if anyone) you will live with, you need to determine your budget. Understanding what you can afford to pay requires an honest look at your spending and, if necessary, a willingness to cut back to afford housing costs. Additionally, if your parents are paying for the cost of the apartment, they need to be a part of the process from start to finish. It is recommended that you sp |
| 5 | 6 Tips for Finding Off-Campus Housing.txt | partment, they need to be a part of the process from start to finish. It is recommended that you spend no more that 30 to 40 percent of your monthly income on rent. Please keep this and the following costs in mind when as your finalize your budget: Security Deposits: Many apartments charge a security deposit to cover the costs of potential damage. They could cost up to a month's rent, so be sure that you have considered this. Utilities and Amenities: Did you know that some apartments charge e |

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:** I used all-MiniLM-L6-v2 because it is lightweight, fast, and can run locally without requiring a separate embedding API key. It was a good fit for this project because my dataset is relatively small and mostly contains English housing information and student discussions. If I were deploying this system for real users and cost was not a constraint, I would compare other embedding models based on retrieval accuracy, context length, multilingual support, latency, and whether the model runs locally or through an API. A larger or more advanced model might understand more complex or domain-specific housing questions better, but it could also be slower and require more computing resources. I would also consider a multilingual model if the system needed to support students asking questions in languages other than English.

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->


Relevance explanation:
**Query 1:** What should students consider when looking for off-campus housing?

Top returned chunks:
- **Result 1 — Source: 6 Tips for Finding Off-Campus Housing.txt, Chunk 0:** Selecting the perfect off-campus apartment is a huge responsibility, one that should not be taken lightly. Before embarking on your search, students should have the steps, tips, and tools needed to find their next apartment home.
- **Result 2 — Source: 6 Tips for Finding Off-Campus Housing.txt, Chunk 1:** Before selecting an off-campus apartment, students need to decide whether they want to live by themselves or with others. If living with others, everyone should be on the same page regarding living preferences.
- **Result 3 — Source: Housing.txt, Chunk 2:** Living off campus is an opportunity for students to prepare for life after college, exercise independence in their own living space, and still receive support from the university.
- **Result 4 — Source: Find Off-Campus Housing.txt, Chunk 2:** This chunk discusses off-campus housing options, being a respectful member of the surrounding community, and the University housing waitlist.

Relevance explanation:
The retrieval results were relevant to the question because they provided information students should consider when looking for off-campus housing. The strongest results were the first two chunks because they directly discussed preparing for an apartment search, deciding whether to live alone or with roommates, and considering living preferences. Results 3 and 4 were also related to off-campus housing, although they provided more general information and were less directly focused on factors students should consider during their housing search.

---

**Query 2: What should students know about applying for Howard University housing?

Top returned chunks:

- **Result 1 — Source: Apply for Housing.txt, Chunk 0:** Explains that students use StarRez to submit and manage their housing application and that a $50 nonrefundable application fee must be paid before accessing the application.
- **Result 2 — Source: Apply for Housing.txt, Chunk 10:** Explains additional housing requirements, including paying the $300 non-refundable enrollment fee and completing all required steps.
- **Result 3 — Source: Housing.txt, Chunk 0:** Provides general Howard University housing information and resources for students.
- **Result 4 — Source: Find Off-Campus Housing.txt, Chunk 1:** Explains that independent off-campus properties are managed separately, while university-sponsored housing follows Howard's housing assignment process.

Relevance explanation:
The retrieval results were relevant because the highest-ranked chunks came directly from Howard University's housing application information. The first two results specifically explain important application requirements, including using StarRez, paying the $50 application fee, and completing required enrollment steps. The fourth result is less directly related to the application process, but it still provides useful context about Howard's housing options.

---

**Query 3: What is the difference between independent off-campus housing and university-sponsored housing?

Top returned chunks:
- **Result 1 — Source: Housing.txt, Chunk 2:** Discusses off-campus housing as an opportunity for students to exercise independence while still receiving support from the university.
- **Result 2 — Source: Find Off-Campus Housing.txt, Chunk 1:** Explains that independent off-campus properties are owned and managed separately, and students lease directly from the property owner or manager. University-sponsored housing follows Howard's housing assignment process.
- **Result 3 — Source: Find Off-Campus Housing.txt, Chunk 0:** Introduces the two housing paths and explains that properties listed through Howard's off-campus housing portal are independently owned and managed.
- **Result 4 — Source: 6 Tips for Finding Off-Campus Housing.txt, Chunk 1:** Provides general advice about selecting off-campus housing, including deciding whether to live alone or with roommates and considering living preferences.

Relevance explanation:
The retrieval results were relevant because Results 2 and 3 directly explain the difference between independent off-campus housing and university-sponsored housing. They show that independent housing involves leasing directly from a property owner or manager, while university-sponsored housing follows Howard's housing assignment process. Results 1 and 4 provide related information about off-campus living, but they are less directly focused on the difference between the two housing options.
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

## Grounded Generation

The system retrieves the most relevant housing chunks from ChromaDB and provides those chunks to the Groq language model as context. The prompt instructs the model to answer only using the retrieved information and not to make up information. If the retrieved context does not contain enough information to answer the question, the model is instructed to respond that it does not have enough information in the provided housing documents.

The generated response also includes the source files connected to the retrieved chunks so users can see where the information came from.

**System prompt grounding instruction:**  
The system prompt tells the model to answer the user's question using only the information provided in the retrieved context. It also instructs the model not to make up information. If the context does not contain enough information to answer the question, the model is instructed to say, "I don't have enough information in the provided housing documents to answer that question."

**How source attribution is surfaced in the response:**  
After the model generates an answer, the system displays a Sources section containing the names of the documents used in the retrieved context. Duplicate source names are removed so that each source is only listed once.
---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->


**Grounded response 1**

Query: What should students know about applying for Howard University housing?

Response: Students should complete all required steps for the housing application process, including paying the enrollment fee, paying the housing application fee, and submitting the housing application by the listed deadlines. If the required steps are not completed on time, access to on-campus housing could be jeopardized.

Source attribution:
- Apply for Housing.txt
- Housing.txt
- Find Off-Campus Housing.txt

---

**Grounded response 2**

Query: What should students consider when looking for off-campus housing?

Response: Students should think about several key factors when searching for off-campus housing:

1. **Whether to live alone or with roommates** – Decide if you want to "ride solo" or share an apartment.
2. **Living-style compatibility** – If you choose to live with others, make sure all parties are on the same page about preferences such as sleep schedules (early birds vs. night owls) and how often you like to entertain guests.
3. **Being a respectful member of the surrounding community** – Consider how your habits will affect neighbors and the broader community.
4. **Your independence and the support available** – Off-campus living offers independence while still allowing you to receive support from the university, such as through the Office of Off-Campus Housing.

If you need further guidance, you can contact the Office of Off-Campus Housing at offcampushousing@howard.edu.

Source attribution:
- 6 Tips for Finding Off-Campus Housing.txt
- Housing.txt
- Find Off-Campus Housing.txt

---

**Out-of-scope response**

Query: What is the best restaurant near Howard University?

Response: I don't have enough information in the provided housing documents to answer that question.

Source attribution:
- Help Picking Dorm.txt
- Resident hall recommendations .txt
- Transfer student looking for housing.txt
---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->
**Input fields:**  
The interface contains a text box labeled "Ask a housing question" where users can enter questions about Howard University housing or off-campus housing. Users submit their question by clicking the "Ask" button.

**Output format:**  
The interface displays the generated response in an "Answer" field and lists the retrieved document names in a separate "Sources" field. This allows the user to see both the answer and the documents that were used as context to generate it.

---

**Sample Interaction Transcript**

**User:** What should students consider when looking for off-campus housing?

**System:** Students should think about several key factors when searching for off-campus housing:

1. **Whether to live alone or with roommates** – Decide if you want to "ride solo" or share an apartment.
2. **Living-style compatibility** – If you choose to live with others, make sure all parties are on the same page about preferences such as sleep schedules (early birds vs. night owls) and how often you like to entertain guests.
3. **Being a respectful member of the surrounding community** – Consider how your habits will affect neighbors and the broader community.
4. **Your independence and the support available** – Off-campus living offers independence while still allowing you to receive support from the university, such as through the Office of Off-Campus Housing.

If you need further guidance, you can contact the Office of Off-Campus Housing at offcampushousing@howard.edu.

 **Sources:**
6 Tips for Finding Off-Campus Housing.txt
Housing.txt
Find Off-Campus Housing.txt

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

## Evaluation Report

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What should students consider when looking for off-campus housing? | Students should consider factors such as roommates, living preferences, budget, and responsibilities related to living off campus. | The system explained living arrangements, roommate compatibility, community respect, and provided the Office of Off-Campus Housing contact information. | Relevant | Accurate |
| 2 | What should students know about applying for Howard University housing? | Students should know how to access the housing application, required fees, and important application requirements. | The system explained that students use StarRez, must pay a $50 application fee, that the fee does not guarantee housing, and that required steps and deadlines must be completed. | Relevant | Accurate |
| 3 | What is the difference between independent off-campus housing and university-sponsored housing? | Independent off-campus housing is independently owned and managed, while university-sponsored housing follows Howard's housing assignment process. | The system correctly explained that independent properties are separately owned and managed while university-sponsored housing follows Howard's housing assignment process. | Relevant | Accurate |
| 4 | What should students consider when choosing a roommate? | Students should consider compatibility in living preferences, schedules, guests, budget, and other shared expectations. | The system discussed sleep schedules, entertaining habits, and budget considerations when choosing a roommate. | Relevant | Accurate |
| 5 | What is the best restaurant near Howard University? | The system should refuse to answer because restaurant recommendations are outside the scope of the housing documents. | The system stated that it did not have enough information in the provided housing documents to answer the question. | Off-target | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

**Question that failed:**  
What is the difference between independent off-campus housing and university-sponsored housing?

**What the system returned:**  
The final generated answer was accurate, but the retrieval ranking was not ideal. The first retrieved result was Housing.txt, Chunk 2, which discussed off-campus living and independence but did not directly explain the difference between independent off-campus housing and university-sponsored housing. The more directly relevant information from Find Off-Campus Housing.txt appeared as Results 2 and 3.

**Root cause (tied to a specific pipeline stage):**  
The weakness occurred during the retrieval stage. The all-MiniLM-L6-v2 embedding model matched the concepts of "off-campus housing" and "independence" in Housing.txt with the question, causing a more general chunk to rank above chunks that directly explained the two housing categories. This shows that semantic similarity does not always rank the most precise chunk first.

**What you would change to fix it:**  
I would experiment with a stronger embedding model, different chunk sizes, or retrieving more candidate chunks and reranking them before sending them to the language model. A reranking step could help prioritize chunks that directly address both independent off-campus housing and university-sponsored housing.

---

## Spec Reflection

**One way the spec helped you during implementation:**  
The planning specification gave me a clear structure for building the RAG system one stage at a time. It helped me organize the project into document collection, chunking, embeddings, retrieval, grounded generation, and evaluation instead of trying to build the entire system at once. The planned evaluation questions also gave me a consistent way to test whether the completed system was working as expected.

**One way your implementation diverged from the spec, and why:**  
My implementation changed slightly during the generation stage because the Groq models I originally attempted to use were not available to my API key. I checked which model was available through my Groq account and changed the generation model to `groq/compound`. This allowed me to continue using Groq while keeping the retrieval and grounding structure of my original plan.

---

## AI Usage

**Instance 1**

- **What I gave the AI:** I provided ChatGPT with my project requirements, my planned 500-character chunk size with 100-character overlap, and outputs from my ingestion and retrieval code. I asked for help implementing and troubleshooting the RAG pipeline.
- **What it produced:** ChatGPT provided code suggestions for connecting my document chunks, SentenceTransformer embeddings, ChromaDB retrieval, and Groq generation. It also helped explain errors that occurred while connecting the retrieval output to the generation code.
- **What I changed or overrode:** I tested the suggested code against my actual project and provided the real error messages when the suggested implementation did not match the structure of my ChromaDB retrieval results. The generation code was then adjusted to use the actual `documents` and `metadatas` returned by my retrieval function instead of changing my working retrieval implementation.

**Instance 2**

- **What I gave the AI:** I provided ChatGPT with the Groq API errors showing that the initially selected models were unavailable to my account, followed by the output showing the model available to my API key.
- **What it produced:** ChatGPT helped me troubleshoot the model-access problem and showed me how to check the models available through my Groq account. It then helped update the generation code to use the available `groq/compound` model and helped connect the working generation function to a Gradio interface.
- **What I changed or overrode:** Instead of continuing to try models that my account could not access, I tested the available models with my own API key and used the model returned by Groq. I also tested the completed system with housing questions and an out-of-scope restaurant question to verify that the answers remained grounded in my housing documents.

# Demo Video

Link: https://drive.google.com/file/d/1CzNVz8flmsJeK6JtgRPGP8zjhBGCUj8-/view?usp=sharing
