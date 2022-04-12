secretWord= "Me"
wordguessed= ""

scoreCount= 6

while scoreCount > 0 :
  userGuess= input("Enter a word: ")

if userGuess in secretWord:
    print("correct")
else:
    scoreCount -=1
    print(f"Incorrect. You have {scoreCount} chances remaining")       
    
wordguessed= wordguessed + userGuess    