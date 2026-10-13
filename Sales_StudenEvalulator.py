# hey it's me its verity


def display_header():
    print(f"Welcome to the Student Performance Evaluator\n")
# ALL THE VARIABLES BELOPW ARE GLOBAL
print("------------------------------------------------------------------------------\n")
print(f"We will be first collecting your infortmation, to evaluate your performance!")
studentname = input("Please enter your name: ")
print(f"Hello, {studentname}!")
while True:
    try:
        score_numerouno = int(input("Ok first enter your, FIRST score. This is important!"))
        if score_numerouno > 100 or score_numerouno < 0:
            print("Sorry, that is invalid digit. Please try again.")
            continue
        score_numerodos = int(input("Now enter another score number, IMPORTANT!"))
        if score_numerodos > 100 or score_numerodos < 0:
            print("Sorry, that is invalid digit. Please try again.")
            continue
        score_numerotres = int(input("Ok one more time, enter your score number one last time!"))
        if score_numerotres > 100 or score_numerotres < 0:
            print("Sorry, that is invalid digit. Please try again.")
            continue
        break
    except ValueError:
        print("Sorry, that is invalid digit. Please try again.")
        continue

def evaluate_performance(TRUE_Average, is_status):
    # ALL THE VARIABLES BELOW ARE LOCAL
    TRUE_Average = (score_numerouno + score_numerodos + score_numerotres) / 3
    if TRUE_Average >= 90:
        is_status = "Outstanding"
    elif TRUE_Average >= 85:
        is_status = "Very Satisfactory"
    elif TRUE_Average >= 80:
        is_status = "Satisfactory"
    elif TRUE_Average >= 75:
        is_status = "Fairly Satisfactory"
    else:
        is_status = "Needs Improvement"

def display_output(TRUE_Average, is_status):
    print(f"{studentname}\n")
    print(score_numerouno, score_numerodos, score_numerotres)
    print(f"The average score is: {TRUE_Average:.2f}")
    print(f"{is_status}\n")
display_header()
evaluate_performance(TRUE_Average, is_status)
display_output(TRUE_Average, is_status)

