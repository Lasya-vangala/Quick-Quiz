

import random

import time

time_limit=10

quiz_questions=[{         "question": " Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) def", "C) define", "D) func"],
        "answer": "B"
       },

       { "question": " Which of the following is used to output text in Python?",
        "options": ["A) echo", "B) print", "C) output", "D) display"],
        "answer": "B"},

       {"question": " Which symbol is used for single-line comments in Python?",
        "options": ["A) //", "B) <!-- -->", "C) #", "D) /* */"],
        "answer": "C"},

       { "question": " Which of the following data types is **immutable** in Python?",
        "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
        "answer": "D"},

       { "question": " Which operator is used to get the remainder in Python?",
        "options": ["A) /", "B) //", "C) %", "D) **"],
        "answer": "C"}]

while True:

   score=0

   random.shuffle(quiz_questions)


   for q in quiz_questions:
      print(q["question"])
      for option in q["options"]:
        print(option)
    
      start_time = time.time()
      user_answer=input("Enter your answer(A,B,C or D):").upper()
      end_time = time.time()

      if end_time - start_time>time_limit:
         print("time up!")

      elif user_answer == q["answer"]:
         print("correct!")
         score += 1

      else:
         print(f"you'r answer is wrong! correct answer is {q["answer"]}")

    
   percentage=(score/(len(quiz_questions)))*100
   print(f"Quiz Over! Your final score is {score}/{len(quiz_questions)} ({percentage:.2f}%)")

   if percentage == 100:
      print("🏆 Excellent! You got everything right!")
   elif percentage >= 75:
      print("👏 Great job! You did really well!")
   elif percentage >= 50:
      print("🙂 Good effort, but there's room for improvement.")
   else:
    print("😢 Keep practicing, you'll get better!")


   play_again = input("Do you want to play again? (yes/no): ").lower()
   if play_again != "yes":
    print("Thanks for playing! Goodbye! ")
    break

