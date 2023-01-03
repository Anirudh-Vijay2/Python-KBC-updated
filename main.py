questions = [
        "Who is the current prime minister of India?",
        "Which team won the FIFA world cup 2022?",
        "Who is the richest prson in India?",
        "Which is the largest planet in our solar system?",
        "Who is the father of Atomic bomb",
        "\"A way of reffering to a country's working population in terms of their existing productive skills and abilities\" is known as?",
        "Which is the most densely populated state in India?",
        "Who is the current prime minister of United Kingdom(England)?",
        "FCI stands for?",
        "Have you subscribed to Code With Harry youtube channel?"
    ]

options = [
        " A: Rahul Gandhi    B: Priyanka Gandhi \n C: Narendra Modi    D: Aravind Kejariwal",
        " A: Portugal    B: India \n C: Argentina    D: France",
        " A: Ratan Tata    B: Gautham Adani \n C: Anil Ambani    D: Mukesh Ambani",
        " A: Earth    B: Jupiter \n C: Mars    D: Saturn",
        " A: Robert Oppenheimer    B: CV Raman \n C: Issac Newton    D: J.J Thomson",
        "A: Working people    B: People as Resource \n C: Workers    D: Employed people",
        " A: Uttar Pradesh    B: Kerala \n C: Maharashtra    D: Bihar",
        " A: Rishi Sunak    B: Boris Johnson \n C: Liz Truss    D: Hugh O'Leary",
        " A: Food Corporation of India    B: Funding Cost Inning\n C: Fantastic Coporation of India    D: Forme Cord of India", 
        " A: Yes    B: No \n C: Maybe    D: Will Do",
    
    ]
answers = ["c", "c", "b", "b", "a", "b", "d", "a", "a", "a"]
OnlyOP = ["a", "b", "c", "d", "q"]
money = [50, 100, 200, 300, 400, 500, 600, 700, 800, 2000]
turn = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "nineth", "tenth (Jackpot)"]


print("Welcome to Updated version of KBC")
need = input("Are you ready play? Enter y to play ")

def Question():
    if need.lower() == "y":
        earned = 0
        for i in range(10):
            print(f"Here is your {turn[i]} question for {money[i]}$")
            print(questions[i])
            print("The options are:")
            print(options[i])
            correct = input("enter the correct option here or enter q to quit here: ")
            if correct.lower() in OnlyOP:
                if correct.lower() == answers[i]:
                    print("yes the answer is correct")
                    print(f"You earn {money[i]}$")
                    earned = earned + money[i]
                    print(f"Your current earning is {earned}")
                    print("\n")
                elif correct.lower() == "q":
                        print("You quit")
                        print(f"You earned {earned}$")  
                        break  
                else:
                    print("Sorry your answer is wrong..! Better luck next time.")
                    print(f"Your earning is {earned}$")
                    break
            else:
               print("Enter a valid option")
               print("Example a, b, c, d")
               break

Question()