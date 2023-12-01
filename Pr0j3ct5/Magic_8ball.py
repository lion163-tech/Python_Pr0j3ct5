#Created by Stesha Quarcoo; similar to the real thing,not so original
#Ask a question and run to wait for an answer
import random 

def Magik8ball(ans):
    if ans == 1:
      return 'It is certain'
    elif ans == 2:
        return 'It is decidedly so'
    elif ans == 3:
        return 'Yes'
    elif ans == 4:
        return 'Reply hazy try again'
    elif ans == 5:
        return 'Ask again later'
    elif ans == 6:
        return 'Concentrate and ask again'
    elif ans == 7:
        return 'My reply is no'
    elif ans == 8:
        return 'Outlook not so good'
    elif ans == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = Magik8ball(r)
print("******************************")
print(fortune)

