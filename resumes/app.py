import os
import json
import pandas as pd

from pathlib import Path

from resume_parser import extract_text
from extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_experience
)

from scorer import (
    semantic_similarity,
    skill_score
)


REQUIRED_SKILLS = [
    "Python",
    "Machine Learning",
    "Artificial Intelligence",
    "Natural Language Processing",
    "Data Analysis",
    "SQL",
    "Git",
    "Scikit-learn"
]


def calculate_experience_score(experience):

    if experience >= 0 and experience <= 2:
        return 100

    if experience <= 4:
        return 80

    return 60


def calculate_education_score(text):

    education_keywords = [
        "computer science",
        "information technology",
        "artificial intelligence",
        "data science",
        "engineering"
    ]

    text = text.lower()

    matches = sum(
        keyword in text
        for keyword in education_keywords
    )

    return min(matches * 25, 100)


def screen_resume(file_path, jd_text):

    resume_text = extract_text(file_path)

    similarity = semantic_similarity(
        resume_text,
        jd_text
    )

    skills_score, matched_skills = skill_score(
        resume_text,
        REQUIRED_SKILLS
    )

    experience = extract_experience(
        resume_text
    )

    experience_score = calculate_experience_score(
        experience
    )

    education_score = calculate_education_score(
        resume_text
    )

    final_score = (
        similarity * 100 * 0.50
        + skills_score * 0.30
        + experience_score * 0.10
        + education_score * 0.10
    )

    if final_score >= 80:
        recommendation = "Strong Match"

    elif final_score >= 65:
        recommendation = "Good Match"

    elif final_score >= 50:
        recommendation = "Moderate Match"

    else:
        recommendation = "Low Match"

    return {
        "candidate": extract_name(resume_text),
        "email": extract_email(resume_text),
        "phone": extract_phone(resume_text),
        "experience_years": experience,
        "semantic_similarity": round(
            similarity * 100,
            2
        ),
        "skill_match": round(
            skills_score,
            2
        ),
        "matched_skills": ", ".join(
            matched_skills
        ),
        "experience_score": experience_score,
        "education_score": education_score,
        "final_score": round(
            final_score,
            2
        ),
        "recommendation": recommendation
    }


def main():

    jd_path = Path(
        "data/job_description.txt"
    )

    jd_text = jd_path.read_text(
        encoding="utf-8"
    )

    resume_folder = Path(
        "data/resumes"
    )

    results = []

    for file_path in resume_folder.iterdir():

        if file_path.suffix.lower() not in [
            ".pdf",
            ".docx",
            ".txt"
        ]:
            continue

        print(
            f"Processing: {file_path.name}"
        )

        try:

            result = screen_resume(
                file_path,
                jd_text
            )

            result["file"] = file_path.name

            results.append(result)

        except Exception as e:

            print(
                f"Error processing {file_path.name}: {e}"
            )

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    for index, result in enumerate(
        results,
        start=1
    ):

        result["rank"] = index

    output_folder = Path("output")

    output_folder.mkdir(
        exist_ok=True
    )

    df = pd.DataFrame(results)

    df.to_csv(
        output_folder /
        "ranked_candidates.csv",
        index=False
    )

    with open(
        output_folder /
        "ranked_candidates.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )

    print("\nFINAL RANKING\n")

    print(
        df[
            [
                "rank",
                "candidate",
                "final_score",
                "recommendation"
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()