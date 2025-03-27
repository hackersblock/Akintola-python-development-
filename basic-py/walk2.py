import random 

def randomm_walk_2(n):
    """Return coordinates after 'n' block random walk."""
    x, y =0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1),(0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

#we can also use the monte carlo rule



for i in range (25):
    walk = randomm_walk_2(10)
    print(walk, "distance from home = ",
         abs(walk[0]) + abs(walk[1]))