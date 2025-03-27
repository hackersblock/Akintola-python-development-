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
number_of_walks = 10 000

for walk_length in range(1, 31):
    no_transport = 0 #number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x, y) = randomm_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 5:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print('walk size = ', walk_length,
    '/ % of no transport = ', 100*no_transport_percentage)