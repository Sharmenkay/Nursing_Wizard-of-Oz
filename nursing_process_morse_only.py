import streamlit as st
st.write("App loaded")

st.set_page_config(page_title="Morse Fall Risk - Nursing Process", layout="centered")

st.title("Morse Fall Risk Simulation")

# 1. Assessment
st.header("1. Assessment")
st.markdown("Please complete the **Morse Fall Scale** below:")

history_falling = st.selectbox("History of falling (immediate or within 3 months)?", ["No", "Yes"])
secondary_diagnosis = st.selectbox("Secondary diagnosis present?", ["No", "Yes"])
ambulatory_aid = st.selectbox("Ambulatory aid used?", ["Normal/bedrest/nurse", "Crutches/cane/walker", "Furniture"])
iv_therapy = st.selectbox("IV therapy or heparin lock?", ["No", "Yes"])
gait = st.selectbox("Gait/transferring?", ["Normal/bedrest/immobile", "Weak", "Impaired"])
mental_status = st.selectbox("Mental status?", ["Oriented to own ability", "Forgets limitations"])

# Scoring logic
score = 0
score += 25 if history_falling == "Yes" else 0
score += 15 if secondary_diagnosis == "Yes" else 0
score += 0 if ambulatory_aid == "Normal/bedrest/nurse" else (15 if ambulatory_aid == "Crutches/cane/walker" else 30)
score += 20 if iv_therapy == "Yes" else 0
score += 10 if gait == "Weak" else (20 if gait == "Impaired" else 0)
score += 15 if mental_status == "Forgets limitations" else 0

# 2. Diagnosis
st.header("2. Diagnosis")
if score >= 45:
    risk_level = "High Risk"
elif 25 <= score < 45:
    risk_level = "Moderate Risk"
else:
    risk_level = "Low Risk"
st.markdown(f"**Fall Risk Score:** {score} → **{risk_level}**")

# 3. Outcomes Identification
st.header("3. Outcomes Identification")
st.write("Goal: Prevent patient falls during hospital stay by tailoring interventions to their risk level.")

# 4. Planning
st.header("4. Planning")
interventions = st.multiselect("Select appropriate interventions:", [
    "Bed alarm engaged", "Frequent rounding", "Close proximity to nurses’ station",
    "Non-slip socks", "Toileting schedule", "Family education", "Use assistive devices"
])
st.write("Selected Interventions:", interventions)

# 5. Implementation
st.header("5. Implementation")
implemented = st.checkbox("Nursing staff confirmed implementation of above interventions.")

# 6. Evaluation
st.header("6. Evaluation")
st.write("Post-intervention re-evaluation is scheduled for 12 hours post-implementation.")

# Contextual Justification
st.subheader("Contextual Justification (Required for XAIR)")
st.write(f"""
According to the **2023 Nurse Protocol Manual**, a Morse Fall Score of {score} categorizes the patient as **{risk_level}**.
Interventions were selected based on standard practices for this level of risk.
""")

# Save logs
with open("morse_logs.txt", "a") as f:
    f.write(f"Score: {score}, Risk: {risk_level}, Interventions: {interventions}\\n")
