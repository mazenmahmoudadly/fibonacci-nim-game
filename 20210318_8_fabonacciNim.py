#this game is writtrn by mazen mahmoud adly
#id : 20210318
def game(coins,turns):
  while(coins!=0):
    print("remaining coin =",coins)
    #switching turns
    if(turns%2==0):
      print("player 1 turn")
      player1=int(input())
      while((player1==coins and turns==0) or player1<1 or player1>coins or (turns>0 and player1>pervious*2)):
        print("invalid move! \n enter valid number:")
        player1=int(input())

      pervious=player1
      winner=True
      coins=coins-player1
    else:
      print("player 2 turn \n")
      player2=int(input())
      # defining the terms of the game
      while( player2<1 or player2>coins or player2>pervious*2):
        print("invalid move! \n enter valid number:")
        player2=int(input())  
      pervious=player2#update pervious player move and updating state
      winner=False
      coins=coins-player2   
    turns+=1
  if (winner==True):#declaing winner
    print("player 1 wins!!!")
  else:
    print("player 2 wins!!!")    

turns=0
print("welcome to fibonacci nim game!!") 
coins=int(input("how many you want to play with?"))
game(coins, turns)
