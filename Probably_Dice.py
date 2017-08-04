import itertools

def probability(dice_number, sides, target):
    prob = {}
    points = [ sum(p) for p in itertools.product(range(1,sides+1), repeat = dice_number) ]
    for k, g in itertools.groupby(sorted(points)):
        prob[k] = len(list(g))
    print prob[target]

probability(10, 10, 50)
