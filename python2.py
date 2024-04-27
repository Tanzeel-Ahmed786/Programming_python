"""Exercise # 2
Time : This program was written on 2 April 2024
use : this program runs a basic show kon bane ga crorepati"""
questions = {"""How many fingers in one hand?
a-5
b-23
c-10
d-12 """:"a",
"""How many days in a weak?
a-4
b-5
c-3
d-7""":"d",
"""How many months in a year?
a-24
b-12
c-18
d-20""":"b",
"""How many continents in the world?
a-10
b-5
c-3
d-7""":"d",
"""Best programming language?
a-Python
b-C++
c-Java
d-Depends on user""":"d",
"""Bigget city in Pakistan?
a-Karachi
b-Lahore
c-Quetta
d-Peshawar""":"a",
"""Biggest brand in the world?
a-Nike
b-Gucci
c-Apple
d-Toyota""":"c",
"""Country with biggest land?
a-America
b-Canada
c-China
d-Russia""":"d",
"""Best religion in the world?
a-Islam
b-Christianity
c-Hinduism
d-Sikhism""":"a",
"""Biggest youtube channel?
a-T-series
b-Mr-best
c-Honda
d-pakwheels""":"a"}
total_reward = 0
amount = (10,50,100,500,1000,5000,10000,50000,100000,200000)
lives = 2
print("welcome to KBC".center(90))
for i,(question,answer) in enumerate(questions.items()):
    print(f"Question number({i+1}) for {amount[i]} RS is :")
    print(question.center(100))
    while True:
        user_ans = input()
        if user_ans.lower() == "a" or user_ans.lower() == "b" or user_ans.lower() == "c" or user_ans.lower() == "d":

            break
        else:
            print("Wrong option!Please select a option between 'a','b','c','d'.")
            print("Enter your option : ")
    if user_ans.lower() == answer:
        print("Congratulations! your answer is correct.")
        total_reward =  total_reward+amount[i]
    else:
        print("Wrong answer.")
        lives = lives -1
    if lives < 0:
        print("Game over! You have no lives left.")
        break
    else:
        print(f"You have {lives} lives left.")
print(f"Your reward is {total_reward} RS.")
