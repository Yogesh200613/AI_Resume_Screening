required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "OpenCV",
    "Git",
    "GitHub",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Java",
    "C",
    "C++"
]


def get_missing_skills(found_skills):

    missing = []

    for skill in required_skills:
        if skill not in found_skills:
            missing.append(skill)

    return missing