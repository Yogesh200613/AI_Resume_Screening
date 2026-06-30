import matplotlib.pyplot as plt

def create_chart(score):

    matched = score
    missing = 100 - score

    plt.figure(figsize=(5,5))

    plt.pie(
        [matched, missing],
        labels=["Matched Skills", "Missing Skills"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Resume Skill Analysis")

    plt.savefig("static/chart.png")

    plt.close()