# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully
1. set total loses to 0
2. Create a function called 'initial sticks'
   3. enter loop
   3. prompt user to enter number of sticks (10-100)
      4. if input is between 10 and 100 
         5. return number
      6. otherwise
         7. output error message and continue the loop
8. create a function called 'player turn'
   9. enter loop
   10. prompt player to take 1-3 sticks
   11. if input is between 1-3:
       12. return remaining sticks
   13. otherwise
       14. output error message and continue loop
15. create a function called 'computer turn'
    16. generate a random number between 1 and 3
    17. display how many sticks the computer took
19. create a while loop called play again
20. while play again is true (main loop)
    21. call function 'initial sticks' to set the number of sticks for this game
    22. create a list called 'players' with [Player 1, Player 2, Computer].
    23. set current player index to 0
    24. create a dictionary game losses to track losses for this game, initially 0 for each player.
25. enter stick taking loop
    26. while the number of sticks is greater than 0:
        27. display the current number of sticks
    28. if current player is 'computer' 
        29. call computer turn function to get number of sticks taken
    30. otherwise 
        31. call player turn function to get number of sticks taken
        32. subtract taken sticks from total sticks
    33. if sticks is 0
        34. output that the current player has lost
        35. add loss to game losses
    36. add game losses to total losses
37. prompt user to answer if they would like to play again
    38. if user inputs yes
        39. continue main loop
    40. if user inputs no
        41. set play again to false
42. output total losses for each player from total losses
    