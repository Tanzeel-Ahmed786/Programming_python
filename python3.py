'''EXERSISE # 3
Time : this program was written on 14 october 2023 when i was doing a yt course on pyhton basics by codewithharry
use : this program take a string and key from user and encode and decode the message according to the given key'''
import string
import random

def encode_message(stru,key):    
    characters = string.ascii_letters

    if len(stru) < 3:
        print("the message is too small")
    else:
        strlist = stru.split()
        for i,word in enumerate(strlist):
            random_str = "".join(random.sample(characters, key))
            random_str2 = "".join(random.sample(characters, key))
            random_str3 = "".join(random.sample(characters, key))
            if len(word) >= 3:
                modefiedword = word[2:] + word[1] + word[0]
                strlist[i] = random_str + modefiedword + random_str2
            elif len(word) == 2 :
                strlist[i] = word[1] + random_str3 + word[0]
        return  " ".join(strlist)

def decode_message(stru,key):
    if len(stru) < 4 :
        print("The message is to small.")
    else:
        strlist = stru.split()
        for i,word in enumerate(strlist):
            if len(word) > key+2+key:
                modefiedword = word[-key-1] + word[-key-2] + word[key:-key-2]
                strlist[i] = modefiedword
            elif len(word) == 1:
                strlist[i] = word
            else:
                strlist[i] = word[-1] + word[0]
    return " ".join(strlist)

while True:
    try:
        purpose = int(input("Enter 1 to code and 2 to decode message : "))
        if purpose != 1 and purpose != 2:
            raise Exception("Chose an option between 1 and 2...Try again.")
        break
    except ValueError:
        print("Your option must be a number...Try again.")
    except Exception as e:
        print(e)
while True:
    try:
        key = int(input("Enter your key : "))
        if key <= 0:
            raise Exception("Your key must be positive and greater than zero...Try again.")
        break
    except ValueError:
        print("You have not entered a number...Try again.")
    except Exception as e:
        print(e)
stru = input("Enter message : ")
if purpose == 1:
    print(encode_message(stru, key))
elif purpose == 2:
    print(decode_message(stru, key))
