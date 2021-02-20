import random
import string

from src.environment.environment import Environment
from src.prisoner.prisoner import Prisoner
from src.prisoner.learning_prisoner import LearningPrisoner


def predefined_prisoners():
    imprisoned_jacek = Prisoner(name="Jacek Jankowiak", decision_weights=[50, 50])
    imprisoned_kasia = Prisoner(name="Kasia Górczyńska", decision_weights=[1, 0])
    prison = Environment(imprisoned_jacek, imprisoned_kasia)

    print(prison.pass_sentences())


def q_learning_experiment(n_prisoners=100):
    prisoners = []
    for i in range(n_prisoners):
        prisoner_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) + '-' +\
                      ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
        prisoners.append(LearningPrisoner("Prisoner "+prisoner_id+str(i)))
    print([prisoner.name for prisoner in prisoners])
    print(prisoners)


if __name__ == "__main__":
    # predefined_prisoners()
    q_learning_experiment(100)
