import time

def startGame():
  
  readyToPlay = input("Are you ready to play (Y/N)")
  if readyToPlay.upper() == "Y":
    while True:
      try:
        print("-"*40)
        print("You have Total 1 minute Time to Complete the quiz")
        print("-"*40)
        questionLengthPick = int(input("How many Question Do you want? "))
        print(f"you choose {questionLengthPick} Questions to Play\n")
        break
      except ValueError:
        print("Put the Valid number\n")
    return questionLengthPick
  
  elif readyToPlay.upper() == "N":
    print("OKay! NO Quiz Start! Thanks for checking..")
    return 0
  else:
    print("Plz Input the correct one! You Put the wrong Word ...")
    startGame()
  



userAnswers = []
correctAnswers = []

questions = [
    {
        "question": "Who was Naruto's first teacher at the Ninja Academy?",
        "options": [ "Kakashi Hatake", "Jiraiya","Iruka Umino", "Tsunade"],
        "answer": "Iruka Umino"
    },
    {
        "question": "What is the name of Tanjiro Kamado's sister?",
        "options": [ "Mitsuri", "Shinobu", "Kanao","Nezuko"],
        "answer": "Nezuko"
    },
    {
        "question": "What was Light Yagami’s main goal after finding the Death Note?",
        "options": [
            "To become the richest man in the world",
            "To rid the world of criminals and become a god",
            "To resurrect his mother",
            "To pass his exams"
        ],
        "answer": "To rid the world of criminals and become a god"
    },
    {
        "question": "What is the name of the cursed object that Yuji Itadori consumes?",
        "options": ["Sukuna's Finger", "Cursed Amulet", "Black Flash", "Cursed Blade"],
        "answer": "Sukuna's Finger"
    },
    {
        "question": "Who is Gon Freecss's father?",
        "options": ["Hisoka", "Ging Freecss", "Netero", "Killua's father"],
        "answer": "Ging Freecss"
    },
    {
        "question": "What was Sung Jin-Woo’s rank when he first became a hunter?",
        "options": ["E-rank", "D-rank", "C-rank", "B-rank"],
        "answer": "E-rank"
    },
    {
        "question": "What is Frieren's main quest in the story?",
        "options": [
            "To conquer the world",
            "To seek eternal life",
            "To understand human emotions",
            "To become the strongest mage"
        ],
        "answer": "To understand human emotions"
    },
    {
        "question": "What is the name of Naruto’s signature jutsu?",
        "options": ["Chidori", "Rasengan", "Amaterasu", "Shadow Clone Jutsu"],
        "answer": "Rasengan"
    },
    {
        "question": "What is the breathing style used by Zenitsu Agatsuma?",
        "options": ["Water Breathing", "Flame Breathing", "Thunder Breathing", "Wind Breathing"],
        "answer": "Thunder Breathing"
    },
    {
        "question": "What is the name of the exam that Gon takes to become a hunter?",
        "options": ["Ninja Exam", "Chunin Exam", "Hunter Exam", "Wizard Exam"],
        "answer": "Hunter Exam"
    }
]


# endIndex = questionLengthPick


def QuestionLoad(questions,questionLengthPick):
    try:
      Index = 0
      correctAns=0
      totalQuestions = len(questions)

      startTime = time.time()

      for Index in range(questionLengthPick):
        currentQuestionLength = Index % totalQuestions
        question = questions[currentQuestionLength]
        print(f"Question {1+ Index}: {question['question']} ")
        for optionsIndex , option in enumerate(question ["options"],1):
          print(f"{optionsIndex}. {option}")

        userAnswer = input("Enter Your Answer: (in numbers): ")
        userAnswers.append(userAnswer)

        if question["options"][int(userAnswer)-1] ==  question["answer"]:
          print("Good! You are Correct...!")
          correctAns += 1 
          correctAnswers.append(correctAns)
        else:
          print("Sorry, that's incorrect. The correct   answer is", question["answer"])
        input("Plz Press Enter to Continue to next  Question.....\n")
        print(f"{"-"*40}\n")

        if time.time() - startTime >= 60:
          print("Time's Up ! Quiz ended.")
          break
        
    except Exception as e:
        print("You put the invalid inputs , Following error   occurs: ",e)
        question_length_pick = startGame()
        QuestionLoad(questions, question_length_pick)

    endTime = time.time()
    TakeTime = endTime - startTime
    print(f"{"="*40}")
    print("      RESULT     ")
    print("="*40)
    print("Your Answers: ")
    for ans in userAnswers:
      print(f"{ans}",end=" ")
    print()
    res = int((correctAns/questionLengthPick)*100)
    print(f"your result is {res}%")
    print(f"You answered {correctAns} out of  {questionLengthPick} questions correctly!")
    print(f"You take {TakeTime:.2f}s time to complete the quiz")
    # print(f"\n{"="*40}\n")

  

questionLengthPick = startGame()
if questionLengthPick is not None:
  QuestionLoad(questions,questionLengthPick)
else:
  print("Quiz Game stopped! Goodbye")
  
  
print("="*40)


