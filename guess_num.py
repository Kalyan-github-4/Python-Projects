import random
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Choose difficulty level
difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()
speak(f"You chose {difficulty} difficulty level.")
if difficulty == "easy":
    max_number = 50
    max_attempts = 10
elif difficulty == "medium":
    max_number = 100
    max_attempts = 7
elif difficulty == "hard":
    max_number = 100
    max_attempts = 5
else:
    message = "Invalid difficulty level, setting to medium by default."
    print(message)
    speak(message)
    max_number = 100
    max_attempts = 7

# Generate a random number based on difficulty
n = random.randint(1, max_number)
guesses = 0
a = -1

message = f"Guess the number between 1 and {max_number}. You have {max_attempts} attempts."
print(message)
speak(message)

# Loop until the player guesses the number or runs out of attempts
while (a != n) and (guesses < max_attempts):
    guesses += 1
    a = int(input(f"Attempt {guesses}: Guess the number: "))
    
    if a == n:
        message = f"Your guess is correct! You guessed the number {n} in {guesses} attempts."
        print(message)
        speak(message)
        break
    elif a > n:
        message = "Lower number please."
        print(message)
        speak(message)
    else:
        message = "Higher number please."
        print(message)
        speak(message)
    
    # Hint if the guess is close
    if abs(a - n) <= 5 and a != n:
        message = "You're very close!"
        print(message)
        speak(message)

# If the player runs out of attempts
if a != n:
    message = f"Sorry, you've used all your attempts. The correct number was {n}. Better luck next time!"
    print(message)
    speak(message)
