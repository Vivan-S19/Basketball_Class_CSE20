#Basketball player class that simulates some aspects of a pro basketball career
import random #Need for randint
class Basketball_Player():
    #Class attribute, every player is a basketball player
    profession = "Basketball Player"
   
    #Constructor. Takes the name, jersey number, physicals, and position (PG, SG, SF, PF, or C) of the player
    def __init__(self, name, number, height, wingspan, weight, position):
        self._name = name
        self._number = number
        self._height = height
        self._wingspan = wingspan
        self._weight = weight
        self._position = position
        #Skill attributes, everything is set at the base value of 10
        self._scoring = 10
        self._rebounding = 10
        self._perimeter_defense = 10
        self._paint_defense = 10
        self._playmaking = 10 
        #Not a skill
        self._fitness = 50
        #Skill attributes list for general practice method
        self._attributes_list = [self._scoring, self._rebounding, self._perimeter_defense, self._paint_defense, self._playmaking]
        self._offense_list = [self._scoring, self._rebounding, self._playmaking]
        self._defense_list = [self._perimeter_defense, self._paint_defense]
        self._win_chance = 50 #base win chance is 50

    #Getters return the values of the private data variables set in the constructor
    def get_name(self):
        return self._name
    def get_number(self):
        return self._number
    def get_height(self):
        return self._height
    def get_wingpsan(self):
        return self._wingspan
    def get_weight(self):
        return self._weight
    def get_position(self):
        return self._position
    #Thiss returns string values of the attributes
    def get_attributes_string(self):
        attribute_string = "Scoring: " + str(self._scoring) + "\n" + "Rebounding: " + str(self._rebounding) + "\n" + "Perimeter Defense: " + str(self._perimeter_defense) + "\n" + "Paint Defense: " + str(self._paint_defense) + "\n" + "Playmaking: " + str(self._playmaking) + "\n" + "Fitness: " + str(self._fitness)
        return attribute_string
    #Prints a string showcasing winchance
    def get_win_chance_string(self):
        string = self._name + " has a " + str(self._win_chance) + " win chance attribute."
        return string

    
    #Setters allow the user to change the basketball player and you can cheat by changing win chance and attributes
    def set_name(self, name):
        self._name = name
        return self._name
    def set_number(self, num):
        self._number = num
        return self._number
    def set_height(self, h):
        self._height = h
        return self._height
    def set_wingpsan(self, w):
        self._weight = w
        return self._wingspan
    def set_weight(self, wgt):
        self._weight = weight
        return self._weight
    def set_position(self, pos):
        self._position = pos
        return self._position
    #Cheats
    def set_scoring(self, scoring):
        self._scoring = scoring
        return self._scoring
    def set_playmaking(self, playmaking):
        self._playmaking = playmaking
        return self._playmaking
    def set_rebounding(self, r):
        self._rebounding = r
        return self._rebounding
    def set_perimeter_defense(self, per_d):
        self._perimeter_defense = per_d
        return self._perimeter_defense
    def set_paint_defense(self, paint_d):
        self._paint_defense = paint_d
        return self._paint_defense
    def set_fitness(self, fitness):
        self._fitness = fitness
        return self._fitness
    def set_win_chance(self, win):
        self._win_chance = win
        return self._win_chance

    #Methods for the class

    #Workout method that has a small injury risk
    def work_out(self):
        risk = random.randint(1, 100)
        if risk > 95:
            print("Oh no! " + self._name + " got injured! Now they lose fitness.")
            self._fitness -= 5
        else:
            self._fitness += 5
            print(self._name + " increased fitness by 5.")
        return self._fitness
    
    #Runs offensive drills, increases attributes, injury risk
    def run_drills(self):
        risk = random.randint(1, 100)
        if risk > 95:
            print("Oh no! " + self._name + " got injured! Now they get worse.")
            for i in range(len(self._offense_list)):
                self._offense_list[i] -= 5
            return self._offense_list
        else:
            for i in range(len(self._offense_list)):
                self._offense_list[i] += 5
            print(self._name + " increased offensive attributes by 5")
            return self._offense_list
    
    #Runs defensive drills, increases attributes, injury risk
    def defense_practice(self):
        risk = random.randint(1, 100)
        if risk > 95:
            print("Oh no! " + self._name + " got injured! Now they get worse.")
            for i in range(len(self._defense_list)):
                self._defense_list[i] -= 3
            return self._defense_list
        else:
            for i in range(len(self._defense_list)):
                self._defense_list[i] += 3
            print(self._name + " increased defensive attributes by 3")
            return self._defense_list
    
    #Runs extensive drills, improves offense and defeense, increases attributes more, higher injury risk
    def run_extensive_drills(self):
        risk = random.randint(1, 100)
        if risk > 90:
            print("Oh no! " + self._name + " got injured! Now they get worse.")
            for i in range(len(self._attributes_list)):
                self._attributes_list[i] -= 8
            return self._attributes_list
        else:
            for i in range(len(self._attributes_list)):
                self._attributes_list[i] += 10
            print(self._name + " increased all attributes by 5")
            return self._attributes_list
    
    #Game simulation, this is a BIG chunk of code. Box score stats are based on player attributes on offense, and defensive attributes improve win chance. Then, an outcome is calculated.
    def play_game(self):
    #Seeing how offense impacts the game
        if self._fitness < 50:
            print ("You are not allowed to play the game, your fitness is under 50!")
            return None
        if self._scoring <= 20:
            point_probability = random.randint(0, 100)
            if point_probability <= 10:
                points = random.randint(0,10)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 30 and point_probability > 10:
                points = random.randint(10,15)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 60 and point_probability > 30:
                points = random.randint(15,20)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 90 and point_probability > 60:
                points = random.randint(20,30)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 95 and point_probability > 90:
                points = random.randint(30,40)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 100 and point_probability > 95:
                points = random.randint(40,50)
                print(self._name + " scored " + str(points) + " points." )
        if self._scoring > 20 and self._scoring <= 40:
            point_probability = random.randint(0, 100)
            if point_probability <= 10:
                points = random.randint(0,12)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 30 and point_probability > 10:
                points = random.randint(12,18)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 60 and point_probability > 30:
                points = random.randint(18,25)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 90 and point_probability > 60:
                points = random.randint(25,32)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 95 and point_probability > 90:
                points = random.randint(32,45)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 97 and point_probability > 95:
                points = random.randint(40,55)
                print(self._name + " scored " + str(points) + " points." )
            else:
                points = random.randint(55,60)
                print(self._name + " scored " + str(points) + " points." )
        if self._scoring > 40 and self._scoring <= 70:
            point_probability = random.randint(0, 100)
            if point_probability <= 10:
                points = random.randint(0,15)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 30 and point_probability > 10:
                points = random.randint(15,20)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 60 and point_probability > 30:
                points = random.randint(20,28)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 90 and point_probability > 60:
                points = random.randint(28,36)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 95 and point_probability > 90:
                points = random.randint(36,50)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability <= 97 and point_probability > 95:
                points = random.randint(50,60)
                print(self._name + " scored " + str(points) + " points." )
            else:
                points = random.randint(60,65)
                print(self._name + " scored " + str(points) + " points." )
        if self._scoring > 90:
            point_probability = random.randint(0, 100)
            if point_probability <= 10:
                points = random.randint(0,16)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability > 10 and point_probability <= 30:
                points = random.randint(16,21)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability > 30 and point_probability <= 60:
                points = random.randint(21,30)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability > 60 and point_probability <= 90:
                points = random.randint(30,40)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability > 90 and point_probability <= 95:
                points = random.randint(40,55)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability > 95 and point_probability <= 97:
                points = random.randint(55,65)
                print(self._name + " scored " + str(points) + " points." )
            if point_probability > 97 and point_probability <= 99:
                points = random.randint(65,81) #RIP Kobe
                print(self._name + " scored " + str(points) + " points." )
            else:
                points = random.randint(81, 110) #Can break Wilt's record
                print(self._name + " scored " + str(points) + " points." )
        if self._rebounding < 20:
            rebound_probability = random.randint(0, 10)
            if rebound_probability <= 2:
                reb = random.randint(0,3)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability <= 5 and rebound_probability > 2:
                reb = 4
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability <=8 and rebound_probability > 5:
                reb = random.randint(3,5)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability > 8:
                reb = random.randint(5,10)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
        if self._rebounding <= 40 and self._rebounding > 20:
            rebound_probability = random.randint(0, 10)
            if rebound_probability <= 2:
                reb = random.randint(0,6)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability <= 5 and rebound_probability > 2:
                reb = 7
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability <=9 and rebound_probability > 5:
                reb = random.randint(7,10)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability > 9:
                reb = random.randint(10,15)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
        if self._rebounding <= 80 and self._rebounding > 40:
            rebound_probability = random.randint(0, 10)
            if rebound_probability <= 2:
                reb = random.randint(0,7)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability <=5 and rebound_probability > 2:
                reb = random.randint(7,10)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability <= 9 and rebound_probability>5:
                reb = random.randint(11,15)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability > 9:
                reb = random.randint(15,20)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
        if self._rebounding > 80:
            rebound_probability = random.randint(0, 10)
            if rebound_probability <= 2:
                reb = random.randint(0,8)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability <=5 and rebound_probability > 2:
                reb = random.randint(8,12)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability < 9 and rebound_probability>5:
                reb = random.randint(13,18)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability == 9:
                reb = random.randint(18,35)
                print(self._name + " grabbed " + str(reb) + " rebounds." )
            if rebound_probability == 10:
                reb = random.randint(20,56) #Can break Wilt's record
                print(self._name + " grabbed " + str(reb) + " rebounds." )
        
        if self._playmaking < 20:
            playmaking = random.randint(0, 100)
            if playmaking < 30:
                assists = random.randint(0,4)
                turnovers = random.randint(0,4)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 50 and playmaking > 30:
                assists = random.randint(4,6)
                turnovers = random.randint(0,6)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 70 and playmaking > 50:
                assists = random.randint(6,8)
                turnovers = random.randint(0,7)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 100 and playmaking > 70:
                assists = random.randint(8,10)
                turnovers = random.randint(0,10)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
        if self._playmaking <= 40 and self._playmaking > 20:
            playmaking = random.randint(0, 100)
            if playmaking < 30:
                assists = random.randint(0,6)
                turnovers = random.randint(0,4)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 50 and playmaking > 30:
                assists = random.randint(6,9)
                turnovers = random.randint(0,8)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 90 and playmaking > 50:
                assists = random.randint(9, 12)
                turnovers = random.randint(0,9)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 100 and playmaking > 90:
                assists = random.randint(12,15)
                turnovers = random.randint(0,15)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
        if self._playmaking <= 80 and self._playmaking > 40:
            playmaking = random.randint(0, 100)
            if playmaking < 30:
                assists = random.randint(0,7)
                turnovers = random.randint(0,3)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 50 and playmaking > 30:
                assists = random.randint(7,10)
                turnovers = random.randint(0,4)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 90 and playmaking > 50:
                assists = random.randint(11, 15)
                turnovers = random.randint(0,6)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 100 and playmaking > 90:
                assists = random.randint(15,18)
                turnovers = random.randint(0,12)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
        if self._playmaking > 80:
            playmaking = random.randint(0, 100)
            if playmaking < 30:
                assists = random.randint(0,6)
                turnovers = random.randint(0,2)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 50 and playmaking > 30:
                assists = random.randint(6,9)
                turnovers = random.randint(0,6)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 90 and playmaking > 50:
                assists = random.randint(9, 12)
                turnovers = random.randint(0,7)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 95 and playmaking > 90:
                assists = random.randint(12,20)
                turnovers = random.randint(0,10)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")
            if playmaking <= 100 and playmaking > 95:
                assists = random.randint(20,31) #Can break Scott Skiles' record
                turnovers = random.randint(0,12)
                print(self._name + " dished " + str(assists) + " assists and committed " + str(turnovers) + " turnovers.")

    #Seeing how defense impacts the game
        if (self._perimeter_defense + self._paint_defense) <= 20:
            self._win_chance += 1
        if (self._perimeter_defense + self._paint_defense) > 20 and (self._perimeter_defense + self._paint_defense) <= 50:
            self._win_chance += 1.25
        if (self._perimeter_defense + self._paint_defense) > 50 and (self._perimeter_defense + self._paint_defense) <= 80:
            self._win_chance += 1.35
        if (self._perimeter_defense + self._paint_defense) > 80 and (self._perimeter_defense + self._paint_defense) <= 90:
            self._win_chance += 1.45
        if (self._perimeter_defense + self._paint_defense) > 90 and (self._perimeter_defense + self._paint_defense) <= 100:
            self._win_chance += 1.55
        if (self._perimeter_defense + self._paint_defense) > 100 and (self._perimeter_defense + self._paint_defense) <= 120:
            self._win_chance += 1.75
        if (self._perimeter_defense + self._paint_defense) > 120:
            self._win_chance += 2
    #Calculating an outcome
        rand = random.randint(0,100)
        if rand < self._win_chance:
            print("You won this game!")
            self._win_chance += 2
            return self._win_chance
        else:
            print("You lost this game!")
            self._win_chance -=2    
            return self._win_chance
              
def main():
    #Example simualtion with Damian Lillard, Superstar PG of the Portland Trail Blazers. First I'm making the object and printing basic values
    Dame = Basketball_Player("Damian Lillard", 0, 74, 80, 195, "PG")
    print("His profession is " + Dame.profession) #Using the class attribute
    print("His name is " + Dame.get_name())
    print("His number is " + str(Dame.get_number()))
    print("His height is " + str(Dame.get_height()) + " inches")
    print("His wingpsan is " + str(Dame.get_wingpsan()) + " inches")
    print("His weight is " + str(Dame.get_weight()) + "lbs")
    print("He plays the " + Dame.get_position() + " position")
    print(Dame.get_attributes_string())
    #Now I'm using the methods defined in the class. The work out method increases fitness, and the run_drills method increases offenive skills. Defense_practice method increases defensive skills, and the run_extensive_drills method increases all attributes.
    Dame.work_out()
    Dame.work_out()
    Dame.run_drills()
    Dame.run_drills()
    Dame.run_drills()
    Dame.defense_practice()
    Dame.run_extensive_drills()
    Dame.run_extensive_drills()
    print()
    #Play_game simulates a game and box score for the player.
    Dame.play_game()
    print()
    Dame.play_game()
    print()
    Dame.play_game()
    #Getting his win chance after these games
    print(Dame.get_win_chance_string())
    print()
    #Going to use setters to cheat and change attributes
    print("Time to cheat and make Dame the GOAT.")
    Dame.set_scoring(100)
    Dame.set_playmaking(100)
    Dame.set_rebounding(100)
    Dame.set_perimeter_defense(100)
    Dame.set_paint_defense(100)
    Dame.set_fitness(100)
    Dame.set_win_chance(100)
    print("Cheating done!")
    #Same thing as before but with a maxed out player.
    print(Dame.get_attributes_string())
    Dame.work_out()
    Dame.work_out()
    Dame.run_drills()
    Dame.run_drills()
    Dame.run_drills()
    Dame.defense_practice()
    Dame.run_extensive_drills()
    Dame.run_extensive_drills()
    print()
    Dame.play_game()
    print()
    Dame.play_game()
    print()
    Dame.play_game()
    print(Dame.get_win_chance_string())
    print()
    print("Time to make a new player to showcase the basic setters! Meet Kevin Durant.")
    #Example simulation with Brooklyn Nets superstar PF KD, starting off with his GSW self.
    KD = Basketball_Player("Kevin Durant", 35, 83, 89, 240, "SF")
    print("His profession is " + KD.profession) #Using the class attribute
    print("His name is " + KD.get_name())
    print("His number is " + str(KD.get_number()))
    print("His height is " + str(KD.get_height()) + " inches")
    print("His wingpsan is " + str(KD.get_wingpsan()) + " inches")
    print("His weight is " + str(KD.get_weight()) + "lbs")
    print("He plays the " + KD.get_position() + " position")
    print(KD.get_attributes_string())
    print("After tearing his achilles on Golden State, KD signed with the Nets, and some of his attributes changed.")
    #Now showcasing the set_position and set_number methods. Feel free to use the others if you want.
    print("His new number is " + str(KD.set_number(7)))
    print("His new position is " + str(KD.set_position("PF")))
    print()
    print("Let's see him play some games after I adjust his skills")
    #Adjusting KD's skills
    KD.set_scoring(35)
    KD.set_rebounding(75)
    KD.set_playmaking(75)
    KD.set_paint_defense(70)
    KD.set_perimeter_defense(65)
    #Attributes set
    KD.play_game()
    print()
    KD.play_game()
    print()
    KD.play_game()

if __name__ == "__main__":
    main()

