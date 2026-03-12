import random

datasets = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 630,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 505,
        "description": "Footballer",
        "country": "Argentina"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 430,
        "description": "Singer and Actress",
        "country": "USA"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 400,
        "description": "Reality TV star and Businesswoman",
        "country": "USA"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 395,
        "description": "Actor and Wrestler",
        "country": "USA"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 380,
        "description": "Singer",
        "country": "USA"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 365,
        "description": "Reality TV star",
        "country": "USA"
    },
    {
        "name": "Beyoncé",
        "follower_count": 320,
        "description": "Singer",
        "country": "USA"
    },
    {
        "name": "Justin Bieber",
        "follower_count": 295,
        "description": "Singer",
        "country": "Canada"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 285,
        "description": "Singer",
        "country": "USA"
    }
]

game_state = {
    "a" : {},
    "b" :{},
    "current_score" : 0,
    "continue": True
}

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


first_question = random.choice(datasets)
game_state["a"] = first_question

print(f"Compare A: {first_question["name"]}, a {first_question["description"]}, from {first_question["country"]}")
print("VS")


while game_state["continue"]:
    next_question = random.choice(datasets)

    while next_question == game_state["a"]:
        next_question = random.choice(datasets)
    game_state["b"] = next_question

    print(f"Compare B: {next_question["name"]}, a {next_question["description"]}, from {next_question["country"]}")
    print("******************")
    print(game_state)
    print("******************")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = check_answer(user_choice, game_state["a"]["follower_count"], game_state["b"]["follower_count"])

    if is_correct:
        game_state["current_score"] += 1
        print(f"You're right! Current score: {game_state["current_score"]}")

        game_state["a"] = game_state["b"]
        datasets.remove(game_state["b"])

        if len(datasets) == 0:
            print("You won the game!")
            break
    else:
        print(f"Sorry, that's wrong. Final score: {game_state["current_score"]}")
        game_state["continue"] = False