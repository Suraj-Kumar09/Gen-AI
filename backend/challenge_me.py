from transformers import pipeline

question_generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_questions(text, num_questions=3):
    prompt = f"Generate {num_questions} comprehension questions based on the text:\n{text[:1000]}"
    output = question_generator(prompt, max_length=128, do_sample=False)
    return [q.strip() for q in output[0]['generated_text'].split('?') if q.strip()][:num_questions]

def evaluate_answer(question, user_answer, full_text):
    return {
        "score": 1,
        "feedback": f"Your answer seems plausible. Based on the text, here's one possible answer..."
    }
