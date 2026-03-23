from wordllama import WordLlama

class Matcher:
    def __init__(self, volunteers, doctors, care_coordinators, residents):
        self.volunteers = volunteers
        self.doctors = doctors
        self.care_coordinators = care_coordinators
        self.residents = residents
        # Load the default WordLlama model (this can later be cached at the app level to save time)
        self.wl = WordLlama.load()

    def match(self):
        matches = {
            'doctor_matches': [],
            'resident_matches': [],
            'care_coordinator_matches': []
        }
        for volunteer in self.volunteers:
            for doctor in self.doctors:
                score = self._calculate_doctor_match_score(volunteer, doctor)
                matches['doctor_matches'].append({
                    'volunteer': volunteer.name,
                    'volunteer_id': volunteer.id,
                    'doctor': doctor.name,
                    'doctor_id': doctor.id,
                    'score': score
                })
            for resident in self.residents:
                score = self._calculate_resident_match_score(volunteer, resident)
                matches['resident_matches'].append({
                    'volunteer': volunteer.name,
                    'volunteer_id': volunteer.id,
                    'resident': resident.name,
                    'resident_id': resident.id,
                    'score': score
                })
            for cc in self.care_coordinators:
                score = self._calculate_care_coordinator_match_score(volunteer, cc)
                matches['care_coordinator_matches'].append({
                    'volunteer': volunteer.name,
                    'volunteer_id': volunteer.id,
                    'care_coordinator': cc.name,
                    'care_coordinator_id': cc.id,
                    'score': score
                })
        
        matches['doctor_matches'] = sorted(matches['doctor_matches'], key=lambda x: x['score'], reverse=True)
        matches['resident_matches'] = sorted(matches['resident_matches'], key=lambda x: x['score'], reverse=True)
        matches['care_coordinator_matches'] = sorted(matches['care_coordinator_matches'], key=lambda x: x['score'], reverse=True)
        return matches

    def _calculate_doctor_match_score(self, volunteer, doctor):
        # Layer 2: NLP Semantic Matching
        volunteer_text = f"{volunteer.interest_keywords} {volunteer.career_goals}"
        doctor_text = f"{doctor.current_projects}"

        if volunteer_text.strip() and doctor_text.strip():
            # wl.similarity computes cosine similarity (range generally between -1.0 and 1.0)
            research_similarity = max(0.0, self.wl.similarity(volunteer_text, doctor_text))
        else:
            research_similarity = 0.0

        # Layer 3: The Weighted Scoring Matrix
        technical_skills_overlap = self._calculate_set_overlap(volunteer.skills, doctor.required_skills)
        goal_alignment = self._calculate_set_overlap(volunteer.career_goals, doctor.current_projects)

        score = (
            technical_skills_overlap * 0.4 +
            research_similarity * 0.4 +
            goal_alignment * 0.2
        )
        return float(score)

    def _calculate_resident_match_score(self, volunteer, resident):
        # Layer 2: NLP Semantic Matching
        volunteer_text = f"{volunteer.interest_keywords} {volunteer.skills}"
        resident_text = f"{resident.hobbies} {resident.life_history}"
        
        if volunteer_text.strip() and resident_text.strip():
            hobby_overlap = max(0.0, self.wl.similarity(volunteer_text, resident_text))
        else:
            hobby_overlap = 0.0

        # Layer 3: The Weighted Scoring Matrix
        # This is a simplified version, as soft skills and language compatibility are not yet implemented
        score = hobby_overlap * 0.5
        return float(score)

    def _calculate_care_coordinator_match_score(self, volunteer, care_coordinator):
        volunteer_text = f"{volunteer.skills} {volunteer.interest_keywords}"
        cc_text = f"{care_coordinator.facility_programs} {care_coordinator.shift_requirements}"

        if volunteer_text.strip() and cc_text.strip():
            similarity = max(0.0, self.wl.similarity(volunteer_text, cc_text))
        else:
            similarity = 0.0

        skills_overlap = self._calculate_set_overlap(volunteer.skills, care_coordinator.shift_requirements)

        score = similarity * 0.6 + skills_overlap * 0.4
        return float(score)
    
    def _calculate_set_overlap(self, set1_str, set2_str):
        if not set1_str or not set2_str:
            return 0
        
        # Split, trim whitespace, and lowercase for better overlap detection
        set1 = {s.strip().lower() for s in set1_str.split(',') if s.strip()}
        set2 = {s.strip().lower() for s in set2_str.split(',') if s.strip()}
        
        if not set1 or not set2:
            return 0
            
        return len(set1.intersection(set2)) / len(set1.union(set2)) if len(set1.union(set2)) > 0 else 0
