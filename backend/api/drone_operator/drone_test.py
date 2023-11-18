import random

LARGE_CAP = 8
MEDIUM_CAP = 4
SMALL_CAP = 1

def num_drones(cone_count):
    curr_cap = 0
    drone_list = []
    large = ['Large' for i in range(0, random.randint(0, 3))]
    med = ['Med' for i in range(0, random.randint(0, 3))]
    small = ["small" for i in range(0, random.randint(0, 3))]



def get_max(cone_count, large, med, small, drone_list):
    done = False;
    while not done:
        if cone_count > LARGE_CAP:
            if len(large) > 0:
                drone_list.append("Large")
                cone_count -= LARGE_CAP;    
        elif cone_count > MEDIUM_CAP:
            if len(med) > 0:
                drone_list.append()
                

'''
Num Drones(cone_count, small, med, large)
    drone_list = []
    cone_count = drones_by_max(cone count, small, med, large, drone_list)
    cone_count = drones_by_min(cone_count, small, med, large, drone_list)



'''