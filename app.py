import streamlit as st
import pandas as pd
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
st.subheader("Sales and ROAS Forecast")

conversion_rate = st.number_input(
    "Lead to sale conversion rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=10.0,
    step=1.0
)

average_order_value = st.number_input(
    "Average order value",
    min_value=0.0,
    value=500.0,
    step=50.0
)

expected_sales = expected_leads * (conversion_rate / 100)
expected_revenue = expected_sales * average_order_value
expected_roas = expected_revenue / budget if budget > 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("Expected sales", f"{expected_sales:,.0f}")
col2.metric("Expected revenue", f"{expected_revenue:,.2f}")
col3.metric("Expected ROAS", f"{expected_roas:.2f}x")
st.divider()
st.header("Meta Ads Report Analyzer")

uploaded_file = st.file_uploader(
    "Upload your Meta Ads report",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        report = pd.read_csv(uploaded_file)

        st.success("Report uploaded successfully!")
        st.write(f"Rows: {len(report)}")
        st.subheader("Report Preview")
        st.dataframe(report, use_container_width=True)

    except Exception as error:
        st.error(f"Could not read the file: {error}")
