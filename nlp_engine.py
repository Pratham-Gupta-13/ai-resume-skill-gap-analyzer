from skill_database import SkillDatabase
from text_processor import TextProcessor

class NLPEngine:
    def __init__(self):
        self.db = SkillDatabase()
        self.processor = TextProcessor()

    def extract_skills(self, text):
        tokens = self.processor.preprocess(text)

        tech = {s for s in self.db.technical_skills if s in tokens}
        soft = {s for s in self.db.soft_skills if s in tokens}

        return sorted(tech), sorted(soft)

    def analyze(self, resume_text, role_key):
        role = self.db.get_job_role(role_key)
        if not role:
            return None

        tech_found, soft_found = self.extract_skills(resume_text)

        tech_req = role["technical_skills"]
        soft_req = role["soft_skills"]

        tech_match = round(len(set(tech_found)&tech_req)/len(tech_req)*100,2)
        soft_match = round(len(set(soft_found)&soft_req)/len(soft_req)*100,2)
        overall = round(0.7*tech_match + 0.3*soft_match,2)

        missing_tech = sorted(tech_req - set(tech_found))
        missing_soft = sorted(soft_req - set(soft_found))

        if overall >= 80:
            category = "Excellent Match"
            recommendation = "Candidate is highly suitable for the selected role."
        elif overall >= 60:
            category = "Good Match"
            recommendation = "Candidate meets most requirements but minor upskilling is advised."
        elif overall >= 40:
            category = "Average Match"
            recommendation = "Candidate requires significant skill improvement."
        else:
            category = "Poor Match"
            recommendation = "Candidate does not currently meet the role requirements."

        return {
            "job_role": role["name"],
            "category": category,

            "scores": {
                "overall_match": overall,
                "technical_match": tech_match,
                "soft_match": soft_match
            },

            "resume_skills": {
                "technical_skills": tech_found,
                "soft_skills": soft_found
            },

            "missing_skills": {
                "technical": missing_tech,
                "soft": missing_soft
            },

            "recommendation": recommendation
        }
