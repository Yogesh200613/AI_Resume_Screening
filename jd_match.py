from skills import skills

def jd_match(job_description, resume_text):

    matched_skills = []

    job_description = job_description.lower()
    resume_text = resume_text.lower()

    for skill in skills:

        if skill.lower() in job_description and skill.lower() in resume_text:
            matched_skills.append(skill)

    required_count = 0

    for skill in skills:
        if skill.lower() in job_description:
            required_count += 1

    if required_count == 0:
        match_percentage = 0
    else:
        match_percentage = int((len(matched_skills) / required_count) * 100)

    return matched_skills, match_percentage