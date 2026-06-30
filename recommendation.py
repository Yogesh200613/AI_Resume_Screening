def get_recommendation(score):

    if score >= 90:
        return "⭐⭐⭐⭐⭐ Excellent Resume! You are highly suitable for this role."

    elif score >= 75:
        return "⭐⭐⭐⭐ Good Resume! Add a few more technical skills to improve."

    elif score >= 60:
        return "⭐⭐⭐ Average Resume! Improve your projects and technical skills."

    elif score >= 40:
        return "⭐⭐ Needs Improvement! Learn more technical skills and build projects."

    else:
        return "⭐ Poor Resume! Improve your resume, add projects, certifications, and technical skills."