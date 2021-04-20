# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'


# Part 1: Greet 
def greet(name, greeting='Hello, <name>!'):
    if greeting.endswith('<name>!'):
        greeting = greeting[0:-8]
    return(f'{greeting} {name}!')

# Part 2: Force 
def force(mass, body='earth'):
    planet_gravity={
        'sun':  274,
        'jupiter':  24.9,
        'neptune':  11.2,
        'saturn':  10.4,
        'earth':  9.8,
        'uranus':  8.9,
        'venus':  8.9,
        'mars':  3.7,
        'mercury':  3.7,
        'moon':  1.6,
        'pluto':  0.6
        }
    return mass * planet_gravity[body]
    


#Part 3: Gravity
def pull(m1, m2,d):
    G=6.674*(10**-11)
    return G*((m1*m2) / d ** 2)
