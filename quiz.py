# Questions for the Fast Cars Quiz
questions = [
    {
        "question": "Which car holds the record for the fastest production car in 2022?",
        "options": ["1. Bugatti Chiron Super Sport 300+", "2. Koenigsegg Jesko Absolut", "3. SSC Tuatara", "4. Hennessey Venom F5"],
        "answer": 3  # SSC Tuatara
    },
    {
        "question": "What does 'GT' stand for in car names?",
        "options": ["1. Grand Touring", "2. Grand Turbo", "3. General Transport", "4. Great Traction"],
        "answer": 1  # Grand Touring
    },
    {
        "question": "Which car manufacturer produces the Aventador?",
        "options": ["1. Ferrari", "2. Lamborghini", "3. McLaren", "4. Porsche"],
        "answer": 2  # Lamborghini
    },
    {
        "question": "Which car brand is known for the iconic Supra?",
        "options": ["1. Nissan", "2. Toyota", "3. Mazda", "4. Honda"],
        "answer": 2  # Toyota
    },
    {
        "question": "What is the top speed of the Bugatti Veyron Super Sport?",
        "options": ["1. 267 mph", "2. 250 mph", "3. 280 mph", "4. 300 mph"],
        "answer": 1  # 267 mph
    },
    {
        "question": "Which country is Pagani based in?",
        "options": ["1. Germany", "2. Italy", "3. France", "4. UK"],
        "answer": 2  # Italy
    },
    {
        "question": "The McLaren F1 was first produced in which year?",
        "options": ["1. 1990", "2. 1992", "3. 1994", "4. 1996"],
        "answer": 2  # 1992
    },
    {
        "question": "Which car is featured in the Fast & Furious series as Brian's signature vehicle?",
        "options": ["1. Mitsubishi Eclipse", "2. Nissan GT-R", "3. Toyota Supra", "4. Mazda RX-7"],
        "answer": 3  # Toyota Supra
    },
    {
        "question": "What does 'RPM' stand for in car terminology?",
        "options": ["1. Revolutions Per Minute", "2. Rotation Per Mile", "3. Rate Per Minute", "4. Revolves Per Motor"],
        "answer": 1  # Revolutions Per Minute
    },
    {
        "question": "Which car manufacturer makes the 'LaFerrari'?",
        "options": ["1. McLaren", "2. Ferrari", "3. Porsche", "4. Lamborghini"],
        "answer": 2  # Ferrari
    }
]

# Function to display the welcome message and get the user's name
def welcome_message():
    """
    Display a welcome message and prompt the user for their name.
    """
    print("\nWelcome to the Fast Cars Quiz!")
    name = input("What is your name? ").strip()
    print(f"\nHello, {name}! Use the main menu to start the quiz, view instructions, or exit.\n")
    return name

# Function to display instructions
def view_instructions():
    """
    Display quiz instructions to the user.
    """
    print("\nInstructions:")
    print("1. The quiz consists of 10 multiple-choice questions about fast cars.")
    print("2. Each question has 4 options, and you need to select the correct one.")
    print("3. Your final score will be displayed at the end.")
    print("4. Have fun and good luck!\n")

# Function to display a question and validate user input
def ask_question(question_data, question_number):
    """
    Display a single quiz question and get the user's answer.
    """
    print(f"Question {question_number}: {question_data['question']}")
    for option in question_data["options"]:
        print(option)
    
    while True:
        try:
            answer = int(input("Your answer (1-4): ").strip())
            if 1 <= answer <= 4:
                return answer
            else:
                print("Invalid choice. Please select an option between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

# Function to calculate the final score
def calculate_score(user_answers):
    """
    Calculate the user's final score based on correct answers.
    """
    score = 0
    for i, user_answer in enumerate(user_answers):
        if user_answer == questions[i]["answer"]:
            score += 1
    return score

# Function to display the results
def display_results(score, total_questions, name):
    """
    Display the user's quiz results and a message based on their score.
    """
    print("\nQuiz Results:")
    print(f"Your Score: {score}/{total_questions}")
    
    if score == total_questions:
        print(f"Excellent, {name}! You're a true car enthusiast!")
    elif score >= total_questions * 0.7:
        print(f"Great job, {name}! You really know your cars!")
    elif score >= total_questions * 0.4:
        print(f"Not bad, {name}! You have some knowledge of fast cars.")
    else:
        print(f"Better luck next time, {name}! Keep learning about these amazing machines.")
    
    print("\nThank you for taking the Fast Cars Quiz!")

# Function to run the quiz
def run_quiz(name):
    """
    Run the quiz for the user.
    """
    user_answers = []
    
    for i, question_data in enumerate(questions, start=1):
        user_answer = ask_question(question_data, i)
        user_answers.append(user_answer)
    
    score = calculate_score(user_answers)
    display_results(score, len(questions), name)

# Main menu function
def main_menu():
    """
    Display the main menu and handle user choices.
    """
    name = welcome_message()
    
    while True:
        print("\nMain Menu:")
        print("1. Start Quiz")
        print("2. View Instructions")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            run_quiz(name)
        elif choice == "2":
            view_instructions()
        elif choice == "3":
            print(f"\nGoodbye, {name}! Thanks for visiting the Fast Cars Quiz.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
