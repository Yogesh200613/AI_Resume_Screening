def get_jobs(score):

    if score >= 90:
        return [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Python Developer"
        ]

    elif score >= 75:
        return [
            "Software Developer",
            "Web Developer",
            "Backend Developer"
        ]

    else:
        return [
            "Internship",
            "Junior Python Developer",
            "Trainee Software Engineer"
        ]