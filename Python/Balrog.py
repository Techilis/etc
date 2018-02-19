# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:10:38 2018

@author: User
"""

def defeat_balrog(protagonist):    
    def spawn_balrog():
        """Spawns and returns a stubborn balrog"""
        pass
    def balrog_attack(balrog, person):
        """Returns an attack move from the balrog's repertoire"""
        pass
    def yell(protagonist, text):
        # To print a statement of what the protagonist would say
        pass
    cave_balrog = spawn_balrog()
    is_balrog_defeated = False
    yell(protagonist, 'You cannot pass!')
    while not is_balrog_defeated:
        current_attack = balrog_attack(cave_balrog, protagonist)
        if current_attack != None:
            take_defensive_action(protagonist, current_attack)
        yell(protagonist, 'YOU SHALL NOT PASS!')
        take_offensive_action(protagonist, cave_balrog)
        is_balrog_defeated = True
    return True

def take_defensive_action(attacked_entity, attack_move):
    """
    attacked_entity anticipates attack_move and defends himself.
    """
    pass


def take_offensive_action(protagonist, attacked_entity):
    """
    protagonist attacks balrog
    """
    pass
#
# Your stubs will go here
#
defeat_balrog('gandalf')