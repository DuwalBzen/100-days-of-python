import random
from prettytable import PrettyTable
from database import create_table,save_progress,load_progress,show_history,load_last_progress

class PushUpTracker:

    def __init__(self, quotes):
        create_table()

        data = load_last_progress()

        if data:  # database already has data
            self.current_push_ups = data[0]
            self.daily_target = data[1]
        else:  # first time running program
            self.daily_target = 300
            self.current_push_ups = 0

        self.remaining_push_ups = self.daily_target - self.current_push_ups
        self.quotes = quotes
        self.daily_quotes = quotes
        self.milestones = {
            50: "🔥 Good start! Keep going!",
            100: "💪 You're getting stronger!",
            200: "🚀 Elite discipline!",
            300: "🏆 TARGET COMPLETE! Amazing work!"
        }
        # create table when program starts
        create_table()

    def add_push_ups(self, amount):
        if amount > 0:
            self.current_push_ups += amount
            self.remaining_push_ups = self.daily_target - self.current_push_ups
            # save progress to database
            save_progress(self.current_push_ups, self.daily_target)
            self.check_milestone()
            return True
        return False

    def remaining_push_ups(self):
        print(f"You did {self.current_push_ups} pushUps Remaining pushUps: {self.remaining_push_ups}")

    def show_progress(self):

        # Fetch data from db
        data = load_progress()

        if data:
            self.current_push_ups = data[0]
            self.daily_target = data[1]

        self.remaining_push_ups = self.daily_target - self.current_push_ups

        progress = int((self.current_push_ups / self.daily_target) * 100)

        bar_length = 20
        filled = int(bar_length * self.current_push_ups / self.daily_target)
        progress_bar = "█" * filled + "░" * (bar_length - filled)

        quote = self.motivational_message()

        table = PrettyTable()
        table.field_names = ["Metric", "Value"]

        table.align["Metric"] = "l"
        table.align["Value"] = "l"

        table.add_row(["Daily Target", self.daily_target])
        table.add_row(["Completed", self.current_push_ups])
        table.add_row(["Remaining", self.remaining_push_ups])
        table.add_row(["Progress", f"[{progress_bar}] {progress}%"])
        table.add_row(["Quote", quote + " KEEP GOING"])

        print("\n💪 PUSH-UP TRACKER\n")
        print(table)

    def motivational_message(self):
        return random.choice(self.daily_quotes)

    def check_milestone(self):
        if self.current_push_ups in self.milestones:
            print("\n🎯 MILESTONE ACHIEVED!")
            print(self.milestones[self.current_push_ups])



