import re
from wordllama import WordLlama
# NOTE: layer 1 (hard requirements) is removed
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
                    'languages': resident.languages,
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

        # Soft Skills Similarity (30%)
        soft_skills_text = f"{volunteer.skills}"
        resident_needs_text = f"{resident.cognitive_profile} {resident.life_history}"
        if soft_skills_text.strip() and resident_needs_text.strip():
            soft_skills_score = max(0.0, self.wl.similarity(soft_skills_text, resident_needs_text))
        else:
            soft_skills_score = 0.0

        # Language Compatibility (20%)
        language_score = self._calculate_language_compatibility(
            f"{volunteer.skills} {volunteer.interest_keywords}",
            f"{resident.languages} {resident.life_history} {resident.hobbies} {resident.cognitive_profile}"
        )

        # Layer 3: The Weighted Scoring Matrix
        score = (
            hobby_overlap * 0.5 +
            soft_skills_score * 0.3 +
            language_score * 0.2
        )
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
    
    def _calculate_language_compatibility(self, text1, text2):
        languages = [
            'english', 'spanish', 'mandarin', 'french', 'arabic', 'bengali', 
            'russian', 'portuguese', 'indonesian', 'urdu', 'japanese', 'german', 
            'punjabi', 'javanese', 'wu', 'telugu', 'turkish', 'korean', 'marathi', 
            'tamil', 'italian', 'vietnamese', 'cantonese', 'hausa', 'thai', 
            'gujarati', 'jin', 'amharic', 'kannada', 'persian', 'bhojpuri', 
            'hakka', 'burmese', 'yoruba', 'uzbek', 'odia', 'maithili', 'sindhi', 
            'ukrainian', 'malayalam', 'sunda', 'igbo', 'romanian', 'tagalog', 
            'dutch', 'kurdish', 'serbian', 'malagasy', 'saraiki', 'nepali', 
            'sinhalese', 'chittagonian', 'zhuang', 'khmer', 'turkmen', 'assamese', 
            'madurese', 'somali', 'marwari', 'magahi', 'haryanvi', 'hungarian', 
            'chhattisgarhi', 'greek', 'chewa', 'kinyarwanda', 'akan', 'kazakh', 
            'sylheti', 'zulu', 'czech', 'rwanda-rundi', 'min bei', 'swedish', 
            'hmong', 'shona', 'uyghur', 'hiligaynon', 'ilongo', 'balochi', 
            'belarusian', 'bambara', 'konkani', 'sign language', 'asl', 'hebrew', 
            'danish', 'finnish', 'norwegian', 'polish', 'farsi', 'hindi', 
            'swahili', 'filipino', 'malay', 'yiddish', 'gaelic', 'welsh', 'catalan',
            'basque', 'galician', 'esperanto', 'latin', 'hawaiian', 'maori',
            'navajo', 'samoan', 'fijian', 'tongan', 'tahitian', 'kashmiri'
        ]
        
        t1_lower = text1.lower()
        t2_lower = text2.lower()
        
        t1_langs = {lang for lang in languages if re.search(r'\b' + re.escape(lang) + r'\b', t1_lower)}
        t2_langs = {lang for lang in languages if re.search(r'\b' + re.escape(lang) + r'\b', t2_lower)}
        
        if not t2_langs:
            # If the resident doesn't mention any specific language, assume default compatibility (100%)
            return 1.0
            
        if t1_langs.intersection(t2_langs):
            # They share at least one language
            return 1.0
            
        # Resident mentions a language, but volunteer doesn't have it
        return 0.0

    def _calculate_set_overlap(self, set1_str, set2_str):
        if not set1_str or not set2_str:
            return 0
        
        # Split, trim whitespace, and lowercase for better overlap detection
        set1 = {s.strip().lower() for s in set1_str.split(',') if s.strip()}
        set2 = {s.strip().lower() for s in set2_str.split(',') if s.strip()}
        
        if not set1 or not set2:
            return 0
            
        return len(set1.intersection(set2)) / len(set1.union(set2)) if len(set1.union(set2)) > 0 else 0
