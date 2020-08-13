import numpy as np

def playerSkill(mu=None, sigma=None):
    if (mu or sigma) == None:
        return 
    assert(mu>0, "Player skill must be a positive real number")
    else:
        return np.random.normal(mu, sigma**2)

def playerPerformance(mu=None, beta=None):
    assert(mu>0, "Player performance must be a positive real number")
    return np.random.normal(mu, beta**2)

def step_winning(perf1, perf2, epsilon):
    assert(epsilon>0, "epsilon must be a positive real number")
    if (perf1-perf2) > epsilon:
        return "p1"
    elif np.abs(perf1-perf2) <= epsilon:
        return "draw"
    else:
        return "p2"

def teamPerformance(perfP={}, corrMatrix=None): #we do not consider time at this time
    def individual_contrib():
        

    return teamP.sum()
