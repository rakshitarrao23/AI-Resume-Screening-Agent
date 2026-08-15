import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def normalize_text(text):
    return re.sub(
        r"\s+",
        " ",
        text.lower()
    ).strip()


def semantic_similarity(resume_text, jd_text):

    resume_text = normalize_text(resume_text)
    jd_text = normalize_text(jd_text)

    embeddings = model.encode(
        [resume_text, jd_text]
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return float(similarity)


def extract_skills(text, skills):

    text = text.lower()

    found = []

    for skill in skills:

        pattern = r"\b" + re.escape(
            skill.lower()
        ) + r"\b"

        if re.search(pattern, text):
            found.append(skill)

    return found


def skill_score(resume_text, required_skills):

    found = extract_skills(
        resume_text,
        required_skills
    )

    if not required_skills:
        return 0, found

    score = (
        len(found) / len(required_skills)
    ) * 100

    return score, found