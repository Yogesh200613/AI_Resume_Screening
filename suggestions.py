def get_suggestions(missing_skills):

    suggestions = []

    if "SQL" in missing_skills:
        suggestions.append("Learn SQL and practice writing database queries.")

    if "Machine Learning" in missing_skills:
        suggestions.append("Build at least one Machine Learning project using Scikit-learn.")

    if "Deep Learning" in missing_skills:
        suggestions.append("Learn Neural Networks and Deep Learning concepts.")

    if "TensorFlow" in missing_skills:
        suggestions.append("Practice TensorFlow by building an image classification project.")

    if "Scikit-learn" in missing_skills:
        suggestions.append("Learn Scikit-learn algorithms like Linear Regression and Decision Trees.")

    if "Pandas" in missing_skills:
        suggestions.append("Practice data cleaning and analysis using Pandas.")

    if "NumPy" in missing_skills:
        suggestions.append("Learn NumPy arrays and mathematical operations.")

    if "OpenCV" in missing_skills:
        suggestions.append("Build a Face Recognition or Object Detection project using OpenCV.")

    if "GitHub" in missing_skills:
        suggestions.append("Upload your projects to GitHub with proper README files.")

    if "Git" in missing_skills:
        suggestions.append("Learn Git commands like commit, push, pull and branch.")

    return suggestions