quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. New Delhi", "B. Mumbai", "C. Chennai", "D. Hyderabad"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    }
]

score = 0
print("Welcome To Quiz!")

for q in quiz:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("Correct!!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")
        
print("\nQuiz completed!")
print(f"Your total score: {score}/{len(quiz)}")
A