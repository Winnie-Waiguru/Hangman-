import random

print("Welcome to Hangman.")
print("-------------------------------------------------")

guessWord= ["flowers", "Sun", "Trees", "grass", "plates", "Tables", "chair", "flowerbeds", "rings", "bottles"]
randomWord=random.choice(guessWord)

for x in random:
    print("_", end=" ")
    
def printHangman(wrong):
    
    if (wrong== 0):
        print("\n+----------+")
        print("   |")
        print("   |")
        print("   |")
        print("   ===")
    elif (wrong== 1):
        print("\n+----------+")
        print("   |")
        print("   |")
        print("   |")
        print("   ===")  
    elif (wrong== 2):
        print("\n+----------+")
        print("   |")
        print("   |")
        print("   |")
        print("   ===")
    elif (wrong== 3):
        print("\n+----------+")
        print("   |")
        print("   |")
        print("   |")
        print("   ===")
    elif (wrong== 4):
        print("\n+----------+")
        print("   |")
        print("   |")
        print("   |")
        print("   ===")
    elif (wrong== 5):
        print("\n+----------+")
        print("   |")
        print("   |")
        print("   |")
        print("   ===")
    elif (wrong== 6):
        print("\n+----------+")
        print("   |")
        print("   |")
        print("   |")
        print("   ===")     
    