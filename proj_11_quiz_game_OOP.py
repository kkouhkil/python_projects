"""Author: Keyhan Kouhkiloui Babarahmati
           PhD in Robotics and AI
"""
from colorama import Fore, Style

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


class QuizBrain:

    def __init__(self, q_list):
        self.correct_answer = None
        self.user_input_answer = ""
        self.question_number = 0
        self.question_list = q_list
        self.quiz_score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.user_input_answer = input(f"Q.{self.question_number + 1}: {current_question.text}. (True/False)? ").lower()
        self.correct_answer = current_question.answer
        self.question_number += 1

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_input_answer, correct_answer):
        if user_input_answer.lower() == correct_answer.lower():
            self.quiz_score += 1
            print(f"{Fore.GREEN}You're right!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}You got it wrong!{Style.RESET_ALL}")

        if correct_answer == "True":
            print(f"The correct answer was: {Fore.GREEN}{correct_answer}{Style.RESET_ALL}")
        else:
            print(f"The correct answer was: {Fore.RED}{correct_answer}{Style.RESET_ALL}")
        # print(f"Your current score is: {self.quiz_score}/{self.question_number}")
        print("\n")


question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    quiz.check_answer(quiz.user_input_answer, quiz.correct_answer)

print("Congratulations!, You've just completed the Quiz Game!")
if quiz.quiz_score < len(question_bank)/2:
    print(f"Your score is: {Fore.RED}{quiz.quiz_score}{Style.RESET_ALL}/"
          f"{Fore.GREEN}{len(question_bank)}{Style.RESET_ALL}")
else:
    print(f"Your score is: {Fore.GREEN}{quiz.quiz_score}{Style.RESET_ALL}/"
          f"{Fore.GREEN}{len(question_bank)}{Style.RESET_ALL}")

