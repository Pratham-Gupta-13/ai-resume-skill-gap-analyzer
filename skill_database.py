class SkillDatabase:
    def __init__(self):
        # Technical skills pool
        self.technical_skills = {
            "python","java","c","c++","javascript","html","css","sql",
            "react","node js","git","mongodb","mysql","flask","django",
            "machine learning","data analysis","nlp","statistics",
            "linux","docker","cloud","aws"
        }

        # Soft skills pool
        self.soft_skills = {
            "communication","teamwork","problem solving",
            "analytical thinking","adaptability","time management"
        }

        # Job roles and required skills
        self.job_roles = {

            "software_developer": {
                "name": "Software Developer",
                "technical_skills": {
                    "python","java","html","css","javascript","sql","git"
                },
                "soft_skills": {
                    "communication","teamwork","problem solving"
                }
            },

            "web_developer": {
                "name": "Web Developer",
                "technical_skills": {
                    "html","css","javascript","react","node js","git"
                },
                "soft_skills": {
                    "communication","teamwork"
                }
            },

            "data_scientist": {
                "name": "Data Scientist",
                "technical_skills": {
                    "python","statistics","machine learning",
                    "data analysis","sql"
                },
                "soft_skills": {
                    "analytical thinking","problem solving"
                }
            },

            "machine_learning_engineer": {
                "name": "Machine Learning Engineer",
                "technical_skills": {
                    "python","machine learning","statistics",
                    "data analysis","nlp"
                },
                "soft_skills": {
                    "analytical thinking","problem solving"
                }
            },

            "cloud_engineer": {
                "name": "Cloud Engineer",
                "technical_skills": {
                    "linux","docker","cloud","aws","python"
                },
                "soft_skills": {
                    "problem solving","adaptability"
                }
            },

            "devops_engineer": {
                "name": "DevOps Engineer",
                "technical_skills": {
                    "linux","docker","git","python","cloud"
                },
                "soft_skills": {
                    "teamwork","communication","problem solving"
                }
            }
        }

    def get_all_job_roles(self):
        return {k: v["name"] for k, v in self.job_roles.items()}

    def get_job_role(self, key):
        return self.job_roles.get(key)
