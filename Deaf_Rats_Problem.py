#Story
#The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

#But some of the rats are deaf and are going the wrong way!

#Kata Task
#How many deaf rats are there?

#Legend
#P = The Pied Piper
#O~ = Rat going left
#~O = Rat going right
#Example
#ex1 ~O~O~O~O P has 0 deaf rats
#ex2 P O~ O~ ~O O~ has 1 deaf rat
#ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

def count_deaf_rats(town):
    num_of_deaf_rats = 0

    town = town.replace(' ', '')

    if town[0] != 'P' and town[-1] != 'P':

        town = town.split('P')

        rats_left_of_piper = town[0]
        rats_right_of_piper = town[-1]

        left_rats = []
        right_rats = []

        index = 0
        for i in range(int(len(rats_left_of_piper) / 2)):
            left_rats.append(rats_left_of_piper[index] + rats_left_of_piper[index + 1])
            index += 2

        index = 0
        for i in range(int(len(rats_right_of_piper) / 2)):
            right_rats.append(rats_right_of_piper[index] + rats_right_of_piper[index + 1])
            index += 2

        num_of_deaf_rats += left_rats.count('O~')
        num_of_deaf_rats += right_rats.count('~O')

        return num_of_deaf_rats

    piper_index = town.index('P')

    town = town.replace('P', '')

    rat_list = []

    index = 0

    for i in range(int(len(town) / 2)):
        rat_list.append(town[index] + town[index + 1])
        index += 2

    if piper_index == 0:
        num_of_deaf_rats += rat_list.count('~O')

    if piper_index == len(town):
        num_of_deaf_rats += rat_list.count('O~')

    return num_of_deaf_rats