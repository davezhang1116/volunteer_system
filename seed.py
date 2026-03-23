from app import app, db
from app.models import User, Volunteer, Doctor, CareCoordinator, Resident

def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create admin user
        admin = User(name='Admin', email='admin@a.com', role='admin')
        admin.set_password("123456")
        db.session.add(admin)
        db.session.commit() # Commit admin separately to ensure it's available if needed immediately

        # Create test users
        # Volunteers
        v1 = Volunteer(name='John Doe', email='john.doe@example.com', major='Computer Science', minor='Mathematics', year_of_study='Junior', career_goals='Software Engineer, AI Research', skills='Python, Java, C++, Data Entry', interest_keywords='AI, Machine Learning, Robotics, Elderly Care', availability='Mon 9-12, Wed 1-4', is_active=True, linked_status = None)
        v1.set_password("123456")
        v2 = Volunteer(name='Jane Smith', email='jane.smith@example.com', major='Biology', minor='Chemistry', year_of_study='Senior', career_goals='Medical Doctor, Clinical Research', skills='Lab work, Data analysis, First Aid, Patient Observation', interest_keywords='Genetics, Cancer research, Alzheimer\'s research, Patient interaction', availability='Tue 10-2, Thu 1-5 (Recurring)', is_active=True, linked_status = None)
        v2.set_password("123456")
        v3 = Volunteer(name='Alice Johnson', email='alice.j@example.com', major='Nursing', minor='Psychology', year_of_study='Sophomore', career_goals='Geriatric Nurse, Care Coordinator', skills='CPR, Basic Life Support, Empathy, Dementia Communication', interest_keywords='Memory care, Music therapy, Social engagement, Elderly companionship', availability='Fri 9-1, Sat 10-3', is_active=True, linked_status = None)
        v3.set_password("123456")
        v4 = Volunteer(name='Bob Williams', email='bob.w@example.com', major='Psychology', minor='Sociology', year_of_study='Graduate', career_goals='Clinical Psychologist, Researcher', skills='Statistical Analysis, Interviewing, Active Listening, Bilingual (Spanish)', interest_keywords='Cognitive decline, Mental health, Group therapy, Cross-cultural studies', availability='Mon 1-5, Wed 9-12 (Recurring)', is_active=True, linked_status = None)
        v4.set_password("123456")
        v5 = Volunteer(name='Charlie Brown', email='charlie.b@example.com', major='Data Science', minor='Statistics', year_of_study='Junior', career_goals='Data Analyst, Biostatistician', skills='R, Python, SQL, Data Visualization', interest_keywords='Epidemiology, Public Health, Health Informatics, Data privacy', availability='Tue 9-12, Thu 2-5', is_active=True, linked_status = None)
        v5.set_password("123456")
        v6 = Volunteer(name='Diana Prince', email='diana.p@example.com', major='Social Work', minor='Gerontology', year_of_study='Senior', career_goals='Social Worker, Advocate for Elderly', skills='Crisis Intervention, Communication, Resource Navigation, Mobility Assistance', interest_keywords='Elder abuse prevention, Community outreach, Palliative care, Family support', availability='Mon 10-2, Wed 10-2, Fri 10-2 (Recurring)', is_active=True, linked_status = None)
        v6.set_password("123456")
        
        # High School Volunteers (no experience)
        v7 = Volunteer(name='Sam Miller', email='sam.m@example.com', major='High School', minor='', year_of_study='Sophomore', career_goals='Undecided, explore healthcare', skills='Eager to learn, Basic computer skills, Good listener', interest_keywords='Helping others, Community service, Animals', availability='Weekends, Mon/Wed 3-5 PM', is_active=True, linked_status = None)
        v7.set_password("123456")
        v8 = Volunteer(name='Chloe Davis', email='chloe.d@example.com', major='High School', minor='', year_of_study='Junior', career_goals='Considering nursing or teaching', skills='Organized, Friendly, Quick learner', interest_keywords='Reading, Arts and crafts, Elderly companionship', availability='Tue/Thu 4-6 PM, Sat mornings', is_active=True, linked_status = None)
        v8.set_password("123456")
        v9 = Volunteer(name='Ethan White', email='ethan.w@example.com', major='High School', minor='', year_of_study='Freshman', career_goals='Explore science, volunteer experience', skills='Enthusiastic, Follows instructions well, Basic communication', interest_keywords='Science, Games, Storytelling', availability='Fri 3-5 PM, Sun afternoons', is_active=True, linked_status = None)
        v9.set_password("123456")

        v10 = Volunteer(name='Liam Taylor', email='liam.t@example.com', major='High School', minor='', year_of_study='Freshman', career_goals='Veterinarian or Doctor', skills='Energetic, Tech-savvy, Loves animals', interest_keywords='Pet therapy, Technology help, Reading', availability='Weekends 10-2', is_active=True, linked_status = None)
        v10.set_password("123456")
        v11 = Volunteer(name='Emma Wilson', email='emma.w@example.com', major='High School', minor='', year_of_study='Sophomore', career_goals='Nursing', skills='Organized, Punctual, Good with elderly family members', interest_keywords='Companionship, Arts and crafts, Baking', availability='Tue/Thu 4-6 PM', is_active=True, linked_status = None)
        v11.set_password("123456")
        v12 = Volunteer(name='Lucas Moore', email='lucas.m@example.com', major='High School', minor='', year_of_study='Junior', career_goals='Undecided, seeking community service hours', skills='Heavy lifting, Setting up events, Friendly', interest_keywords='Event planning, Outdoor walks, Board games', availability='Sat/Sun 1-5 PM', is_active=True, linked_status = None)
        v12.set_password("123456")
        v13 = Volunteer(name='Mia Anderson', email='mia.a@example.com', major='High School', minor='', year_of_study='Senior', career_goals='Pre-Med Track in College', skills='CPR Certified, Detail-oriented, Note-taking', interest_keywords='Shadowing, Administrative support, Health science', availability='Mon/Wed 3:30-5:30 PM', is_active=True, linked_status = None)
        v13.set_password("123456")
        v14 = Volunteer(name='Noah Thomas', email='noah.t@example.com', major='High School', minor='', year_of_study='Sophomore', career_goals='Social Worker', skills='Active listening, Patient, Bilingual (French)', interest_keywords='Talking with residents, Reading aloud', availability='Fri 4-7 PM', is_active=True, linked_status = None)
        v14.set_password("123456")
        v15 = Volunteer(name='Ava Jackson', email='ava.j@example.com', major='High School', minor='', year_of_study='Junior', career_goals='Physical Therapy', skills='Athletic, Enthusiastic, First Aid', interest_keywords='Mobility assistance, Exercise groups, Sports watching', availability='Wed/Fri 4-6 PM', is_active=True, linked_status = None)
        v15.set_password("123456")
        v16 = Volunteer(name='Elijah White', email='elijah.w@example.com', major='High School', minor='', year_of_study='Freshman', career_goals='Explore science fields', skills='Curious, Follows directions, Clean-up and prep', interest_keywords='Science experiments, Puzzles, History', availability='Sat 9-12 AM', is_active=True, linked_status = None)
        v16.set_password("123456")
        v17 = Volunteer(name='Isabella Harris', email='isabella.h@example.com', major='High School', minor='', year_of_study='Senior', career_goals='Healthcare Administration', skills='Microsoft Office, Scheduling, Cordial phone manners', interest_keywords='Front desk help, Organizing files, Welcoming guests', availability='Tue/Thu 3-6 PM', is_active=True, linked_status = None)
        v17.set_password("123456")
        v18 = Volunteer(name='Mason Martin', email='mason.m@example.com', major='High School', minor='', year_of_study='Sophomore', career_goals='Music Therapist', skills='Plays piano and guitar, Outgoing, Empathetic', interest_keywords='Music sessions, Sing-alongs, Memory care through music', availability='Sun 1-4 PM', is_active=True, linked_status = None)
        v18.set_password("123456")
        v19 = Volunteer(name='Sophia Thompson', email='sophia.t@example.com', major='High School', minor='', year_of_study='Junior', career_goals='Art Therapist', skills='Painting, Sculpting, Patient instruction', interest_keywords='Leading art classes, Creative expression, Decorating', availability='Sat 2-5 PM', is_active=True, linked_status = None)
        v19.set_password("123456")

        # --- Early University (Some Skills / Developing Focus) ---
        v20 = Volunteer(name='Logan Garcia', email='logan.g@example.com', major='Pre-Med', minor='Biology', year_of_study='Freshman', career_goals='Surgeon', skills='Basic Life Support, Academic research, Fast learner', interest_keywords='Clinical exposure, Patient transport, Anatomy', availability='Mon/Wed 8-11 AM', is_active=True, linked_status = None)
        v20.set_password("123456")
        v21 = Volunteer(name='Amelia Martinez', email='amelia.m@example.com', major='Psychology', minor='Sociology', year_of_study='Sophomore', career_goals='Clinical Therapist', skills='Crisis de-escalation training, Empathy, Interviewing', interest_keywords='Mental health awareness, Group discussions, Memory mapping', availability='Tue/Thu 1-4 PM', is_active=True, linked_status = None)
        v21.set_password("123456")
        v22 = Volunteer(name='James Robinson', email='james.r@example.com', major='Kinesiology', minor='Nutrition', year_of_study='Sophomore', career_goals='Occupational Therapist', skills='Safe lifting techniques, Biomechanics knowledge, Meal prep assistance', interest_keywords='Rehabilitation, Motor skills games, Nutrition tracking', availability='Fri 8-12 AM', is_active=True, linked_status = None)
        v22.set_password("123456")
        v23 = Volunteer(name='Harper Clark', email='harper.c@example.com', major='Public Health', minor='Policy', year_of_study='Freshman', career_goals='Epidemiologist', skills='Data entry, Survey administration, Spanish (Fluent)', interest_keywords='Health education, Infection control protocols, Community outreach', availability='Wed 1-5 PM', is_active=True, linked_status = None)
        v23.set_password("123456")
        v24 = Volunteer(name='Benjamin Rodriguez', email='benjamin.r@example.com', major='Computer Science', minor='', year_of_study='Sophomore', career_goals='Health Tech Developer', skills='Java, HTML/CSS, IT troubleshooting', interest_keywords='Updating facility tech, Teaching elders to use tablets, Database help', availability='Sat 10-3 PM', is_active=True, linked_status = None)
        v24.set_password("123456")
        v25 = Volunteer(name='Evelyn Lewis', email='evelyn.l@example.com', major='Nursing', minor='Spanish', year_of_study='Sophomore', career_goals='ER Nurse', skills='Vitals measurement (academic), First Aid, High energy', interest_keywords='Triage shadowing, Rounding with nurses, Acute care', availability='Thu/Fri 2-6 PM', is_active=True, linked_status = None   )
        v25.set_password("123456")
        v26 = Volunteer(name='William Lee', email='william.l@example.com', major='Communications', minor='English', year_of_study='Freshman', career_goals='Hospital Public Relations', skills='Writing, Social Media management, Photography', interest_keywords='Writing resident biographies, Newsletter creation, Event photography', availability='Mon/Tue 10-1 PM', is_active=True, linked_status = None)
        v26.set_password("123456")
        v27 = Volunteer(name='Abigail Walker', email='abigail.w@example.com', major='Sociology', minor='Gerontology', year_of_study='Sophomore', career_goals='Gerontologist', skills='Literature review, Qualitative observation, Respectful demeanor', interest_keywords='Aging populations, Social isolation studies, Oral histories', availability='Wed/Fri 9-12 AM', is_active=True, linked_status = None)
        v27.set_password("123456")
        v28 = Volunteer(name='Alexander Hall', email='alexander.h@example.com', major='Biochemistry', minor='', year_of_study='Freshman', career_goals='Pharmacist', skills='Lab safety, Precision, Math', interest_keywords='Medication schedule shadowing, Pharmacy organization, Chemistry', availability='Sun 9-1 PM', is_active=True, linked_status = None)
        v28.set_password("123456")
        v29 = Volunteer(name='Elizabeth Allen', email='elizabeth.a@example.com', major='Education', minor='Special Ed', year_of_study='Sophomore', career_goals='Adult Educator', skills='Lesson planning, Patience, Adapting to learning speeds', interest_keywords='Cognitive exercises, Teaching new skills, Technology classes', availability='Tue/Thu 9-12 AM', is_active=True, linked_status = None)
        v29.set_password("123456")

        # --- Upper-Level University (Advanced Skills / Practical Focus) ---
        v30 = Volunteer(name='Michael Young', email='michael.y@example.com', major='Neuroscience', minor='Computer Science', year_of_study='Junior', career_goals='Neurologist, AI in Medicine', skills='EEG setup (academic), Python, Data Visualization', interest_keywords='Brain mapping, Cognitive decline research, Tech interventions', availability='Mon/Wed 2-6 PM', is_active=True, linked_status = None)
        v30.set_password("123456")
        v31 = Volunteer(name='Mila Hernandez', email='mila.h@example.com', major='Nursing', minor='Gerontology', year_of_study='Senior', career_goals='Nurse Practitioner (Geriatrics)', skills='Phlebotomy, Patient charting, Wound care knowledge', interest_keywords='Direct patient care, Medication administration observation, Palliative care', availability='Fri/Sat 7-12 AM', is_active=True, linked_status = None)
        v31.set_password("123456")
        v32 = Volunteer(name='Daniel King', email='daniel.k@example.com', major='Biomedical Engineering', minor='Mathematics', year_of_study='Junior', career_goals='Medical Device Design', skills='CAD, Prototyping, Ergonomics', interest_keywords='Wheelchair calibration, Customizing assistive devices, Mobility tech', availability='Tue/Thu 1-5 PM', is_active=True, linked_status = None)
        v32.set_password("123456")
        v33 = Volunteer(name='Avery Wright', email='avery.w@example.com', major='Nutrition', minor='Chemistry', year_of_study='Senior', career_goals='Registered Dietitian', skills='Dietary assessment, Meal planning, Caloric tracking', interest_keywords='Diabetic diets, Dysphagia nutrition, Cooking demonstrations', availability='Mon/Fri 10-2 PM', is_active=True, linked_status = None)
        v33.set_password("123456")
        v34 = Volunteer(name='Henry Lopez', email='henry.l@example.com', major='Social Work', minor='Public Policy', year_of_study='Junior', career_goals='Medical Social Worker', skills='Case management theory, Resource mapping, Conflict resolution', interest_keywords='Family counseling, Insurance navigation, Discharge planning', availability='Wed 9-5 PM', is_active=True, linked_status = None)
        v34.set_password("123456")
        v35 = Volunteer(name='Sofia Hill', email='sofia.h@example.com', major='Speech-Language Pathology', minor='Linguistics', year_of_study='Senior', career_goals='Speech Therapist', skills='Phonetics, Swallowing assessment knowledge, Sign Language (ASL)', interest_keywords='Aphasia support, Communication boards, Vocal exercises', availability='Tue/Thu 9-1 PM', is_active=True, linked_status = None)
        v35.set_password("123456")
        v36 = Volunteer(name='Jackson Scott', email='jackson.s@example.com', major='Health Informatics', minor='Business', year_of_study='Junior', career_goals='Hospital Administrator', skills='EHR/EMR systems, HIPAA compliance training, SQL', interest_keywords='Records digitization, Workflow optimization, Data privacy', availability='Fri 1-5 PM', is_active=True, linked_status = None)
        v36.set_password("123456")
        v37 = Volunteer(name='Chloe Green', email='chloe.g@example.com', major='Pre-Law', minor='Bioethics', year_of_study='Senior', career_goals='Healthcare Attorney', skills='Policy analysis, Debate, Contract review', interest_keywords='Patient rights, Advanced directives, Medical ethics discussions', availability='Mon 1-4, Thu 1-4 PM', is_active=True, linked_status = None)
        v37.set_password("123456")
        v38 = Volunteer(name='Sebastian Adams', email='sebastian.a@example.com', major='Physical Therapy', minor='Anatomy', year_of_study='Senior', career_goals='Geriatric PT', skills='Gait analysis, Range of motion testing, Massage', interest_keywords='Fall prevention, Post-op rehab, Arthritis management', availability='Sat/Sun 8-12 AM', is_active=True, linked_status = None)
        v38.set_password("123456")
        v39 = Volunteer(name='Lily Baker', email='lily.b@example.com', major='Pharmacology', minor='Biology', year_of_study='Junior', career_goals='Clinical Researcher', skills='Clinical trial protocols, Pharmacokinetics, Lab reporting', interest_keywords='Drug interaction studies, Medication efficacy tracking, Research assistance', availability='Wed/Fri 2-5 PM', is_active=True, linked_status = None)
        v39.set_password("123456")

        # --- Graduate / Research Level (Highly Specialized / Advanced Experience) ---
        v40 = Volunteer(name='Carter Gonzalez', email='carter.g@example.com', major='Biostatistics', minor='', year_of_study='Graduate', career_goals='Lead Biostatistician', skills='R, SAS, Survival Analysis, Longitudinal Data', interest_keywords='Clinical trial data, Mortality rate studies, Epidemiology', availability='Tue 9-5 PM', is_active=True, linked_status = None)
        v40.set_password("123456")
        v41 = Volunteer(name='Grace Nelson', email='grace.n@example.com', major='Clinical Psychology', minor='', year_of_study='Graduate', career_goals='Neuropsychologist', skills='Cognitive testing (MoCA, MMSE), Diagnostic interviewing, CBT', interest_keywords='Dementia staging, Depression in elderly, Caregiver burden', availability='Mon/Wed 10-3 PM', is_active=True, linked_status = None)
        v41.set_password("123456")
        v42 = Volunteer(name='Wyatt Carter', email='wyatt.c@example.com', major='Medical Physics', minor='', year_of_study='Graduate', career_goals='Oncology Physicist', skills='Radiation protocols, Imaging software, Advanced Mathematics', interest_keywords='Radiology shadowing, MRI/CT research, Cancer treatment', availability='Thu/Fri 1-5 PM', is_active=True, linked_status = None)
        v42.set_password("123456")
        v43 = Volunteer(name='Victoria Mitchell', email='victoria.m@example.com', major='Public Health (MPH)', minor='', year_of_study='Graduate', career_goals='Public Health Director', skills='Program evaluation, Grant writing, Epidemiology', interest_keywords='Facility outbreak protocols, Community health grants, Policy reform', availability='Mon/Fri 9-1 PM', is_active=True, linked_status = None)
        v43.set_password("123456")
        v44 = Volunteer(name='Jayden Perez', email='jayden.p@example.com', major='Genetics', minor='', year_of_study='Graduate', career_goals='Genetic Counselor', skills='Pedigree analysis, DNA sequencing data, Compassionate communication', interest_keywords='Hereditary diseases, Genetic predisposition to Alzheimer\'s, Patient education', availability='Wed 10-4 PM', is_active=True, linked_status = None)
        v44.set_password("123456")
        v45 = Volunteer(name='Zoe Roberts', email='zoe.r@example.com', major='Nursing (DNP)', minor='', year_of_study='Graduate', career_goals='Chief Nursing Officer', skills='Advanced physical assessment, Healthcare leadership, Quality improvement', interest_keywords='Nursing staff training, Clinical protocol design, Advanced care', availability='Weekends 7-3 PM', is_active=True, linked_status = None)
        v45.set_password("123456")
        v46 = Volunteer(name='Luke Turner', email='luke.t@example.com', major='Occupational Therapy (OTD)', minor='', year_of_study='Graduate', career_goals='OT Clinic Director', skills='Environmental modification, ADL training, Neuro-rehab', interest_keywords='Home safety evaluations, Adaptive equipment fitting, Stroke recovery', availability='Tue/Thu 8-12 AM', is_active=True, linked_status = None)
        v46.set_password("123456")
        v47 = Volunteer(name='Penelope Phillips', email='penelope.p@example.com', major='Gerontology (PhD)', minor='', year_of_study='Graduate', career_goals='University Professor, Lead Researcher', skills='Qualitative coding, Publication writing, Ethics board (IRB) submissions', interest_keywords='Aging theories, Quality of life research, Academic publishing', availability='Flexible / Remote Data Work', is_active=True, linked_status = None)
        v47.set_password("123456")
        v48 = Volunteer(name='Levi Campbell', email='levi.c@example.com', major='Artificial Intelligence', minor='', year_of_study='Graduate', career_goals='Machine Learning Engineer (Healthcare)', skills='PyTorch, Deep Learning, Predictive Modeling, NLP', interest_keywords='Predicting patient falls via data, Automating clinical notes, AI diagnostics', availability='Mon/Wed 4-8 PM', is_active=True, linked_status = None)
        v48.set_password("123456")
        v49 = Volunteer(name='Layla Parker', email='layla.p@example.com', major='Bioethics (MA)', minor='', year_of_study='Graduate', career_goals='Hospital Ethics Committee Lead', skills='Moral philosophy, End-of-life care ethics, Case consultation', interest_keywords='DNR discussions, Patient autonomy, Resource allocation ethics', availability='Thu/Fri 10-2 PM', is_active=True, linked_status = None)
        v49.set_password("123456")


        # Doctors
        d1 = Doctor(name='Dr. Emily Brown', email='dr.brown@example.com', specialty='Geriatric Medicine', current_projects='Longitudinal study on cognitive decline in elderly, Impact of nutrition on aging', required_skills='Statistical Analysis, Clinical Observation, Research Design', is_active=True, linked_status = None)
        d1.set_password("123456")
        d2 = Doctor(name='Dr. Michael Green', email='dr.green@example.com', specialty='Neurology', current_projects='Alzheimer\'s disease research, Pharmacological interventions for dementia, Neuroimaging studies', required_skills='Python, Machine Learning, Data Interpretation, Patient Empathy', is_active=True, linked_status = None)
        d2.set_password("123456")
        d3 = Doctor(name='Dr. Sarah Lee', email='dr.lee@example.com', specialty='Psychiatry', current_projects='Mental health in long-term care residents, Impact of social isolation on mood', required_skills='Counseling, Active Listening, Bilingual (Mandarin)', is_active=True, linked_status = None)
        d3.set_password("123456")
        d4 = Doctor(name='Dr. David Chen', email='dr.chen@example.com', specialty='Physical Therapy', current_projects='Rehabilitation protocols for stroke patients, Mobility improvement in elderly', required_skills='Anatomy Knowledge, Patient Motivation, Exercise Prescription', is_active=True, linked_status = None)
        d4.set_password("123456")
# --- Cognitive & Neurological Research ---
        d5 = Doctor(name='Dr. Robert Vance', email='dr.vance@example.com', specialty='Cognitive Research', current_projects='Working memory training in early dementia, Virtual reality spatial navigation', required_skills='Python, R, Cognitive Assessment Tools', is_active=True, linked_status = None)
        d5.set_password("123456")
        d6 = Doctor(name='Dr. Aisha Khan', email='dr.khan@example.com', specialty='Cognitive Research', current_projects='Bilingualism and cognitive reserve, Sleep quality and memory consolidation', required_skills='EEG operation, Statistical Modeling, Fluent in Arabic', is_active=True, linked_status = None)
        d6.set_password("123456")
        d24 = Doctor(name='Dr. Olivia Taylor', email='dr.taylor@example.com', specialty='Cognitive Psychology', current_projects='Reminiscence therapy efficacy, Caregiver behavioral interventions', required_skills='Psychological Testing, Group Therapy Facilitation, Active Listening', is_active=True, linked_status = None)
        d24.set_password("123456")
        d18 = Doctor(name='Dr. Rachel Green', email='dr.rgreen@example.com', specialty='Neurology', current_projects='Parkinson\'s disease gait freezing, Lewy body dementia diagnostics', required_skills='Neurological Examination, Clinical Trial Management, Empathy', is_active=True, linked_status = None)
        d18.set_password("123456")

        # --- Dentistry & Oral Health ---
        d7 = Doctor(name='Dr. Marcus Webb', email='dr.webb@example.com', specialty='Geriatric Dentistry', current_projects='Impact of oral health on systemic disease in elderly, Dementia-friendly dental practices', required_skills='Patience, Dental Surgery, Sedation Dentistry', is_active=True, linked_status = None)
        d7.set_password("123456")
        d8 = Doctor(name='Dr. Linda Choi', email='dr.choi@example.com', specialty='Prosthodontics (Dentistry)', current_projects='3D printed dentures, Nutritional outcomes post-restoration', required_skills='CAD/CAM, Material Science, Fine Motor Skills', is_active=True, linked_status = None)
        d8.set_password("123456")

        # --- Cardiology ---
        d9 = Doctor(name='Dr. Omar Patel', email='dr.patel@example.com', specialty='Cardiology', current_projects='Heart failure management in octogenarians, Wearable ECG monitoring', required_skills='Echocardiography, Data Analysis, Patient Education', is_active=True, linked_status = None)
        d9.set_password("123456")
        d10 = Doctor(name='Dr. Elena Rostova', email='dr.rostova@example.com', specialty='Cardiology', current_projects='Hypertension and cognitive decline correlation, Post-stroke cardiac care', required_skills='Clinical Pharmacology, Russian (Fluent), Emergency Response', is_active=True, linked_status = None)
        d10.set_password("123456")

        # --- Palliative & End-of-Life Care ---
        d15 = Doctor(name='Dr. Thomas Becker', email='dr.becker@example.com', specialty='Palliative Care', current_projects='Advanced directive communication effectiveness, Non-pharmacological pain management', required_skills='Empathetic Communication, Bioethics, Family Counseling', is_active=True, linked_status = None)
        d15.set_password("123456")
        d16 = Doctor(name='Dr. Sarah Jenkins', email='dr.jenkins@example.com', specialty='Palliative Care', current_projects='Music therapy in end-of-life care, Caregiver bereavement support', required_skills='Active Listening, Pain Management, Crisis Intervention', is_active=True, linked_status = None)
        d16.set_password("123456")

        # --- Specialized Geriatric Care ---
        d11 = Doctor(name='Dr. James Sullivan', email='dr.sullivan@example.com', specialty='Podiatry', current_projects='Diabetic neuropathy ulcer prevention, Fall risk reduction via footwear modification', required_skills='Wound Care, Biomechanics, Patient Empathy', is_active=True, linked_status = None)
        d11.set_password("123456")
        d12 = Doctor(name='Dr. Mei Lin', email='dr.mlin@example.com', specialty='Audiology', current_projects='Hearing loss and social isolation links, Cochlear implant outcomes in seniors', required_skills='Audiometry, Sign Language (ASL), Technical Troubleshooting', is_active=True, linked_status = None)
        d12.set_password("123456")
        d13 = Doctor(name='Dr. Samuel Clarke', email='dr.clarke@example.com', specialty='Optometry', current_projects='Macular degeneration progression tracking, Low-vision aids training', required_skills='Optical Coherence Tomography, Patience, Detail-Oriented', is_active=True, linked_status = None)
        d13.set_password("123456")
        d14 = Doctor(name='Dr. Anita Desai', email='dr.desai@example.com', specialty='Rheumatology', current_projects='Osteoarthritis pain management protocols, Autoimmune markers in aging', required_skills='Joint Injection Techniques, Immunology, Clinical Observation', is_active=True, linked_status = None)
        d14.set_password("123456")
        d17 = Doctor(name='Dr. Carlos Mendez', email='dr.mendez@example.com', specialty='Psychiatry', current_projects='Late-life depression interventions, Pharmacogenomics of antidepressants', required_skills='Psychiatric Evaluation, Spanish (Fluent), Empathy', is_active=True, linked_status = None)
        d17.set_password("123456")
        d21 = Doctor(name='Dr. Gregory Barnes', email='dr.barnes@example.com', specialty='Geriatric Medicine', current_projects='Polypharmacy reduction, Frailty index validation', required_skills='Internal Medicine, Pharmacology, Comprehensive Geriatric Assessment', is_active=True, linked_status = None)
        d21.set_password("123456")
        d22 = Doctor(name='Dr. Evelyn Wu', email='dr.wu@example.com', specialty='Geriatric Oncology', current_projects='Tolerability of low-dose chemo in elderly, Quality of life vs survival time', required_skills='Oncological Protocols, Compassionate Delivery, Statistical Analysis', is_active=True, linked_status = None)
        d22.set_password("123456")
        d23 = Doctor(name='Dr. William Foster', email='dr.foster@example.com', specialty='Orthopedics', current_projects='Hip replacement recovery timelines, Osteoporosis fracture prevention', required_skills='Surgical Consultation, Rehabilitation Planning, X-Ray Interpretation', is_active=True, linked_status = None)
        d23.set_password("123456")

        # --- Allied Health & Therapy ---
        d19 = Doctor(name='Dr. David Kim', email='dr.dkim@example.com', specialty='Occupational Therapy', current_projects='Adaptive equipment adoption rates, Environmental modifications for severe dementia', required_skills='Ergonomic Assessment, Creative Problem Solving, Patience', is_active=True, linked_status = None)
        d19.set_password("123456")
        d20 = Doctor(name='Dr. Fatima Al-Sayed', email='dr.alsayed@example.com', specialty='Speech-Language Pathology', current_projects='Post-stroke aphasia recovery, Dysphagia diet compliance', required_skills='Swallowing Assessment, Linguistic Analysis, Arabic (Fluent)', is_active=True, linked_status = None)
        d20.set_password("123456")


        # Care Coordinators
        cc1 = CareCoordinator(name='Coordinator Maria', email='cc1@example.com', facility_programs='Group physical therapy, Memory care wing support, Mealtime assistance', shift_requirements='3 volunteers, CPR certified, Safe Lifting', is_active=True, linked_status = None)
        cc1.set_password("123456")
        cc2 = CareCoordinator(name='Coordinator Alex', email='cc2@example.com', facility_programs='Art therapy sessions, Outdoor walking groups, Reading circles', shift_requirements='2 volunteers, Dementia communication skills, First Aid', is_active=True, linked_status = None)
        cc2.set_password("123456")
        cc3 = CareCoordinator(name='Coordinator Jessica', email='cc3@example.com', facility_programs='Music appreciation, Storytelling hours, Card game tournaments', shift_requirements='1 volunteer, Patient engagement skills, Empathy', is_active=True, linked_status = None)
        cc3.set_password("123456")

        # Residents
        r1 = Resident(name='Resident A', life_history='Former high school history teacher, lived in Europe for 10 years', hobbies='Reading, Chess, Documentaries', cognitive_profile='Early stage dementia, enjoys conversation and historical topics', is_active=True, linked_status = None)
        r2 = Resident(name='Resident B', life_history='Retired jazz musician, played saxophone in a band for 40 years', hobbies='Music, Singing, Listening to old records', cognitive_profile='Needs reading assistance, enjoys classical and jazz music', is_active=True, linked_status = None)
        r3 = Resident(name='Resident C', life_history='WWII veteran, worked as an engineer for NASA', hobbies='Gardening, Building model airplanes, Watching nature shows', cognitive_profile='Enjoys outdoor walks, good verbal skills, sometimes confused about dates', is_active=True, linked_status = None)
        r4 = Resident(name='Resident D', life_history='Homemaker and avid gardener, raised three children', hobbies='Knitting, Gardening, Cooking shows', cognitive_profile='Advanced dementia, responds well to gentle touch and music', is_active=True, linked_status = None)
        r5 = Resident(name='Resident E', life_history='Artist and painter, taught art classes for 20 years', hobbies='Painting, Drawing, Visiting art museums', cognitive_profile='Mild cognitive impairment, enjoys creative activities and discussing art', is_active=True, linked_status = None)
        r6 = Resident(name='Resident F', life_history='Small business owner, ran a local bookstore for 30 years', hobbies='Reading, Card games, Discussing current events', cognitive_profile='Alert and oriented, enjoys intellectual stimulation and companionship', is_active=True, linked_status = None)
        r7 = Resident(name='Resident G', life_history='Former nurse, passionate about helping others', hobbies='Bird watching, Puzzles, Listening to audiobooks', cognitive_profile='Moderate dementia, benefits from structured activities and calm environments', is_active=True, linked_status = None)


        r8 = Resident(name='Resident H', life_history='Retired structural engineer, helped design several local bridges.', hobbies='Chess, Sudoku, Discussing architecture', cognitive_profile='Completely sharp, sharp wit, uses a wheelchair for mobility.', is_active=True, linked_status = None)
        r9 = Resident(name='Resident I', life_history='Former professional ballerina and dance instructor.', hobbies='Classical music, Watching ballet performances, Gentle stretching', cognitive_profile='Alert, very social, enjoys mentoring younger volunteers.', is_active=True, linked_status = None)
        r10 = Resident(name='Resident J', life_history='First-generation immigrant from Italy, owned a family bakery for 45 years.', hobbies='Baking (when assisted), Sharing recipes, Card games', cognitive_profile='Alert, occasionally struggles with English word retrieval, fluent in Italian.', is_active=True, linked_status = None)
        r11 = Resident(name='Resident K', life_history='Veteran of the Navy, traveled to over 50 countries.', hobbies='Reading historical non-fiction, Geography trivia, Model ships', cognitive_profile='Mild age-related memory loss, highly engaging storyteller.', is_active=True, linked_status = None)
        r12 = Resident(name='Resident L', life_history='Former defense attorney and local judge.', hobbies='Debate, Current events, Crossword puzzles', cognitive_profile='Very sharp, enjoys intellectual challenges and debating the news.', is_active=True, linked_status = None)
        r13 = Resident(name='Resident M', life_history='Career librarian, fostered dozens of rescue dogs over her life.', hobbies='Reading clubs, Pet therapy days, Knitting', cognitive_profile='Alert, quiet and introverted, very empathetic.', is_active=True, linked_status = None)

        # --- Mild Cognitive Impairment (MCI) / Early-Stage Dementia ---
        r14 = Resident(name='Resident N', life_history='High school science teacher and amateur astronomer.', hobbies='Stargazing, Science documentaries, Trivia', cognitive_profile='Early-stage dementia, repeats questions occasionally but retains deep scientific knowledge.', is_active=True, linked_status = None)
        r15 = Resident(name='Resident O', life_history='Worked on the automotive assembly line, proud union representative.', hobbies='Watching baseball, Tinkering with small parts, Checkers', cognitive_profile='MCI, gets frustrated when he forgets names, responds well to humor.', is_active=True, linked_status = None)
        r16 = Resident(name='Resident P', life_history='Stay-at-home father, raised four children, avid community volunteer.', hobbies='Gardening, Baking, Scrapbooking', cognitive_profile='Mild short-term memory loss, very nurturing, enjoys helping staff with small tasks.', is_active=True, linked_status = None)
        r17 = Resident(name='Resident Q', life_history='Fashion buyer who lived in New York and Paris.', hobbies='Looking at fashion magazines, Watercolor painting, Getting dressed up', cognitive_profile='Early Alzheimer\'s, forgets recent events but remembers 1970s fashion vividly.', is_active=True, linked_status = None)
        r18 = Resident(name='Resident R', life_history='Commercial airline pilot for 30 years.', hobbies='Flight simulators, Watching weather patterns, Travel logs', cognitive_profile='MCI, struggles with dates and times, loves talking about airplanes.', is_active=True, linked_status = None)
        r19 = Resident(name='Resident S', life_history='Professional seamstress and tailor.', hobbies='Sewing, Mending clothes, Listening to podcasts', cognitive_profile='Early-stage vascular dementia, retains excellent fine motor skills and muscle memory.', is_active=True, linked_status = None)
        r20 = Resident(name='Resident T', life_history='Journalist and local newspaper editor.', hobbies='Writing in a journal, Typing on an old typewriter, Reading the morning paper', cognitive_profile='MCI, writes beautiful notes but sometimes loses her train of thought mid-conversation.', is_active=True, linked_status = None)

        # --- Moderate Dementia / Memory Care Required ---
        r21 = Resident(name='Resident U', life_history='Worked as a postal carrier, walked the same route for 25 years.', hobbies='Walking in the courtyard, Sorting mail/papers, Listening to the radio', cognitive_profile='Moderate dementia, pacing behavior, easily redirected by giving him "mail" to sort.', is_active=True, linked_status = None)
        r22 = Resident(name='Resident V', life_history='Classical pianist, taught lessons out of her home.', hobbies='Playing the piano (by ear), Listening to Chopin, Hand massages', cognitive_profile='Moderate Alzheimer\'s, mostly non-verbal but can play complex piano pieces beautifully.', is_active=True, linked_status = None)
        r23 = Resident(name='Resident W', life_history='Farmer who grew corn and soybeans in the Midwest.', hobbies='Being outdoors, Looking at seed catalogs, Animal therapy', cognitive_profile='Moderate dementia, frequently asks about the harvest, enjoys outdoor sensory activities.', is_active=True, linked_status = None)
        r24 = Resident(name='Resident X', life_history='Former pediatric nurse, delivered over 100 babies.', hobbies='Holding baby dolls, Folding baby clothes, Soft lullabies', cognitive_profile='Moderate dementia, believes she is still working at the hospital, very gentle.', is_active=True, linked_status = None)
        r25 = Resident(name='Resident Y', life_history='Graphic designer and comic book enthusiast.', hobbies='Doodling, Looking at colorful illustrations, Watching cartoons', cognitive_profile='Moderate cognitive decline, responds best to highly visual stimuli and bright colors.', is_active=True, linked_status = None)
        r26 = Resident(name='Resident Z', life_history='Immigrated from Mexico, worked as a seamstress to put kids through college.', hobbies='Listening to Mariachi music, Praying the rosary, Family visits', cognitive_profile='Moderate dementia, has reverted entirely to speaking Spanish, easily soothed by familiar music.', is_active=True, linked_status = None)

        # --- Advanced Dementia / Late-Stage Care ---
        r27 = Resident(name='Resident AA', life_history='Corporate accountant, known for being meticulous and organized.', hobbies='Stacking papers, Organizing blocks, Classical music', cognitive_profile='Advanced dementia, limited verbal communication, comforted by repetitive, organized tasks.', is_active=True, linked_status = None)
        r28 = Resident(name='Resident BB', life_history='Career military officer, served in the Army for 30 years.', hobbies='Polishing shoes, Folding flags, Patriotic music', cognitive_profile='Advanced dementia, exhibits sundowning, responds to structured routines and respectful tones.', is_active=True, linked_status = None)
        r29 = Resident(name='Resident CC', life_history='Homemaker who loved hosting large dinner parties.', hobbies='Setting the table, Folding napkins, Smelling spices', cognitive_profile='Advanced Alzheimer\'s, non-verbal, interacts with the world purely through sensory experiences.', is_active=True, linked_status = None)
        r30 = Resident(name='Resident DD', life_history='Former Broadway stagehand and lighting technician.', hobbies='Watching musicals, Handling cables/ropes, Tap dancing music', cognitive_profile='Advanced dementia, frequently restless, enjoys having items to hold and manipulate.', is_active=True, linked_status = None)

        # --- Specialized Cases (Post-Stroke, Neurological) ---
        r31 = Resident(name='Resident EE', life_history='University professor of philosophy.', hobbies='Listening to audiobooks, Sitting in the garden', cognitive_profile='Severe expressive aphasia post-stroke. Cognitively intact but cannot speak. Uses a picture board.', is_active=True, linked_status = None)
        r32 = Resident(name='Resident FF', life_history='Stand-up comedian and radio host.', hobbies='Watching comedy specials, Making people laugh', cognitive_profile='Frontotemporal dementia (FTD), lacks a filter, makes inappropriate but harmless jokes.', is_active=True, linked_status = None)
        r33 = Resident(name='Resident GG', life_history='Park ranger, spent life protecting national forests.', hobbies='Nature documentaries, Touching pinecones/leaves, Birdsong audio', cognitive_profile='Advanced Parkinson\'s disease dementia, experiences hallucinations, calmed by nature sounds.', is_active=True, linked_status = None)
        r34 = Resident(name='Resident HH', life_history='Professional chef in a high-end restaurant.', hobbies='Watching cooking shows, Smelling essential oils, Tasting pureed sweets', cognitive_profile='Lewy Body dementia, fluctuates between highly alert and deeply confused.', is_active=True, linked_status = None)
        r35 = Resident(name='Resident II', life_history='Kindergarten teacher for 40 years.', hobbies='Coloring books, Singing nursery rhymes, Petting animals', cognitive_profile='Advanced Alzheimer\'s, very sweet disposition, responds well to childlike play and bright colors.', is_active=True, linked_status = None)
        r36 = Resident(name='Resident JJ', life_history='Long-haul truck driver.', hobbies='Looking at maps, Watching traffic from the window, Country music', cognitive_profile='Moderate vascular dementia, believes he needs to "get back on the road," requires gentle redirection.', is_active=True, linked_status = None)
        r37 = Resident(name='Resident KK', life_history='Opera singer who performed internationally.', hobbies='Singing, Listening to opera, Dressing in fine fabrics', cognitive_profile='Moderate dementia, struggles with conversation but can sing perfectly in Italian and German.', is_active=True, linked_status = None)
        db.session.add_all([
            # Volunteers (v1 - v49)
            v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,
            v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38,
            v39, v40, v41, v42, v43, v44, v45, v46, v47, v48, v49, 
            
            # Doctors (d1 - d24)
            d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24,
            
            # Care Coordinators
            cc1, cc2, cc3, 
            
            # Residents (r1 - r37)
            r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, 
            r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, r31, r32, r33, r34, r35, r36, r37
        ])
        db.session.commit()
        print("Database seeded successfully with diverse data!")

if __name__ == '__main__':
    seed()
