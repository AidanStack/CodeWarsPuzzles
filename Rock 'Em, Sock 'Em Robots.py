# You and your friends have been battling it out with your Rock 'Em, Sock 'Em robots, but things have gotten a little
# boring.You've each decided to add some amazing new features to your robot and automate them to battle to the death.
#
# Each robot will be represented by an object.You will be given two robot objects, and an object of tactics and how much
# damage they produce.Each robot will have a name, hit points, speed, and then a list of battle tacitcs they are to
# perform in order.Whichever robot has the best speed, will attack first with one battle tactic.
#
# Your job is to decide who wins.
#
# Example:
#
# robot_1 = {
#     "name": "Rocky",
#     "health": 100,
#     "speed": 20,
#     "tactics": ["punch", "punch", "laser", "missile"]
# }
# robot_2 = {
#     "name": "Missile Bob",
#     "health": 100,
#     "speed": 21,
#     "tactics": ["missile", "missile", "missile", "missile"]
# }
# tactics = {
#     "punch": 20,
#     "laser": 30,
#     "missile": 35
# }
# fight(robot_1, robot_2, tactics) -> "Missile Bob has won the fight."

def fight(robot_1, robot_2, tactics):
    if len(robot_2['tactics']) == 0 and len(robot_2['tactics']) > 0:
        return robot_1['name'] + ' has won the fight.'
    if len(robot_1['tactics']) == 0 and len(robot_2['tactics']) > 0:
        return robot_2['name'] + ' has won the fight.'

    fastest_robo = 1
    if robot_2['speed'] > robot_1['speed']:
        fastest_robo = 2

    round = 0

    while robot_1['health'] > 0 and robot_2['health'] > 0 and round < len(robot_1['tactics']):
        if fastest_robo == 1:
            robot_2['health'] = robot_2['health'] - tactics[robot_1['tactics'][round]]
            if robot_2['health'] <= 0:
                return robot_1['name'] + ' has won the fight.'
            robot_1['health'] = robot_1['health'] - tactics[robot_2['tactics'][round]]
            if robot_1['health'] <= 0:
                return robot_2['name'] + ' has won the fight.'
            round += 1

        elif fastest_robo == 2:
            robot_1['health'] = robot_1['health'] - tactics[robot_2['tactics'][round]]
            if robot_1['health'] <= 0:
                return robot_2['name'] + ' has won the fight.'
            robot_2['health'] = robot_2['health'] - tactics[robot_1['tactics'][round]]
            if robot_2['health'] <= 0:
                return robot_1['name'] + ' has won the fight.'
            round += 1

    if robot_1['health'] == robot_2['health']:
        return 'The fight was a draw.'

    if robot_1['health'] > robot_2['health']:
        return robot_1['name'] + ' has won the fight.'

    else:
        return robot_2['name'] + ' has won the fight.'