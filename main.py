from environment import Environment
from prisoner import Prisoner

if __name__ == "__main__":
    zapuszkowany_jacek = Prisoner(name="Jacek Jankowiak", decision_weights=[50, 50])
    zapuszkowana_kasia = Prisoner(name="Kasia Górczyńska", decision_weights=[1, 0])
    wiezienie = Environment(zapuszkowany_jacek, zapuszkowana_kasia)

    print(wiezienie.pass_sentences())
