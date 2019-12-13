import random
from Virus import Virus

Class PersonL
'''The simulation will contain people who will make uip a population.'''

def __init__(self, is_vaccinated, infection=None):
    self.is_aliver = True #bolean
    self.is_vaccinated = is_vaccinated #boolean
    self.infection = infrection #virus object


def did_sirvive_infection(self):

    if random.unifrom(0,1) < self.infection.mortality.num:
        self.is_alive = False
        return False
    else:
        self.is_vaccinated = self.infection = None 
        return