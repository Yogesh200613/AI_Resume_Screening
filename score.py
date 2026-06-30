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
    "GitHub"
]


def calculate_score(found_skills):

    matched = 0

    for skill in required_skills:
        if skill in found_skills:
            matched += 1

    score = int((matched / len(required_skills)) * 100)

    return score