import random

def fizzbuzz(n):
    if n%15 ==0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def fizzbuzz_game(player_numbers):
    players = list(range(1,player_numbers + 1))
    current_number = random.randint(1,100)
    print(f"Computer choose the starting number: {current_number}")
    
    
    while len(players)>1:
        next_players = []
        for player in players:
            correct_response = fizzbuzz(current_number)
            playerresponse = input(f"player{player}, what is your response for {current_number}: ")
            
            if playerresponse.lower() != correct_response.lower(): 
                print(f"player{player} made a mistake so he/she is eliminated:")
            else:
                next_players.append(player)
                print(f"player{player} was correct: ")
                
            current_number = random.randint(1,100)
            
            
        players = next_players
        
    if players:
        print(f"player{players[0]} wins")
    else:
        print("No winner")
            
player_number = int(input("enter the player number: "))
fizzbuzz_game(player_number)