word = "laugh"

allowedAttempts =7
guesses =[]
done = False

while not done:
  for letter in word:
    if letter.lower() in guesses:
      print(letter, end=" ")
    else:
      print("_", end= " ")
  print("") 

  
  guess= input(f"Allowed number of trials left {allowedAttempts}, next guess: ") 
  guesses.append(guess.lower())
  if guess.lower() not in word.lower():
    allowedAttempts -=1
    if allowedAttempts == 0:
      break
    
  done = True
  for letter in word:
    if letter.lower() not in guesses:
      done =False
    
if done:
  print(f"You've found the word. It was {word}")
else:      
   print("")   
      