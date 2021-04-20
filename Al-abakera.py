# -*- coding: utf-8 -*-
"""
Al abakera scoring 
consist of 2 teams each with 4 player
need to score each team and best player
"""
class AP:
    def __init__(self):
        self.team1 = {'Menna':0, 'Omar': 0, 'Shaza': 0, "Ahmed": 0}
        self.team2 = {'Mona':0, 'Amr': 0, 'Shimaa': 0, "Ali": 0}
        #self.best = ' '
        
    def game(self, team_name, player, points):
        if team_name == 'team1':
            for k, v in self.team1.items():
                if k == player:
                    self.team1[k] += points
        if team_name == 'team2':
            for k, v in self.team2.items():
                if k == player:
                    self.team2[k] += points
                
        
    def best_player(self):
        max_1 = max(self.team1.values()) #Max of team1 
        max_2 = max(self.team2.values()) #max of team 2   
        
        if max_1 >= max_2 :
            for k, v in self.team1.items():
                if v == max_1:
                    return k, v
        else:
            for k, v in self.team2.items():
                if v == max_2:
                    return k, v
        
    
    def team_winner(self): 
        val_1 = sum(self.team1.values())
        val_2 = sum(self.team2.values())
        winner_score = max(val_2, val_1)
        d = {'team1':val_1 , 'team2': val_2 }
        for k, v in d.items():
            if v == winner_score:
                return k, v
        
    
if __name__ == "__main__":
    gg = AP()
    gg.game('team1','Menna', 10)
    gg.game('team2', 'Ali', 20)
    print(gg.best_player())
    print(gg.team_winner())
    
    
    