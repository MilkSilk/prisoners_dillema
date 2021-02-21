import random


class Prisoner:
    def __init__(self, name="Criminal Scum", decision_weights=None):
        if decision_weights is None:
            decision_weights = [100, 100]
        self.name = name
        self.decision_weights = decision_weights

    def decide_silence_or_betrayal(self):
        weights_sum = sum(self.decision_weights)
        return random.random() < self.decision_weights[1]/weights_sum

    def go_to_jail(self, time):
        if time == 0:
            return self.name + " goes free!"
        return self.name + " goes to jail for " + str(-time)+" years!"

