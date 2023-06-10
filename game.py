import random
import db


class Choice:
    def __init__(self, choice):
        self.gesture = ['🖐', '✌', '✊']
        self.choice = choice

    def __eq__(self, other):
        return self.choice == other.choice

    def __lt__(self, other):
        if (self.choice == self.gesture[0] and other.choice == self.gesture[1]) or \
                (self.choice == self.gesture[1] and other.choice == self.gesture[2]) or \
                (self.choice == self.gesture[2] and other.choice == self.gesture[0]):
            return self.choice < other.choice

    def __gt__(self, other):
        if (self.choice == self.gesture[0] and other.choice == self.gesture[2]) or \
                (self.choice == self.gesture[1] and other.choice == self.gesture[0]) or \
                (self.choice == self.gesture[2] and other.choice == self.gesture[1]):
            return self.choice > other.choice


def victory_condition(choice: str, nick):
    user_choice = Choice(choice)
    bot_choice = Choice(random.choice(user_choice.gesture))

    if user_choice > bot_choice:
        db.plus_score(nick)
        return bot_choice.choice, 'Congratulations, plus 2 points.'
    elif user_choice < bot_choice:
        db.minus_score(nick)
        return bot_choice.choice, 'Unlucky, I lost a point'
    else:
        return bot_choice.choice, "There's nothing, let's continue."
