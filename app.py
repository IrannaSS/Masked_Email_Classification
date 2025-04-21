"""Streamlit app to classify emails and mask PII."""
import streamlit as st
from core import classify_email_pipeline

st.title("📧 Email Classifier with PII Masking")

email_input = st.text_area("Enter your email content:")

if st.button("Classify"):

    result = classify_email_pipeline(email_input)

    st.subheader("Masked Email")
    st.code(result["masked_email"])

    st.subheader("Detected Entities")
    st.write(result["list_of_masked_entities"])

    st.subheader("Predicted Category")
    st.success(result["category_of_the_email"])
