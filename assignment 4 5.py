def generate_squares_list():
    squares_list = []
    for number in range(1,11):
        squarenum = number**2
        squares_list.append(squarenum)
    return squares_list
def generate_cubes_list():
    cubes_list = []
    for number in range(1,11):
        cubenum = number**3
        cubes_list.append(cubenum)
    return cubes_list

squares_list = generate_squares_list()
cubes_list = generate_cubes_list()
print(f'The squares of numbers 1-10 are:{squares_list}.')
print(f'The cubes of numbers 1-10 are:{cubes_list}.')
