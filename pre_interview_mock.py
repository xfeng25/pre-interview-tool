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

# ---- Session Memory for Chat-like Display ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- Display previous chat messages ----
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- User Input Section ----
uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])
user_input = st.chat_input("Type project context here or press Enter...")

# ---- On Message Submit ----
if user_input or uploaded_file:
    if uploaded_file:
        filename = uploaded_file.name
        user_message = f"I’ve uploaded a project brief: **{filename}**"
    else:
        user_message = user_input

    # display user message
    st.session_state.messages.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.markdown(user_message)

    # ---- Mock Assistant Response ----
    assistant_reply = (
        "**Interview Guide (Sample)**\n"
        "• Objective: Identify key goals, stakeholder roles, and success metrics.\n"
        "• Stakeholders: Business Lead, Operations Manager, Technical Partner.\n"
        "• Topics: Pain points | Data flow | Decision bottlenecks.\n\n"
        "**Interview Slide Guide (Sample Questions)**\n"
        "1. What are your top priorities in this initiative?\n"
        "2. Which process currently causes the most friction?\n"
        "3. What insights or data would help align stakeholders more effectively?"
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
