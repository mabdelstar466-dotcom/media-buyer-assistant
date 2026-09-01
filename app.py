import streamlit as st

st.set_page_config(
    page_title="Media Buyer Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Media Buyer Assistant")
st.write("Analyze your advertising campaigns easily and for free.")
st.success("The application is working successfully!")

st.divider()
st.header("Campaign Budget Calculator")

budget = st.number_input(
    "Campaign budget",
    min_value=0.0,
    value=10000.0,
    step=500.0
)

target_cpl = st.number_input(
    "Expected cost per lead",
    min_value=1.0,
    value=50.0,
    step=1.0
)

expected_leads = budget / target_cpl

st.metric(
    "Expected leads",
    f"{expected_leads:,.0f}"
)
