import streamlit as st

st.set_page_config(
    page_title="Stakeholder Consensus Builder – Pre-Interview Generation",
    layout="centered"
)

# ---- Page Title ----
st.markdown(
    "<h2 style='text-align:center;'>Stakeholder Consensus Builder – Pre-Interview Generation</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;color:gray;'>Upload a project brief or type context below to simulate interview material generation (static prototype).</p>",
    unsafe_allow_html=True
)
st.divider()

# ---- Step 1: Upload or Input ----
uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])
manual_text = st.text_area(
    "Or paste context below:",
    height=160,
    placeholder="Paste project background, goals, timeline, and stakeholder context..."
)

# ---- Step 2: Auto-generate Interview Guide ----
if uploaded_file or manual_text:
    st.subheader("Generated Output 1 – Interview Guide (Mock Result)")
    st.success("Interview Guide generated successfully.")
    st.markdown(
        """
        **Interview Guide (Sample Output)**  
        • Objective: Identify project goals, target stakeholders, and success metrics.  
        • Stakeholders: Business Lead, Operations, Technical Team.  
        • Key Topics: KPIs | Workflow Bottlenecks | Communication Gaps.  
        • Duration: 30–45 min, structured by topic.
        """
    )

    st.markdown("---")
    st.markdown(
        "<p style='font-size:16px; font-weight:bold;'>Would you like to generate an Interview Slide Guide (slide deck)?</p>",
        unsafe_allow_html=True
    )

    generate_slide = st.button("Generate Slide Guide")

    if generate_slide:
        st.subheader("Generated Output 2 – Interview Slide Guide (Mock Result)")
        st.info("Slide Guide generated successfully.")
        st.markdown(
            """
            **Interview Slide Guide (Sample Questions)**  
            - What are your top three business priorities?  
            - Which process causes the most friction or delay?  
            - What would success look like six months from now?  
            - What metrics do you currently use to evaluate progress?
            """
        )
else:
    st.warning("Please upload a project brief or paste context to begin.")
