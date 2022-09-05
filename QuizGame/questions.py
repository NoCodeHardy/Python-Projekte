import score


def question1():
    print("Wieviele Muskeln hat eine Katze in einem Ohr?")
    answer = input("Antwort a: 32 \n"
                   "Antwort b: 15 \n"
                   "Antwort c: 55 \n"
                   "a/b/c > ")
    answer_correct = "a"
    if answer_correct == answer:
        print("Korrekt!")
        score.player_score += 1
    elif score.hard_mode == True:
        print("Falsch!")
        score.player_score -= 1
    else:
        print("Leider falsch!")
    question_list.remove(question1)

def question2():
    print("Wie heißt Barbie mit vollem Namen?")
    answer = input("Antwort a: Barbara Schöneberger \n"
                   "Antwort b: Babsi \n"
                   "Antwort c: Barbara Millicent Roberts \n"
                   "a/b/c > ")
    answer_correct = "c"
    if answer_correct == answer:
        print("Korrekt!")
        score.player_score += 1
    elif score.hard_mode == True:
        print("Falsch!")
        score.player_score -= 1
    else:
        print("Leider falsch!")
    question_list.remove(question2)


def question3():
    print("Was ist das Nationaltier von Schottland?")
    answer = input("Antwort a: der Drache Drogon \n"
                   "Antwort b: ein Einhorn \n"
                   "Antwort c: Ewan McGregor \n"
                   "a/b/c > ")
    answer_correct = "b"
    if answer_correct == answer:
        print("Korrekt!")
        score.player_score += 1
    elif score.hard_mode == True:
        print("Falsch!")
        score.player_score -= 1
    else:
        print("Leider falsch!")
    question_list.remove(question3)


def question4():
    print("Wie lange gähnt ein Mensch im Durchschnitt?")
    answer = input("Antwort a: 10 Sekunden \n"
                   "Antwort b: von Montag bis Freitag \n"
                   "Antwort c: 6 Sekunden \n"
                   "a/b/c > ")
    answer_correct = "c"
    if answer_correct == answer:
        print("Korrekt!")
        score.player_score += 1
    elif score.hard_mode == True:
        print("Falsch!")
        score.player_score -= 1
    else:
        print("Leider falsch!")
    question_list.remove(question4)


question_list = [question1, question2, question3, question4]
question_count = len(question_list)
