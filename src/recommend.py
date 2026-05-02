def recommend(row):
    actions = []

    if row["attendance"] < 60:
        actions.append("Improve attendance")

    if row["quiz_avg"] < 50:
        actions.append("Practice quizzes")

    if row["lms_logins"] < 10:
        actions.append("Increase LMS activity")

    return ", ".join(actions)