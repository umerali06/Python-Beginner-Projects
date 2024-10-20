import time

def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    try:
        user_choice = int(input("Choose the correct option (number): "))
        if user_choice == correct_option:
            print("Correct!")
            return True
        else:
            print(f"Incorrect! The correct answer was: {options[correct_option - 1]}")
            return False
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number corresponding to one of the options.")
        return False

def play_trivia(questions):
    score = 0
    start_time = time.time()
    
    for question, options, correct_option in questions:
        print("\n" + "-" * 40)
        if ask_question(question, options, correct_option):
            score += 1
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print("\n" + "=" * 40)
    print(f"Your final score is: {score}/{len(questions)}")
    print(f"Time taken: {total_time:.2f} seconds")
    print("=" * 40)

# List of trivia questions
questions = [
    ("Who was Naruto's first teacher at the Ninja Academy?", ["Iruka Umino", "Kakashi Hatake", "Jiraiya", "Tsunade"], 1),
    ("What is the name of Tanjiro Kamado's sister?", ["Nezuko", "Mitsuri", "Shinobu", "Kanao"], 1),
    ("What was Light Yagami’s main goal after finding the Death Note?", [
        "To become the richest man in the world",
        "To rid the world of criminals and become a god",
        "To resurrect his mother",
        "To pass his exams"
    ], 2),
    ("What is the name of the cursed object that Yuji Itadori consumes?", ["Sukuna's Finger", "Cursed Amulet", "Black Flash", "Cursed Blade"], 1),
    ("Who is Gon Freecss's father?", ["Hisoka", "Ging Freecss", "Netero", "Killua's father"], 2),
    ("What was Sung Jin-Woo’s rank when he first became a hunter?", ["E-rank", "D-rank", "C-rank", "B-rank"], 1),
    ("What is Frieren's main quest in the story?", [
        "To conquer the world",
        "To seek eternal life",
        "To understand human emotions",
        "To become the strongest mage"
    ], 3),
    ("What is Naruto’s signature jutsu?", ["Chidori", "Rasengan", "Amaterasu", "Shadow Clone Jutsu"], 2),
    ("What is the breathing style used by Zenitsu Agatsuma?", ["Water Breathing", "Flame Breathing", "Thunder Breathing", "Wind Breathing"], 3),
    ("What is the name of the exam that Gon takes to become a hunter?", ["Ninja Exam", "Chunin Exam", "Hunter Exam", "Wizard Exam"], 3)
]

# Start the game
print("Welcome to the Trivia Game!")
play_trivia(questions)
