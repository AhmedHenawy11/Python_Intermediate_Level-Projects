from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def create_quastion_bank():

    question_bank = []

    for item in question_data:
        question_text = item["text"]
        question_answer = item["answer"]
        question_bank.append(Question(question_text, question_answer))

    return question_bank


def main():
    quiz = QuizBrain(create_quastion_bank())
    quiz.quiz_mode()


main()