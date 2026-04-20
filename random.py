import random


def random_str():
    sins = ('Pride', 'Greed', 'Lust', 'Envy', 'Gluttony', 'Wrath', 'Sloth')
    n = random.randint(1, 7)
    s = sins[n-1]
    return (s)


print(random_str())
