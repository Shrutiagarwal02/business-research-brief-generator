import pandas as pd
import streamlit as st

st.set_page_config(page_title="Business Research Brief Generator", layout="wide")

st.title("Business Research Brief Generator")
st.caption("Turn research notes into an executive-ready business brief with evidence, caveats and next steps.")

with st.sidebar:
    st.header("Brief Settings")
    audience = st.selectbox(
        "Audience",
        ["Partner / Director", "Client leadership", "Investment committee", "Internal strategy team"],
    )
    urgency = st.selectbox("Decision urgency", ["Low", "Medium", "High"])
    confidence_floor = st.slider("Minimum confidence threshold", 1, 5, 3)

question = st.text_input(
    "Research question",
    "Should the company expand into the UK premium packaged-food market?",
)
context = st.text_area(
    "Business context",
    height=90,
    placeholder="Add company, market, product, client objective or decision background.",
)

st.subheader("Evidence Table")
sample_evidence = pd.DataFrame(
    {
        "Source": ["Regulator guidance", "Competitor website", "Industry article"],
        "Claim": [
            "Food-labeling requirements must be checked before launch.",
            "Premium brands compete on provenance, quality and niche positioning.",
            "UK consumers show demand for convenient premium food products.",
        ],
        "Strength": ["High", "Medium", "Medium"],
        "Limitation": [
            "Needs current date verification.",
            "Competitor claim may be marketing-led.",
            "Article may not quantify exact target segment.",
        ],
    }
)

evidence = st.data_editor(
    sample_evidence,
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True,
)

assumptions = st.text_area(
    "Known assumptions",
    height=100,
    value="Market demand is based on public signals only; pricing, distribution cost and competitor sales data require validation.",
)
open_questions = st.text_area(
    "Open questions",
    height=100,
    value="What is the exact target segment? Which distribution channel is commercially viable? What compliance steps affect launch timeline?",
)

strength_score = {"High": 5, "Medium": 3, "Low": 1}
available_scores = [strength_score.get(str(value), 1) for value in evidence["Strength"].fillna("Low")]
confidence = round(sum(available_scores) / max(len(available_scores), 1), 1)
confidence_label = "High" if confidence >= 4 else "Medium" if confidence >= confidence_floor else "Low"

high_claims = evidence[evidence["Strength"] == "High"]["Claim"].dropna().tolist()
medium_claims = evidence[evidence["Strength"] == "Medium"]["Claim"].dropna().tolist()
limitations = evidence["Limitation"].dropna().tolist()

if confidence_label == "High":
    answer = "Proceed to a focused business case, subject to targeted validation of commercial and operational assumptions."
elif confidence_label == "Medium":
    answer = "Proceed with caution and complete further diligence before making a final decision."
else:
    answer = "Do not recommend a decision yet; evidence is too limited for a reliable conclusion."

st.subheader("Executive Brief")
col1, col2, col3 = st.columns(3)
col1.metric("Evidence confidence", confidence_label, confidence)
col2.metric("Evidence items", len(evidence))
col3.metric("Decision urgency", urgency)

st.markdown("### Executive Answer")
st.write(answer)

st.markdown("### Evidence Summary")
if high_claims:
    st.markdown("**Strongest evidence**")
    for claim in high_claims:
        st.markdown(f"- {claim}")
if medium_claims:
    st.markdown("**Supporting evidence**")
    for claim in medium_claims:
        st.markdown(f"- {claim}")

st.markdown("### Risks and Caveats")
for limitation in limitations[:5]:
    st.markdown(f"- {limitation}")

st.markdown("### Open Questions")
for line in [item.strip() for item in open_questions.split("?") if item.strip()]:
    st.markdown(f"- {line}?")

st.markdown("### Recommended Next Steps")
st.markdown(
    "- Validate the highest-impact assumptions with current sources.\n"
    "- Build a one-page recommendation memo for the selected audience.\n"
    "- Add a base, upside and downside view before leadership review.\n"
    "- Confirm whether the decision should be made now or delayed pending missing evidence."
)

brief = f"""# Business Research Brief

## Question
{question}

## Audience
{audience}

## Business Context
{context or "Not provided."}

## Executive Answer
{answer}

## Confidence
{confidence_label} ({confidence}/5)

## Evidence Summary
{chr(10).join("- " + claim for claim in evidence["Claim"].dropna().tolist())}

## Assumptions
{assumptions}

## Risks and Caveats
{chr(10).join("- " + item for item in limitations)}

## Open Questions
{open_questions}

## Recommended Next Steps
- Validate the highest-impact assumptions with current sources.
- Build a one-page recommendation memo for the selected audience.
- Add a base, upside and downside view before leadership review.
- Confirm whether the decision should be made now or delayed pending missing evidence.
"""

st.download_button(
    "Download Markdown Brief",
    data=brief,
    file_name="business_research_brief.md",
    mime="text/markdown",
)
