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

# Campaign Budget Calculator
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

# Sales and ROAS Forecast
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

# Meta Ads Report Analyzer
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

        total_spend = report["Amount spent (EGP)"].sum()
        total_impressions = report["Impressions"].sum()
        total_clicks = report["Link clicks"].sum()
        total_results = report["Results"].sum()
        total_revenue = report["Purchase conversion value"].sum()

        ctr = (
            total_clicks / total_impressions * 100
            if total_impressions > 0 else 0
        )

        cost_per_result = (
            total_spend / total_results
            if total_results > 0 else 0
        )

        roas = (
            total_revenue / total_spend
            if total_spend > 0 else 0
        )

        st.subheader("Performance Summary")

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        kpi1.metric("Total Spend", f"{total_spend:,.2f} EGP")
        kpi2.metric("Total Results", f"{total_results:,.0f}")
        kpi3.metric("Cost per Result", f"{cost_per_result:,.2f} EGP")
        kpi4.metric("ROAS", f"{roas:.2f}x")

        st.metric("CTR", f"{ctr:.2f}%")

    except Exception as error:
        st.error(f"Could not read the file: {error}")
