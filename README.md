# AI Resume Screening Agent

An NLP-based AI Resume Screening Agent developed for the Rooman Technologies 24-Hour AI Agent Challenge.The agent reads a Job Description and a batch of resumes in PDF format, extracts relevant information, compares each resume with the Job Description using semantic similarity and skill matching, and produces a ranked shortlist of candidates.

## 1. Problem Statement

Recruiters often need to screen a large number of resumes against a particular Job Description.

This project automates the initial screening process by:

- Reading multiple PDF resumes
- Extracting resume text
- Extracting relevant skills
- Comparing resumes with the Job Description
- Computing a relevance score
- Ranking candidates from highest to lowest match
- Classifying candidates into match categories
- Exporting the results as CSV and JSON

The system is designed to handle 10+ resumes in a single run.

---

## 2. One-Sentence Description

My agent takes a Job Description and a collection of candidate resumes and produces an ordered, scored shortlist with match classification.

---

## 3. Agent Architecture

The workflow is:

Job Description
        |
        v
Resume PDF Files
        |
        v
PDF Text Extraction
        |
        v
Resume Parsing
        |
        +--------------------+
        |                    |
        v                    v
Skill Matching       Semantic Similarity
        |                    |
        +---------+----------+
                  |
                  v
             Score Calculation
                  |
                  v
           Candidate Ranking
                  |
          +-------+-------+
          |               |
          v               v
        CSV              JSON
        Output           Output

---

## 4. Technologies Used

- Python
- Sentence Transformers
- `all-MiniLM-L6-v2`
- scikit-learn
- PyPDF text extraction
- Regular expressions
- CSV
- JSON
- Git and GitHub

---

## 5. NLP / Scoring Approach

The system uses two important signals for resume screening.

### A. Semantic Similarity

The project uses the Sentence Transformers model:

`all-MiniLM-L6-v2`

The Job Description and resume text are converted into semantic embeddings.

Cosine similarity is then used to measure how closely the resume matches the Job Description.

This allows the system to identify relevant meaning even when the exact wording is different.

For example:

"machine learning experience"

and

"developed predictive models using ML techniques"

can have semantic similarity even though the wording is not identical.

---

### B. Skill Matching

The Job Description contains required skills.

The system searches the resume text for the required skills and identifies which skills are present.

The skill coverage score is calculated as:

Skill Score = (Matched Skills / Required Skills) × 100

This provides an interpretable signal showing how many required skills are present in each resume.

---

### C. Final Candidate Ranking

The system combines semantic relevance and skill matching to generate an overall candidate score.

Candidates are then sorted from the highest score to the lowest score.

The system also assigns a match category such as:

- Strong Match
- Good Match
- Moderate Match
- Low Match

This makes the result easier for a recruiter to interpret.

---

## 6. Project Structure

```text
AI-Resume-Screening-Agent/
│
├── resumes/
│   ├── 01_Aarav_Mehta.pdf
│   ├── 02_Priya_Sharma.pdf
│   ├── 03_Rohan_Kumar.pdf
│   ├── 04_Ananya_Rao.pdf
│   ├── 05_Kiran_Patil.pdf
│   ├── 06_Neha_Verma.pdf
│   ├── 07_Arjun_Reddy.pdf
│   ├── 08_Megha_Nair.pdf
│   ├── 09_Rahul_Singh.pdf
│   └── 10_Sneha_Iyer.pdf
│
├── output/
│   ├── ranked_candidates.csv
│   └── ranked_candidates.json
│
├── job_description.txt
├── resume_parser.py
├── scorer.py
├── screening.py
├── requirements.txt
├── README_DATASET.txt
├── expected_test_notes.txt
└── .gitignore
