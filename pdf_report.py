from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_report(filename, score, jd_match, recommendation):

    pdf = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>AI Resume Screening Report</b>", styles["Title"]))
    elements.append(Paragraph(f"Resume : {filename}", styles["Normal"]))
    elements.append(Paragraph(f"Resume Score : {score}%", styles["Normal"]))
    elements.append(Paragraph(f"JD Match : {jd_match}%", styles["Normal"]))
    elements.append(Paragraph(f"Recommendation : {recommendation}", styles["Normal"]))

    pdf.build(elements)