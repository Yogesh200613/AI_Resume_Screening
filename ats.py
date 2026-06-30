def ats_rank(score, jd_match):

    final_score = (score * 0.6) + (jd_match * 0.4)

    if final_score >= 90:
        rank = "Excellent ⭐⭐⭐⭐⭐"

    elif final_score >= 75:
        rank = "Good ⭐⭐⭐⭐"

    elif final_score >= 60:
        rank = "Average ⭐⭐⭐"

    else:
        rank = "Needs Improvement ⭐⭐"

    return round(final_score, 2), rank