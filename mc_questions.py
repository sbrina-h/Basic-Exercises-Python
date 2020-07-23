
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        

question_prompts = [
    "What sound do cows make?\n(a) Moo\n(b) Quack\n(c) Meow\n\n",
    "What color is the sky?\n(a) Pink\n(b) Yellow\n(c) Blue\n\n",
    "What is 2 + 2?\n(a) 6\n(b) 4\n(c) 10\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)
