import re


def extract_email(text):

    match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    return match.group(0) if match else "Not found"


def extract_phone(text):

    match = re.search(
        r'(\+91[\s-]?)?[6-9]\d{9}',
        text
    )

    return match.group(0) if match else "Not found"


def extract_experience(text):

    pattern = r'(\d+(?:\.\d+)?)\+?\s*(?:years?|yrs?)'

    matches = re.findall(
        pattern,
        text.lower()
    )

    if not matches:
        return 0

    return max(
        float(value)
        for value in matches
    )


def extract_name(text):

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if lines:
        return lines[0]

    return "Unknown Candidate"