import gspread


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quiz')
def check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if quiz[question]['answer'].upper() == ans.upper():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False
        def introduction_message () :
    """
   Quiz rules, and takes an input from user to start.
    Returns true when any key pressed.
    """
    print("Welcome to this quiz!")
    print("you will get questions and you can answer with true or false, you can skip a question anytime by pressing 's'")
    input("Press any key to start ;)\n ")
    return True
    intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer (To move to the next question, press 's') :\n ")
            if answer == "s":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

print(f"Your final score is {score}!\n\n")
print("Want to know the correct answers? Please see them below! ;)\n")
print_dictionary()

