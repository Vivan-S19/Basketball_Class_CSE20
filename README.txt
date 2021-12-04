This class is a class that represents a basketball player, and simulates a rudimentary level of their lives. Once a player object is creates, 
they can train to get better. The user can also simulate stats and game outcomes with the play_game() method. There are getters and setters available
to access and modify player attributes, and to add realism, players may get injured.

The class variable "profession" just holds the string that describes the profession of the basketball player.
Self._name holds the name of the player. Self._number holds the jersey number. Self._height holds the height in inches. Self._weight holds the weight in lbs.
Self._wingspan holds the wingspan in inches. Self._position holds the player position (PG, SG, SF, PF, or C). The skill attributes self._scoring, self._rebounding 
self._perimeter_defense, self._paint_defense, and self._playmaking hold the player's attribute values. Self._fitness isn't a skill but holds the players fitness, 
which they need to maintain above 50 to play. Self._attributes_list holds all of the skills in a list.S elf._offense_list holds the offensive skills in a list.
Self._defense_list holds the defensive skills in a list. Self._win_chance is set to 50 at first to simulate a .500 team, and can go up or down based on performance.

The getter methods get_name(), get_height(), get_wingspan(), get_number(), get_weight(), get_position(), get_attributes_string(), and get_win_chance_string() don't
take any arguments (outside of self) and simply return the desired value.

The setter methods set_name() and set_position() expect strings that serve as the new name and position of the player. The other setter methods
set_height(), set_wingspan(), set_number(), set_weight(), and set_win_chance_string() expect an integer value to set new specified attributes, though floats
work as well.

The class methods do not require any input (outside of self, meaning they need an object for them to be called on).
The work_out() method increases the players' fitness. However, there is a small chance of injury in which case fitness will be decreased instead.
The run_drills() method increases the players' offensive attributes. However, there is a small chance of injury in which case offensive attributes will be decreased instead.
The defense_practice() method increases the players' defensive attributes. However, there is a small chance of injury in which case defensive attributes will be decreased instead.
The run_extensive_drills() method increases the players' offensive and defensive attributes. However, there is a small chance of injury in which case all attributes will be decreased instead.
The play_game() method simulates a game for the given player. Based on the attributes and fitness and win chance of a player, a game outcome will be calculated. This includes a win/loss result and player box scores.

The demo program simulates the methods and constructor with my 2 favorite NBA players, Damian Lillard and Kevin Durant. It is commented and easy to follow. 
First, a base version of Dame Lillard is created and goes through basic methods and plays games. Next, he is maxed out with setters and he goes through the same 
process with 100 in all stats. Then, a KD player object is created, and then setters change his number and position to represent his change of teams to the Brooklyn Nets.
Then, he also goes through drills and simulates a game.
In order to run the demo program, all the user has to do is press play. If they wish to use more setters to edit KD, create a new player, or play through more games, they may edit the main method to do so.

https://github.com/Vivan-S19/Basketball_Class_CSE20
