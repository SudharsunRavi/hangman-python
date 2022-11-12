import random
import stages_logo
import words

print(stages_logo.logo)
game_end=False
chosen_word=random.choice(words.word_list)
life=6
list=[]
for und in chosen_word:
  list += "_"
while game_end==False:
  guess=input("Guess a letter: ").lower()
  for i in range(len(chosen_word)):
    letter=chosen_word[i]
    if letter==guess:
      list[i]=letter
  if guess not in chosen_word:
    life=life-1
    print("You lost a life.You have remaining "+ str(life)+" left")
    if life==0:
      game_end=True
      print("You lost")
  print(' '.join(list))
  if "_" not in list:
    game_end=True
    print("You win!")
  print(stages_logo.stages[life])
