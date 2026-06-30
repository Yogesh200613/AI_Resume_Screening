def interview_questions(skills):

    questions = []

    if "Python" in skills:
        questions.append("Explain Python decorators.")
        questions.append("Explain Python OOP concepts.")

    if "Java" in skills:
        questions.append("Explain JVM Architecture.")

    if "SQL" in skills:
        questions.append("Difference between JOIN and UNION?")
        questions.append("Difference between INNER JOIN and LEFT JOIN?")

    if "HTML" in skills:
        questions.append("Difference between HTML and HTML5?")

    if "CSS" in skills:
        questions.append("Explain Flexbox and Grid.")

    if "JavaScript" in skills:
        questions.append("Difference between var, let and const.")

    if "React" in skills:
        questions.append("What are React Hooks?")

    if "Machine Learning" in skills:
        questions.append("Explain Overfitting and Underfitting.")

    if "Artificial Intelligence" in skills:
        questions.append("Difference between AI and ML.")

    return questions