class QuizBrain:

    def __init__(self,q_list):
        self.quastion_num = 0
        self.q_list = q_list

    def quiz_mode (self):

        quastion = self.q_list
        index = self.quastion_num
        score = 0
        user_answer = input(f"Q.{index + 1}: {quastion[index].text} (True/False): ")

        while quastion[index].answer:
            if user_answer == quastion[index].answer or user_answer == quastion[index].answer.lower():
                print("You got it right!")
                print(f"The correct answer was: {quastion[index].answer}.")

                score += 1
                index += 1

                print(f"Your current score is: {score}/{index}")
                user_answer = input(f"\nQ.{index + 1}: {quastion[index].text} (True/False): ")

            else:
                index += 1
                print("That's wrong.")
                if index == len(self.q_list):
                    print(f"The correct answer was: {quastion[index-1].answer}.")
                    print(f"Your current score is: {score}/{index}")
                else:
                    print(f"The correct answer was: {quastion[index-1].answer}.")
                    print(f"Your current score is: {score}/{index}")
                if index == len(self.q_list):
                    break
                user_answer = input(f"\nQ.{index + 1}: {quastion[index].text} (True/False): ")
        print("\n_______________________________________________________________")
        print("\nYou've completed the quiz")
        print(f"Your final score was: {score}/{index}")
