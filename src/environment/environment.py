class Environment:
    def __init__(self, prisoner_a, prisoner_b, sentences=None):
        """sentences defines the outcomes based on both of the actor's decisions
                        a/b   b1  b2
        e.g. sentences = a1 [[[], []],
                         a2  [[], []]]
        a1/b1 means that actor a/b chose to stay silent
        a2/b2 means that actor a/b chose to betray the other
        in default scenario: if both stay silent they get 1 year in prison each
        if one stays silent and the other betrays, the betrayer goes free, the silent one gets 3 years in prison
        if both betray they both get 2 years in prison
        """
        if sentences is None:
            sentences = [[[-1, -1], [-3, 0]],
                         [[0, -3], [-2, -2]]
                        ]
        self.sentences = sentences
        self.prisoner_a = prisoner_a
        self.prisoner_b = prisoner_b

    def pass_sentences(self):
        decision_a = self.prisoner_a.decide_silence_or_betrayal()
        decision_b = self.prisoner_b.decide_silence_or_betrayal()

        sentence = self.sentences[decision_a][decision_b]

        prisoner_a_fate = self.prisoner_a.go_to_jail(sentence[0])
        prisoner_b_fate = self.prisoner_b.go_to_jail(sentence[1])

        return prisoner_a_fate, prisoner_b_fate
