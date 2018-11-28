# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    # With no noise, it is not risky to move towards the high reward state.
    answerDiscount = 0.9
    answerNoise = 0
    return answerDiscount, answerNoise

def question3a():
    # Low discount so that +10 isn't preferred, low living
    # reward to incentivize reaching a sink.
    answerDiscount = 0.2
    answerNoise = 0
    answerLivingReward = -2
    return answerDiscount, answerNoise, answerLivingReward

def question3b():
    # Some noise so that upward route is preferred, other
    # params same so that +1 sink is preferred.
    answerDiscount = 0.2
    answerNoise = 0.2
    answerLivingReward = -2
    return answerDiscount, answerNoise, answerLivingReward

def question3c():
    # High discount so that +10 is preferred, no noise
    # so that bottom route is preferred.
    answerDiscount = 1
    answerNoise = 0
    answerLivingReward = -2
    return answerDiscount, answerNoise, answerLivingReward

def question3d():
    # High discount so that +10 is preferred, some noise so
    # that upward route is preferred. Slightly higher living
    # reward so that +1 isn't preferred.
    answerDiscount = 1
    answerNoise = 0.2
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward

def question3e():
    # Living reward is higher than highest sink state reward,
    # so agent will stay away from sinks.
    answerDiscount = 1
    answerNoise = 0
    answerLivingReward = 11
    return answerDiscount, answerNoise, answerLivingReward

def question6():
    # Very low epsilon will lead to the agent failing to explore enough
    # states and thus not achieve the optimal policy. Very high epsilon
    # can reach the optimal policy given sufficient iterations, but not
    # in only 50 iterations.
    return 'NOT POSSIBLE';

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
