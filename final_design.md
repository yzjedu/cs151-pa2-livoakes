# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 
1. set total loses to 0
2. Create a function called 'initial sticks'
   1. enter loop
   2. prompt user to enter number of sticks (10-100)
      1. if input is between 10 and 100 
         1. return number
      2. otherwise:
         2. output error message and continue the loop
3. create a function called 'player turn'
   1. enter loop
   2. prompt player to take 1-3 sticks
   3. if input is between 1-3:
      1. return remaining sticks
   4. otherwise
       2. output error message and continue loop
5. create a function called 'computer turn'
   1. generate a random number between 1 and 3
   2. display how many sticks the computer took
6. create a while loop called play again
7. while play again is true (main loop)
   1. call function 'initial sticks' to set the number of sticks for this game
   2. create a list called 'players' with [Player 1, Player 2, Computer].
   3. set current player index to 0
   4. create a dictionary game losses to track losses for this game, initially 0 for each player.
7. enter stick taking loop
   1. while the number of sticks is greater than 0:
      1. display the current number of sticks
   2. if current player is 'computer' 
      1. call computer turn function to get number of sticks taken
   3. otherwise 
      1. call player turn function to get number of sticks taken
      2. subtract taken sticks from total sticks
   4. if sticks is 0
      1. output that the current player has lost
      2. add loss to game losses
   5. add game losses to total losses
8. prompt user to answer if they would like to play again
   1. if user inputs yes
      1. continue main loop
   2. if user inputs no
      1. set play again to false
      2. output total losses for each player from total losses and end program
    