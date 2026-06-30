from flask import Flask, render_template, request, redirect, session, send_file
import os
import sqlite3

from resume_parser import extract_text
from skills import extract_skills
from score import calculate_score
from missing_skills import get_missing_skills
from recommendation import get_recommendation
from suggestions import get_suggestions
from jd_match import jd_match
from database import create_database, save_resume, create_user_table
from email_sender import send_email
from jobs import get_jobs
from pdf_report import create_report
from charts import create_chart
from ats import ats_rank
from interview import interview_questions
from improvement import improve_resume



create_user_table()
app = Flask(__name__)
app.secret_key = "resume_secret_key"

create_database()


UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("login.html")
@app.route("/home")
def home_page():
    return redirect("/resume")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    # Admin Login
    if username == "admin" and password == "admin123":
        session["admin"] = True
        session["name"] = "Administrator"
        return redirect("/dashboard")

    # Regular user login
    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, name, email
        FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        session["user_id"] = user[0]
        session["name"] = user[1]
        session["email"] = user[2]
        session["admin"] = False
        return redirect("/resume")

    return "Invalid Username or Password"
# ---------------- RESUME PAGE ----------------

@app.route("/resume")
def resume():
    
    return render_template("index.html")

# ---------------- PROFILE ----------------

@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect("/")

    return render_template(
        "profile.html",
        name=session["name"],
        email=session["email"],
        score=90,
        jd_match=85
    )
@app.route("/history")
def history():

    if not session.get("admin"):
        return "Access Denied"

    ...

    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT filename, score, jd_match, recommendation
        FROM resumes
        WHERE user_id=?
        ORDER BY id DESC
    """, (session["user_id"],))

    data = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        data=data
    )
@app.route("/register")
def register():

    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_user():

    name = request.form["name"]
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users
    (name,email,username,password)

    VALUES(?,?,?,?)
    """,

    (name,email,username,password))

    conn.commit()
    conn.close()

    return redirect("/")


# ---------------- UPLOAD ----------------


@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No Resume Uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "Please Select a Resume"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = extract_text(filepath)

    found_skills = extract_skills(text)

    score = calculate_score(found_skills)

    create_chart(score)

    missing_skills = get_missing_skills(found_skills)

    recommendation = get_recommendation(score)

    jobs = get_jobs(score)

    suggestions = get_suggestions(missing_skills)

    job_description = request.form.get("job_description", "")

    matched_skills, match_percentage = jd_match(
        job_description,
        text
    )

    ats_score, ats_result = ats_rank(
        score,
        match_percentage
    )

    questions = interview_questions(found_skills)

    improvement_tips = improve_resume(missing_skills)

    save_resume(
        session["user_id"],
        file.filename,
        score,
        match_percentage,
        recommendation
    )

    create_report(
        file.filename,
        score,
        match_percentage,
        recommendation
    )

    try:
        send_email(
            session["email"],
            score,
            match_percentage
        )
    except Exception as e:
        print("Email Error:", e)

    return render_template(
        "result.html",
        score=score,
        found_skills=found_skills,
        missing_skills=missing_skills,
        recommendation=recommendation,
        suggestions=suggestions,
        matched_skills=matched_skills,
        match_percentage=match_percentage,
        text=text,
        jobs=jobs,
        ats_score=ats_score,
        ats_result=ats_result,
        questions=questions,
        improvement_tips=improvement_tips
    )
@app.route("/compare")
def compare():

    if not session.get("admin"):
        return "Access Denied"

    ...

    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT filename, score, jd_match
        FROM resumes
        ORDER BY score DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return render_template("compare.html", data=data)
# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if not session.get("admin"):
        return "Access Denied"

    ...
    search = request.args.get("search", "")

    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    # Total Users
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # Total Resumes
    cursor.execute("SELECT COUNT(*) FROM resumes")
    total_resumes = cursor.fetchone()[0]

    # Average Score
    cursor.execute("SELECT AVG(score) FROM resumes")
    average_score = cursor.fetchone()[0]

    if average_score is None:
        average_score = 0

    # Highest Score
    cursor.execute("SELECT MAX(score) FROM resumes")
    highest_score = cursor.fetchone()[0]

    if highest_score is None:
        highest_score = 0

    # Search
    if search:
        cursor.execute("""
            SELECT id, filename, score, jd_match, recommendation
            FROM resumes
            WHERE filename LIKE ?
            ORDER BY id DESC
        """, ('%' + search + '%',))
    else:
       cursor.execute("""
    SELECT id, filename, score, jd_match, recommendation
    FROM resumes
    ORDER BY score DESC, jd_match DESC
""")

    data = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        data=data,
        total_users=total_users,
        total_resumes=total_resumes,
        average_score=round(average_score, 2),
        highest_score=highest_score
    )
@app.route("/delete/<int:id>")
def delete_resume(id):

    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM resumes WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
@app.route("/download")
def download():
    return send_file("report.pdf", as_attachment=True)
@app.route("/analytics")
def analytics():

    if not session.get("admin"):
        return "Access Denied"

    ...
    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM resumes")
    total_resumes = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(score) FROM resumes")
    average_score = cursor.fetchone()[0] or 0

    cursor.execute("SELECT MAX(score) FROM resumes")
    highest_score = cursor.fetchone()[0] or 0

    conn.close()

    return render_template(
        "analytics.html",
        total_users=total_users,
        total_resumes=total_resumes,
        average_score=round(average_score, 2),
        highest_score=highest_score
    )

if __name__ == "__main__":
    app.run(debug=True)
