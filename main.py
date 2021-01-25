# I understand it's messy but the exercise required a single executable piece of code rather than an entire repo, otherwise I would have split it up.
# For details of the task check the README file

import math

# a single attack turn for white walkers army, returns damage to seven kingdoms army along with winner info if the battle is over
def white_attack_turn(white_forces, seven_forces, battle_end, winner):
  remaining_attack = white_forces[0]*50 + white_forces[1]
  print('attacking side remaining attack:', remaining_attack)
  num_dragons = seven_forces[0]
  num_troops = seven_forces[1]

  # Attack living dragons first
  if num_dragons > 0:
    # enough attack points to wipe out remaining dragons and move onto infantry
    if num_dragons < remaining_attack/600:
      remaining_attack -= num_dragons*600
      dragons_killed = num_dragons
      num_dragons = 0
    # not enough attack points to wipe out remaining dragons
    else:
      dragons_killed = math.floor(remaining_attack/600)
      num_dragons -= dragons_killed
      remaining_attack -= dragons_killed*600

  # for info printing purposes
  elif num_dragons == 0:
    dragons_killed = 0

  # left over attack points used on remaining infantry
  troops_killed = math.floor(remaining_attack/2)
  num_troops -= troops_killed
  
  print('dragons killed:', dragons_killed)
  print('infantry killed:', troops_killed, '\n')

  # battle-end conditions
  if num_dragons == 0 and num_troops <= 0:
    battle_end = True
    winner = 'White Walker Army'

  return [num_dragons, num_troops], battle_end, winner

# a single attack turn for seven kingdoms army, returns damage to white walkers army along with winner info if the battle is over
def seven_attack_turn(white_forces, seven_forces, battle_end, winner):
  remaining_attack = seven_forces[0]*600 + seven_forces[1]*2
  print('attacking side remaining attack:', remaining_attack)
  num_wl = white_forces[0]
  num_ww = white_forces[1]

  # Attack living wl (White Lords) first
  if num_wl > 0:
    # enough attack points to wipe out remaining wl and move onto ww (white walkers)
    if remaining_attack > num_wl*100:
      remaining_attack -= num_wl*100
      wl_killed = num_wl
      num_wl = 0
    # not enough attack points to wipe out remaining wl
    else:
      wl_killed = math.floor(remaining_attack/100)
      num_wl -= wl_killed
      remaining_attack -= wl_killed*100
  
  # for info printing purposes
  elif num_wl == 0:
    wl_killed = 0

  # left over attack points used on remaining ww
  ww_killed = math.floor(remaining_attack/3)
  num_ww -= ww_killed

  print('wl killed:', wl_killed)
  print('ww killed', ww_killed, '\n')

  # battle-end conditions
  if num_wl == 0 and num_ww <= 0:
    battle_end = True
    winner = 'Seven Kingdom Army'

  return [num_wl, num_ww], battle_end, winner

def westeros_battle(no_of_dragons, no_of_white_lords, first_strike_army_name):
  # input checking
  if no_of_dragons < 0 or no_of_white_lords < 0:
    return 'Invalid parameter provided'

  # assigning inputs to data structures my functions expect and initialising variables
  white_forces = [no_of_white_lords, 10000]
  seven_forces = [no_of_dragons, 5000]
  battle_end = False
  winner = None
  attacking_side = first_strike_army_name
  turns = 0

  # setting loop to alternate between army's attacks, and setting it to end once battle is over
  while battle_end == False:

    if attacking_side == 'White Walker Army':
      print('White Walker Army attacks', '\n')
      turns += 1
      
      # finding remaining seven kingdom army forces after white walker attack
      seven_forces, battle_end, winner = white_attack_turn(white_forces, seven_forces, battle_end, winner)
      print('White Forces', white_forces)
      print('Seven Forces', seven_forces, '\n', '\n', '-'*45, '\n')
      # Possible for both sides to have one infantry remaining causing an infinite loop since neither member from each side can kill the other
      if white_forces == [0,1] and seven_forces == [0,1]:
        winner = 'draw'
        battle_end = True
      attacking_side = 'Seven Kingdom Army'

    elif attacking_side == 'Seven Kingdom Army':
      print('Seven Kingdom Army attacks', '\n')
      turns += 1

      # finding remaining white walker army forces after seven kingdom attack
      white_forces, battle_end, winner = seven_attack_turn(white_forces, seven_forces, battle_end, winner)
      print('White Forces', white_forces)
      print('Seven Forces', seven_forces, '\n', '\n', '-'*45, '\n')
      if white_forces == [0,1] and seven_forces == [0,1]:
        winner = 'draw'
        battle_end = True
      attacking_side = 'White Walker Army'

  # formatted result 
  return str(winner)+'|'+str(turns)

class Solution:

  def run(self, first_strike_army_name, no_of_dragons, no_of_white_lords):
    # running the battle function to start the simulation return the result
    result = westeros_battle(no_of_dragons, no_of_white_lords, first_strike_army_name)
    return result
