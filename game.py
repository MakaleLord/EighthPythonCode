
<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono');
html{
   display:flex;
   justify-content:center;
   align-items: center;
   width: 100%;
   height: 100%;
   background-image: url('https://source.unsplash.com/collection/327760/1600x900');
   background-size:cover;
}

body{
   width:55%;
   height:60vh;
   border:1px solid lightgray;
   background-color:white;
   border-radius:8px;
   font-family: 'Roboto Mono', monospace;
   box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
   border-top:32px solid #eee;
   overflow-y:scroll;
}

body > div{
  height: calc(100% - 40px);
  overflow-y:auto;
  padding: 20px;
  font-size: 24px;
  white-space: pre;
}

pre{
  margin:inherit;
  font-family: inherit;
}
</style>

#!/usr/bin/python3
print("Content-type: text/html \n")

import magicwand

from rps import choices, random_choice, check, getSymbol

win = 0
lose = 0
player_choices = ("Rock", "Paper", "Scissors")

for player in player_choices:
    print("You choose", player, getSymbol(player))

    if player not in choices:
        print("Wrong choice")
    else:
        computer = random_choice()
        print("Computer choose", computer, getSymbol(computer))
        if player == computer:
            print("It's a draw")
        elif check(player, computer):
            win = win + 1
            print("You won")
        else:
            lose = lose + 1
            print("You lose")
            
print()
print()
print("Match Summary")
print("Total Matches: ", len(player_choices))
print("You won: ", win)
print("You lost: ", lose)
if win > lose:
    print("You won the whole thing")
elif lose == win:
    print("Nobody won")
else:
    print("You lost")
