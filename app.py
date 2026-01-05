from flask import Flask, render_template, request
from nlp_engine import NLPEngine
from skill_database import SkillDatabase

app = Flask(__name__)
engine = NLPEngine()
db = SkillDatabase()

@app.route("/")
def index():
    return render_template("index.html", job_roles=db.get_all_job_roles())

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.form.get("resume_text")
    role = request.form.get("job_role")

    if not resume or not role:
        return render_template(
            "index.html",
            job_roles=db.get_all_job_roles(),
            error="Please provide resume text and select a job role."
        )

    result = engine.analyze(resume, role)
    return render_template("results.html", results=result)

if __name__ == "__main__":
    app.run(debug=True)
