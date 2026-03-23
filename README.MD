This is a potential addition for the American Data’s volunteering system “https://www.american-data.com/”. 

# Volunteer & Research Matching System 

**Objective** To develop a dedicated volunteer matching application designed for the American Data ecosystem. This system goes beyond manual shift tracking by utilizing a multi-tiered matching engine to pair volunteers with clinical researchers, care coordinators, and long-term care residents based on skills, research interests, and compatibility.

## 1. System Architecture & Tech Stack Recommendations
To handle the dynamic interfaces and complex statistical weighting required, the architecture must be efficient and scalable.

**Backend & Matching Engine:** Python-based (utilizing frameworks like Flask) to handle data processing, statistical weighting, and NLP tasks.

**Frontend:** A responsive JavaScript framework to handle UI (scheduling, real-time feeds).

**Database:** A relational database to manage normalized profiles, with indexing to maintain efficient time complexity as the user base scales.

## 2. Multi-Tiered Profile Management
The system requires structured data from four distinct user types to facilitate intelligent matching.

### The Volunteer Profile
**Academic & Career Context:** Major (or high school), minor, year of study, and career goals (e.g., "Med School Prep," "Clinical Psychology," "Nursing").<br>
**Skill Matrix:** Technical skills (e.g., Python, R, data entry) and long-term care specific skills (e.g., mobility assistance, dementia communication).<br>
**Interest Keywords:** Self-defined semantic tags (e.g., "Alzheimer's research," "music therapy," "chess").<br>
**Availability:** Granular time slots with a toggle for "Recurring Weekly Availability."

### The Doctor/Researcher Profile
**Specialty:** (e.g., Cognitive science, Neurology).<br>
**Current Projects:** Descriptions of ongoing cognitive, dementia, or pharmacological research within the nursing home.<br>
**Required Skills:** Hard requirements (e.g., statistical analysis, bilingualism) and soft skills (e.g., clinical observation, patient empathy, reading, arts).

### The Care Coordinator Profile
**Facility Programs:** Group physical therapy, memory care wing support, mealtime assistance.<br>
**Shift Requirements:** Number of volunteers needed, required certifications (e.g., CPR, Safe Lifting).

### The Resident Companion Profile (Anonymized)
**Life History & Hobbies:** Former career, spoken languages, and personal interests.<br>
**Cognitive Profile:** Stage of dementia or specific companionship needs (e.g., "Needs reading assistance," "Enjoys outdoor walks").

## 3. The Multi-Layered Matching Engine (The "AI" Core)
The matching algorithm processes candidate pools through sequential filters and scoring matrices to generate a "Match Percentage."

**Layer 1: Constraint Filtering (Not implementated)**
Eliminates mathematically impossible matches based on schedule conflicts or missing mandatory compliance documents. (In my experience, some doctors give expections and some don't. In the end, I did not implement this because I think it should be up to the volunteer coordinators to decide.)

**Layer 2: NLP Semantic Matching**
Utilizes a lightweight Natural Language Processing (NLP) model to map the volunteer’s "Interest Keywords" and "Career Goals" against Researcher "Projects" or Resident "Life Histories." This ensures semantic hits even without exact phrasing (matching "neurodegeneration" with "dementia").

**Layer 3: The Weighted Scoring Matrix**
* **Research/Doctor Track:** Overlap in technical skills (40%), Research similarity (40%), Goal alignment (20%).
* **Care/Resident Track:** Keyword/Hobby overlap (50%), Relevant soft skills (30%), Language compatibility (20%).

**Layer 4: The "Consistency Multiplier"**
Specifically for the long-term care environment. Volunteers who commit to recurring, identical weekly shifts receive a heavy  boost in their match scores for memory care and resident companion roles, reducing resident anxiety through familiar faces.

## 4. User Experience (UX) & Workflows

### The Discovery & Recruitment Workflow
**Mutual Double Opt-In:** Volunteers first express interest. Then the volunteer coordinator will review the candidate profiles and click "Accept" to admit the profile in the system.

**Volunteer Dashboard:** Displays a feed of "Top Recommended Placements," styled cleanly like Linkedin. Each card displays the Researcher, Coordinator, or Program, the Match Score, and the reasoning.

**Coordinator/Researcher View:** Allows posting of "Openings." The system bypasses manual searching by instantly serving a ranked, sorted list of the top qualified volunteers.

### Ad-Hoc Replacement (Future Implementation)

**Rapid Replacement System:** If a volunteer cancels a shift, the system automatically identifies available, qualified candidates not currently scheduled. It notifies this replacement pool, allowing them to claim the shift on a first-come, first-served basis before requiring admin intervention.

## 5. Administration
**Manual Background Checks:** Volunteers cannot enter the active "Candidate Pool" until admins verify required background checks and health screenings. Also only admins can confirm matches after manually reviewing the requests.

**Attestation Generation: (Future Implementation)** Automated PDF/Word generation for volunteer hours, pulling database records, dates of service, and digital signatures for university or medical school applications.

## How to run the application
1. Install the dependencies: `pip install -r requirements.txt`
2. Initialize the database: `python seed.py`
3. Run the application: `python run.py`