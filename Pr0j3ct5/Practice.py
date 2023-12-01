#This Jotter belongs to B0ym3r
#Just A Random Jotter


#FOR LOOPS
#Create pizza list
#Loop through to print a sentence containing each type
#print an external statement
pizzas = ['Pepperoni', 'Pineapple', 'Vegeterian']
for pizza in pizzas:
    print(f"My uncle makes {pizza} pizza.")
    print(f"He taught me how to make {pizza} pizza")
print('I LOVE PIZZA')
print('-----------------------------------------------------------------------------------')

#List comprehension
#Outputing first five square nums wuthout list comp.
squares = []
for i in range(1,6):
    squares.append(i**2)
print(squares)
print('------------------------------------------------------------------------------------')
#Outputing first five square nums WITH list comprehension
sqnums = [i**2 for i in range(1,6)]
print(sqnums)  
  