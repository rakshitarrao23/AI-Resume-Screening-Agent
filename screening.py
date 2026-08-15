def calculate_overall_score(
    semantic_similarity,
    skill_match,
    experience_match,
    education_match
):
    """
    Calculate the final resume score using weighted components.

    Weights:
    - Semantic similarity: 50%
    - Required skills: 30%
    - Experience: 10%
    - Education: 10%
    """

    overall_score = (
        semantic_similarity * 0.50
        + skill_match * 0.30
        + experience_match * 0.10
        + education_match * 0.10
    )

    return round(overall_score, 2)