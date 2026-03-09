#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install streamlit panda')


# In[3]:


import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ye (Sunny) Xuan | Interactive Resume",
    layout="wide"
)

# -----------------------------
# Data
# -----------------------------
skills_df = pd.DataFrame({
    "Skill": [
        "Python", "SQL", "R Studio", "Excel", "Power BI", "Tableau",
        "Databricks", "Financial Reporting", "Tax Compliance", "Valuation Analytics"
    ],
    "Category": [
        "Programming", "Programming", "Programming", "Tools", "Tools", "Tools",
        "Tools", "Finance", "Finance", "Finance"
    ],
    "Proficiency": [88, 90, 75, 95, 85, 78, 82, 80, 84, 83]
})

education_df = pd.DataFrame({
    "School": [
        "Rotman School of Management, University of Toronto",
        "University of Waterloo"
    ],
    "Program": [
        "Master of Management Analytics Candidate",
        "Bachelor of Financial Analysis and Risk Management, Honours Mathematics"
    ],
    "Period": [
        "08/2025 – 07/2026 (Expected)",
        "09/2020 – 05/2025"
    ],
    "Notes": [
        "Toronto, Ontario, Canada",
        "GPA: 3.7/4.0, Graduated with Distinction"
    ]
})

experience_df = pd.DataFrame({
    "Role": [
        "Data Scientist",
        "Data Analyst",
        "Tax Analyst",
        "Financial Advisor Assistant",
        "Data Analyst"
    ],
    "Company": [
        "Ryan LLC",
        "CIBC",
        "The Stronach Group",
        "Golden Grace Financial Group Inc.",
        "TAIKANG Pension & Insurance Co."
    ],
    "Location": [
        "Toronto, ON",
        "Toronto, ON",
        "Aurora, ON",
        "Toronto, ON",
        "Beijing, China"
    ],
    "Period": [
        "01/2026 – 06/2026 (Expected)",
        "01/2024 – 08/2024",
        "01/2023 – 08/2023",
        "05/2022 – 08/2022",
        "08/2021 – 11/2021"
    ],
    "Focus": [
        "ML, Databricks, LLM + RAG",
        "SQL, Excel, Power BI, KPI reporting",
        "Tax returns, compliance, Excel/VBA",
        "Insurance, wealth planning, ECL model",
        "SQL, ETL, market sizing, reporting"
    ],
    "YearsWeight": [1.0, 1.0, 0.8, 0.4, 0.3]
})

experience_details = {
    "Ryan LLC": [
        "Built regression models to recommend lower UK property tax valuations for appeal cases.",
        "Developed classification models to predict approval probability for valuation-reduction appeals.",
        "Performed Databricks-based EDA and feature engineering; compared new features against baseline models.",
        "Supported an internal LLM + RAG assistant to surface relevant documents and accelerate analysis."
    ],
    "CIBC": [
        "Maintained data quality for enterprise client book-of-record systems using SQL + Excel, updating 20k+ records daily.",
        "Ran trend, segmentation, regression, and outlier diagnostics to explain refund spikes and operational delays.",
        "Built a Power BI dashboard used by 17+ team members in Treasury and Operations.",
        "Created a monthly KPI pack in Excel and saved about 8 hours per week of reporting time."
    ],
    "The Stronach Group": [
        "Prepared Canadian and US tax returns for 10+ entities using Excel and TaxPrep.",
        "Calculated tax provisions, performed compliance checks, and managed trust/election filings.",
        "Built CDA reports with advanced Excel and optimized templates with VBA."
    ],
    "Golden Grace Financial Group Inc.": [
        "Supported 20+ HNW clients across insurance planning, wealth management, tax, and estate questions.",
        "Built an Excel ECL model using probability-of-default and exposure assumptions.",
        "Created reusable client summary packs to improve client conversations and reduce revisions."
    ],
    "TAIKANG Pension & Insurance Co.": [
        "Consolidated 7 years of national health-insurance data into a single SQL fact table.",
        "Sized markets across 5 industries and 3 business lines and presented a management report.",
        "Reconciled analytics to finance totals and collaborated with engineering to improve ETL checks."
    ]
}

project_view = {
    "Analytics": "Strong background in SQL, Excel, Power BI, Tableau, and dashboard/KPI reporting across banking and insurance.",
    "Machine Learning": "Built regression and classification models at Ryan LLC, with Databricks-based EDA and feature engineering.",
    "Finance / Tax": "Hands-on experience in financial reporting, tax compliance, valuation analytics, and client-oriented finance support."
}

# -----------------------------
# Sidebar widgets (3+ interactive widgets)
# -----------------------------
st.sidebar.title("Customize Resume View")

section_choice = st.sidebar.selectbox(
    "Select section",
    ["Overview", "Skills", "Education", "Experience", "Projects"]
)

category_filter = st.sidebar.multiselect(
    "Filter skill category",
    options=sorted(skills_df["Category"].unique()),
    default=sorted(skills_df["Category"].unique())
)

min_proficiency = st.sidebar.slider(
    "Minimum skill proficiency",
    min_value=0,
    max_value=100,
    value=75
)

show_contact = st.sidebar.checkbox("Show contact info", value=True)

selected_company = st.sidebar.selectbox(
    "Highlight experience",
    options=list(experience_details.keys())
)

# -----------------------------
# Header
# -----------------------------
st.title("Ye (Sunny) Xuan")
st.subheader("Interactive Resume")

if show_contact:
    st.write("Email: ye.xuan@rotman.utoronto.ca")
    st.write("Phone: (+1) 437-971-9863")
    st.write("LinkedIn: linkedin.com/in/ye-xuan-94aa55252")

st.markdown(
    """
Data Analyst with experience across banking, insurance, tax, and valuation analytics.
Interested in combining finance, analytics, and machine learning to support better decisions.
"""
)

# -----------------------------
# Filters
# -----------------------------
filtered_skills = skills_df[
    (skills_df["Category"].isin(category_filter)) &
    (skills_df["Proficiency"] >= min_proficiency)
]

# -----------------------------
# Main layout
# -----------------------------
left_col, right_col = st.columns([2, 1])

with left_col:
    if section_choice == "Overview":
        st.markdown("## Overview")
        st.write(
            "This resume highlights experience in data analytics, financial analysis, tax, "
            "and machine learning. My work has included SQL/Excel data quality, KPI reporting, "
            "Power BI dashboards, regression/classification modeling, and LLM + RAG support."
        )

        st.markdown("### Highlighted Experience")
        for bullet in experience_details[selected_company]:
            st.write(f"- {bullet}")

    elif section_choice == "Skills":
        st.markdown("## Skills")
        st.dataframe(filtered_skills, use_container_width=True)

    elif section_choice == "Education":
        st.markdown("## Education")
        st.table(education_df)

    elif section_choice == "Experience":
        st.markdown("## Experience")
        st.dataframe(experience_df.drop(columns=["YearsWeight"]), use_container_width=True)

        st.markdown(f"### Details: {selected_company}")
        for bullet in experience_details[selected_company]:
            st.write(f"- {bullet}")

    elif section_choice == "Projects":
        st.markdown("## Focus Areas")
        project_name = st.selectbox("Choose an area", list(project_view.keys()))
        st.write(project_view[project_name])

with right_col:
    st.markdown("## Skill Chart")
    if filtered_skills.empty:
        st.warning("No skills match the current filters.")
    else:
        chart_df = filtered_skills.set_index("Skill")[["Proficiency"]]
        st.bar_chart(chart_df)

st.markdown("## Work History Table")
st.dataframe(experience_df.drop(columns=["YearsWeight"]), use_container_width=True)

st.markdown("## Experience Timeline Chart")
timeline_df = experience_df.set_index("Company")[["YearsWeight"]]
st.bar_chart(timeline_df)

st.markdown("## Resume Notes")
st.write(
    "This app is personalized using my own resume content and includes interactive filters, "
    "tables, and charts for a more dynamic presentation than a static PDF."
)

