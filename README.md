# Business Research Brief Generator

Research analyst workflow that turns source notes into an executive-ready business brief with evidence, assumptions, caveats and next steps.

## Recruiter Signal

This project shows research synthesis, business writing, evidence discipline, executive communication and decision support.

It is designed for roles such as:

- Research Analyst
- Business Analyst
- Consulting Analyst
- Strategy Analyst
- Policy / Market Research Associate

## Inputs

- Research question
- Audience
- Source notes and evidence table
- Known assumptions
- Business context
- Decision urgency

## Outputs

- Executive answer
- Evidence summary
- Risks and caveats
- Open questions
- Recommended next steps
- Confidence level
- Exportable Markdown brief

## Why This Matters

Research roles do not only require collecting information. A strong analyst must separate fact from assumption, explain confidence, highlight what is missing and convert research into a decision-ready recommendation. This project demonstrates that full workflow.

## Tech Stack

- Streamlit
- pandas

## How To Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

- CSV upload for research notes
- Source-link validation field
- DOCX/PDF export
- AI-assisted draft synthesis from user-provided sources only
- Evidence quality scoring by source type and recency

## Responsible AI Boundary

The app should separate facts from assumptions and never cite sources that the user did not provide.

