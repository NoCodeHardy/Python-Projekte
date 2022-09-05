import questions
import score
import random
import sys
stage = 1


player_name = input("Please enter your Name: ")
hard_choice = input("Möchtest du im Hard Mode spielen? Y/N > ")
if hard_choice.upper() == "Y":
    score.hard_mode = True
elif hard_choice.upper() == "N":
    score.hard_mode = False
else:
    print("Falscher Input, Quiz wird beendet!")
    sys.exit()


print(f"Hallo {player_name}!\nBitte gib nur die vorgegebenen Antwortmöglichkeiten ein \n"
      f"da deine Antwort sonst als falsch gewertet wird! \n"
      f"Es werden {questions.question_count} Fragen. Viel Glück! \n\n")

input("Drücke Enter um zu beginnen. \n"
      ">")


while stage <= 4:
        print(f"Hier kommt Frage {stage}!")
        random.choice(questions.question_list)()
        print(f"\n{player_name} dein aktueller Punktestand ist: {score.player_score} \n")
        stage += 1


if score.hard_mode:
    print(f"{player_name} du hast im Hard Mode {score.player_score} von 4 Punkten erreicht!")
else:
    print(f"{player_name} du hast im Normal Mode {score.player_score} von 4 Punkten erreicht!")
