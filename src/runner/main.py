import random
import string
import copy
from statistics import mean, stdev

from src.environment.environment import Environment
from src.prisoner.prisoner import Prisoner
from src.prisoner.learning_prisoner import LearningPrisoner


def predefined_prisoners():
    imprisoned_jacek = Prisoner(name="Jacek Jankowiak", decision_weights=[50, 50])
    imprisoned_kasia = Prisoner(name="Kasia Górczyńska", decision_weights=[1, 0])
    prison = Environment(imprisoned_jacek, imprisoned_kasia)

    print(prison.pass_sentences())


def q_learning_experiment(n_prisoners=100, n_episodes=1000):
    prisoners = []
    for i in range(n_prisoners):
        # Generates prisoner id's for example: "Prisoner H3D-54A"
        prisoner_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) + '-' +\
                      ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
        prisoner_id = "Prisoner "+prisoner_id

        prisoners.append(LearningPrisoner(prisoner_id+"."+str(i)))

    for i in range(n_episodes):
        # pair up the prisoners
        prisoner_pairs = []
        available_prisoners = copy.deepcopy(prisoners)
        prisoners = []
        n_pairs = n_prisoners//2  # integer division
        for j in range(n_pairs):
            prisoner_pairs.append([])
            for k in range(2):
                prisoner = random.choice(available_prisoners)
                prisoner_pairs[j].append(prisoner)
                available_prisoners.remove(prisoner)
            prison = Environment(prisoner_pairs[j][0], prisoner_pairs[j][1],
                                 sentences=[[[4, 4], [2, 5]], [[5, 2], [3, 3]]])  # the usual times in prison all +5
            prison.pass_sentences()
            prisoners.append(prisoner_pairs[j][0])
            prisoners.append(prisoner_pairs[j][1])
        if n_prisoners % 2 == 1:  # add back the unpaired prisoner to the pool
            prisoners.append(available_prisoners[0])
    return prisoners


if __name__ == "__main__":
    # predefined_prisoners()
    prisoners = q_learning_experiment(10, 10)
    q_tables = [prisoner.q_table for prisoner in prisoners]
    silence_q_values = [q[0] for q in q_tables]
    betrayal_q_values = [q[1] for q in q_tables]
    descriptive_stats = {"average": [mean(silence_q_values), mean(betrayal_q_values)],
                         "std_dev": [stdev(silence_q_values), stdev(betrayal_q_values)],
                         "min": [min(silence_q_values), min(betrayal_q_values)],
                         "max": [max(silence_q_values), max(betrayal_q_values)],
                         }
    print(descriptive_stats)
    print([prisoner.q_table for prisoner in prisoners])
    for prisoner in prisoners:
        print(prisoner)
