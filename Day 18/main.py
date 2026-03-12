from pushup_tracker import PushUpTracker
from models.quotes_model import Quotes
from data import quotes

push_up_quotes = []

tracker  = PushUpTracker(quotes)


def get_quote():
    for q in quotes:
        push_up_quote = Quotes(q)
        push_up_quotes.append(push_up_quote)


is_running = True
get_quote()
while is_running:

    print("\nMy Push-Up Tracker")
    print("1. Add PushUps")
    print("2. Show Progress")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = int(input("How many pushUps did you do? 10, 15, 20, 25 : "))
        is_success = tracker.add_push_ups(amount)
        if is_success:
            tracker.show_progress()

    elif choice == "2":
        tracker.show_progress()

    elif choice == "3":
        print("Good job today 💪")
        is_running = False

