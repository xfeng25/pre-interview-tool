import streamlit as st

st.set_page_config(
    page_title="Stakeholder Interview Tool – Pre-Interview Generation",
    layout="wide"
)

st.markdown(
    "<h2 style='text-align: center;'>Stakeholder Interview Assistant</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Upload or paste your project brief below to generate structured interview materials.</p>",
    unsafe_allow_html=True
)

# Create a centered layout using columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    uploaded_file = st.file_uploader("", type=["pdf", "docx"])
    manual_text = st.text_area(
        "Paste context or brief here:",
        height=180,
        placeholder="Type or paste your project context (e.g. client background, objectives, stakeholders)..."
    )

    st.markdown("---")
    if uploaded_file or manual_text:
        if st.button("Generate Interview Guide", use_container_width=True):
            st.markdown(
                "<div style='background-color:#f7f9fb; padding:15px; border-radius:10px;'>"
                "<strong>Interview Guide (Sample Output)</strong><br><br>"
                "<ul>"
                "<li>Clarify project goals and key stakeholders</li>"
                "<li>Identify decision-makers and success metrics</li>"
                "<li>Surface major challenges and timeline dependencies</li>"
                "</ul>"
                "</div>",
                unsafe_allow_html=True
            )
            st.markdown("")

            if st.button("Generate Interview Slide Guide", use_container_width=True):
                st.markdown(
                    "<div style='background-color:#f7f9fb; padding:15px; border-radius:10px;'>"
                    "<strong>Slide Deck Question Set (Sample)</strong><br><br>"
                    "<ul>"
                    "<li>What are your top business priorities?</li>"
                    "<li>Which areas have been hardest to automate?</li>"
                    "<li>What would success look like six months from now?</li>"
                    "</ul>"
                    "</div>",
                    unsafe_allow_html=True
                )
    else:
        st.warning("Please upload a file or paste context to begin.")
