import mysql.connector
import random

# Connect to the MySQL database
df1 = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="192837465500Aa&",
    database="gamerecords"
)
cur = df1.cursor()

def guess_game():
    number = random.randint(1, 10)
    chances = 3
    
    print("Welcome to the Guessing Game!")
    name = input("Please enter your name: ")
    print("Hello,", name + "! I have selected a number between 1 and 10.")
    
    while chances > 0:
        guess = int(input("Take a guess: "))
        
        if guess == number:
            print("Congratulations,", name + "! You guessed the correct number.")
            print("You win!")
            s = "pass"
            c = 3 - chances
            return name, s, c
        
        print("Wrong guess!")
        chances -= 1
        if chances > 0:
            print("Try again. You have", chances, "chance(s) left.")
    
    print("Game over, ", name + "! You ran out of chances.")
    print("The correct number was:", number)
    print("You lose!")
    n = name
    s = "fail"
    c = 3
    return n, s, c

name, status, chances_taken = guess_game()
print("Name:", name)
print("Status:", status)
print("Chances Taken:", chances_taken)

# Insert values into the MySQL table
query = "INSERT INTO details (name, status, chances) VALUES (%s, %s, %s)"
values = (name, status, chances_taken)
cur.execute(query, values)

# Commit the changes and close the connection
df1.commit()
cur.close()
df1.close()
