from flask import Flask, render_template, request
from database import (
    init_database,
    save_attempt,
    get_statistics,
    get_attempts
)
from simulator.emails import EMAIL_SCENARIOS

app = Flask(__name__)

init_database()

@app.route("/")
def index():
    return render_template(
        "index.html",
        emails=EMAIL_SCENARIOS
    )

@app.route("/answer", methods=["POST"])
def answer():
    email_id = int(request.form["email_id"])
    user_answer = request.form["answer"]

    email = next(
        email for email in EMAIL_SCENARIOS
        if email["id"] == email_id
    )

    correct_answer = "phishing" if email["is_phishing"] else "legitimate"

    is_correct = user_answer == correct_answer

    save_attempt(
        scenario_id=email_id,
        user_answer=user_answer,
        correct_answer=correct_answer,
        is_correct=is_correct
    )

    return render_template(
        "result.html",
        email=email,
        user_answer=user_answer,
        is_correct=is_correct
    )

@app.route("/dashboard")
def dashboard():
    statistics = get_statistics()
    attempts = get_attempts()

    return render_template(
        "dashboard.html",
        statistics=statistics,
        attempts=attempts
    )
if __name__ == "__main__":
    app.run(debug=True)

