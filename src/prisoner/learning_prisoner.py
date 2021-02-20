import random
import sys

from .prisoner import Prisoner


class LearningPrisoner(Prisoner):
    def __init__(self, name: str = "Criminal Scum", q_table: list = None, epsilon: float = 0.01,
                 will_betray: bool = None, omega_l_rate: float = 0.75, discount_factor: float = 0.8):
        """
        :param name: name of the prisoner
        :param q_table: list of float, a q-table used by RL which defines the policy. Q_table[0] is the q-value for
        staying silent, q_table[1] is the q-value for betraying.
        :param epsilon: used to define the probability of exploration instead of exploitation
        :param will_betray: true if prisoner betrays, false if prisoner chooses to stay silent
        :param omega_l_rate: parameter influencing the learning rate - learning_rate = 1/(episode_index**omega_l_rate)
        this was decided based on https://www.jmlr.org/papers/volume5/evendar03a/evendar03a.pdf
        :param learning_rate: defines how fast the q_values will changes
        :param discount_factor: this number diminishes the rewards over time within an episode. Doesn't matter much
        here since we only have 1 reward per episode, but I want to leave it as a param for my OCD's sake
        """
        if q_table is None:
            q_table = [0, 0]
        self.name = name
        self.q_table = q_table
        self.epsilon = epsilon
        self.will_betray = will_betray
        self.omega_l_rate = omega_l_rate
        self.episode_index = 1
        self.learning_rate = 1 / self.episode_index ** self.omega_l_rate
        self.discount_factor = discount_factor

    def decide_silence_or_betrayal(self):
        """
        Called by the environment to ask a prisoner what's his decision - stay silent or betray co-prisoner
        assigns boolean value to the will_betray attribute
        """
        if random.random() <= self.epsilon:  # check if we explore
            self.will_betray = bool(random.randint(0, len(self.q_table) - 1))  # random decision if we explore
        self.will_betray = bool(self.q_table.index(max(self.q_table)))  # exploit the environment otherwise

    def go_to_jail(self, time_to_serve: int):
        """
        Processes the reward based on the decision made by the prisoner
        :param time_to_serve: time that the prisoner got as a result of their and co-prisoners actions
        """
        if not self.will_betray:
            tb = sys.exc_info()[2]
            raise NoDecisionYetError.with_traceback(tb)

        # update based on the Bellman equation - Q[s,a] = Q[s,a] + alpha * [R(s,a) + gamma * maxQ'[s',a'] - Q(s,a)],
        # since we only have 1 action/state per episode, we omit the gamma * maxQ'[s',a'] term. We only have 1 state
        # so we just plug in Q[a], R(a).
        self.q_table[self.will_betray] = self.q_table[self.will_betray] + self.learning_rate \
            * (time_to_serve - self.q_table[self.will_betray])
        self.will_betray = None

    def update_learning_rate(self):
        self.learning_rate = 1 / (self.episode_index ** self.omega_l_rate)


class NoDecisionYetError(Exception):
    """Exception raised for errors of calling go_to_jail before the prisoner has made up his mind on whether to stay
    silent or betray the co-prisoner by calling go_to_jail

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Prisoner was sent to jail without letting them make a decision first"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'go_to_jail() was called before will_betray() was -> {self.message}'
