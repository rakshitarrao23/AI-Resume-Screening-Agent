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

7. Installation & setup

### Requirements

- Python 3.10 or later
- pip
- Required Python packages listed in `requirements.txt`

### Install Dependencies

Create and activate a virtual environment:

```bash
python -m venv .venv

8. Place the Job Description in:

job_description.txt

Place the candidate resumes in:

resumes/

Then run:python screening.py

The agent processes the resumes, compares them against the Job Description, calculates relevance scores, ranks the candidates, and generates the screening results.


9. Input

The agent accepts:

1. A Job Description containing the required role, skills and qualifications.
2. Multiple candidate resumes in PDF format.

The system is designed to process 10 or more resumes in a single run.

10. Output

The agent produces a ranked list of candidates containing:

* Candidate name
* Relevance score
* Match classification
* Matching skills
* Ranking information

Sample results are provided in:

* ranked_candidates.csv
* ranked_candidates.json

The candidates are ordered from the strongest match to the weakest match.

11. Scoring Method

The screening system uses a combination of:

Semantic Similarity

Resume text and Job Description text are converted into sentence embeddings using:

all-MiniLM-L6-v2

Cosine similarity is used to measure semantic relevance between the resume and the Job Description.

Skill Matching

The system identifies required skills from the Job Description and checks whether those skills are present in the candidate resume.

Final Ranking

Candidates are ranked using the computed relevance score and skill-match information.

This approach combines semantic understanding with explicit skill matching rather than relying only on keyword matching.

12. Sample Result

The system was tested on a dataset containing 10 synthetic resumes.

The output provides an ordered ranking of candidates with match scores and match categories such as:

* Good Match
* Moderate Match
* Low Match

The complete sample output is available in:

ranked_candidates.csv

and

ranked_candidates.json

13. Limitations

This project is a prototype resume-screening system.

Limitations include:

* Resume parsing may be affected by unusual PDF layouts.
* Keyword-based skill extraction may miss synonyms or indirectly expressed skills.
* Semantic similarity does not guarantee that a candidate actually possesses a claimed skill.
* The scoring system should support, rather than replace, human recruitment decisions.
* The sample dataset contains synthetic/fictitious candidate information.

14. Trade offs and Design Decisions

Why Sentence Transformers?

all-MiniLM-L6-v2 provides a good balance between semantic understanding, speed and computational requirements. It is lightweight enough for a local prototype.

Why Cosine Similarity?

Cosine similarity provides a simple and interpretable way to compare the semantic representations of resumes and Job Descriptions.

Why Combine Semantic Similarity with Skill Matching?

Semantic similarity captures contextual relevance, while explicit skill matching ensures that important required skills are not overlooked.

Future Improvements

With additional development, the system could be improved by adding:

* More advanced resume entity extraction
* Better handling of synonyms and skill variations
* Experience and education weighting
* Explainable candidate recommendations
* A web-based user interface
* Bias and fairness evaluation
* More extensive testing with diverse resume formats

15. Test Dataset

The repository includes 10 synthetic resumes created specifically for testing the AI Resume Screening Agent.

The candidate names, email addresses and phone numbers in the dataset are fictional placeholders and should not be treated as real candidate information.

16. Conclusion

The AI Resume Screening Agent demonstrates an end-to-end workflow for automatically parsing resumes, comparing candidates against a Job Description, calculating relevance, and producing an ordered shortlist.

The project demonstrates the practical use of Natural Language Processing, sentence embeddings and cosine similarity for automated resume screening.
