#Program takes a pool of names and choses a random name from the pool
import random

namesString = input('Give me everybody\'s names separated by a comma(,)')
names = namesString.split(', ')

num_names = len(names)
randomChoice = random.randint(0, num_names-1)
person_to_pay = names[randomChoice]
print(f"The person to pay is... {person_to_pay}!")