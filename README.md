# prisoners_dillema
Project based around the prisoners dillema, contains a basic simulator for user defined prisoners and a q-learning solution.

## [problem definition](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)

The problem can be described as follows: two criminals have been captured and are currently questioned by the police. Each of them has a choice - either stay silent and say nothing or they can choose to betray the co-prisoner by telling the police what they have done together. Based on what both of the prisoners decide, a proper sentence will be passed on them. What's most important here, is that if they cooperate with each other they will get the lowest sentence in total - 1 year in prison each. But that might not be in each of the prisoners best interest, from the perspective of a single prisoner it's always worth it to betray the other. The problem is, if they do that, each of them gets 2 years in prison which is worse than staying silent and cooperating with one another. The sentencing is defined as follows (in the most known version of this dilemma):

| prisoner A's decision/ prisoner B's decision | B stays silent | B betrays |
|----------------------------------------------| ------------- | ------ |
| A stays silent | A: 1 year, B: 1 year | A: 3 year, B: 0 year |
| A betrays | A: 0 year, B: 3 year | A: 2 years, B: 2 years |

The aim of this project is to see how will RL agents behave in this setting. The intuition is that they should learn to always betray, no matter what are the policies of the other agents. This is under the assumption, that the reward function is simply the negative of the sentence length, if agents were to learn to minimize the total sentence, they should learn to always cooperate by staying silent.

We also assume that like in the real dillema, the prisoners don't exchange information, not about past decisions in passed episodes and not about their current policy.

# usage
To run the project simply go into /src/runner/main.py and define which function you'd like to use.
For user defined prisoners (the simulation part) edit the predefined_prisoners() function and call it under if \_\_name\_\_ == "\_\_main\_\_":
For q-learning just run q_learning_experiment()
