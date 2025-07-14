import streamlit as st
import requests

st.title("🧠 GenAI Document Assistant")

# Upload document
st.header("1. Upload Your PDF or TXT")
uploaded_file = st.file_uploader("Choose a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    res = requests.post("http://127.0.0.1:8000/upload/", files=files)
    
    if res.status_code == 200:
        st.success("✅ Document uploaded and processed successfully!")
        st.subheader("📄 Auto Summary")
        st.info(res.json()["summary"])
    else:
        st.error("❌ Upload failed. Check server logs.")

# Ask Anything
st.header("2. Ask Anything from the Document")
question = st.text_input("Your Question")
if st.button("Ask"):
    res = requests.post("http://127.0.0.1:8000/ask/", json={"query": question})
    if res.status_code == 200:
        data = res.json()
        st.success("✅ Answer:")
        st.write(data["answer"])
        st.caption(f"🧾 Justified by: {data['justification']}")
    else:
        st.error("⚠️ Ask failed.")

# Challenge Mode
st.header("3. Challenge Me 💡")

if st.button("Get Challenge Questions"):
    res = requests.get("http://127.0.0.1:8000/challenge/")
    if res.status_code == 200:
        questions = res.json()["questions"]
        answers = []
        st.session_state["challenge_qs"] = questions
        for i, q in enumerate(questions):
            answers.append(st.text_input(f"Q{i+1}: {q}", key=f"ans_{i}"))
        if st.button("Submit Answers"):
            for i, user_ans in enumerate(answers):
                payload = {"question": questions[i], "user_answer": user_ans}
                eval_res = requests.post("http://127.0.0.1:8000/evaluate/", data=payload)
                if eval_res.status_code == 200:
                    eval = eval_res.json()
                    st.write(f"✅ Feedback on Q{i+1}:")
                    st.write(eval["feedback"])
                else:
                    st.error("❌ Evaluation failed.")
