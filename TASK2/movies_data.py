movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

def add_movies(movies):
    num_movies = int(input("how many movies would you like to add? "))
    for _ in range(num_movies):
        name = input("Enter the movie name: ")
        budget = int(input("Enter the movie budget: "))
        movies.append((name,budget))

def calculate_budget(movies):
    total_budget = sum(budget for _, budget in movies)
    average_budget = total_budget/len(movies)
    print(f"\naverage budget of movies: ${average_budget:,.2f}\n")
    high_budget_movies = []
    
    for name,budget in movies:
        if budget > average_budget:
            high_budget_movies.append((name,budget - average_budget))
            
    print(f"Movies with a budget higher than the average: \n")
    for name,aboveaverage in high_budget_movies:
        print(f"{name}-${aboveaverage:,.2f} above average")
    print(f"\n number of movies with the above budget of average: {len(high_budget_movies)}")
      
      
add_movies(movies)#add morem movies to the lis
calculate_budget(movies)#calculate the budget

    

