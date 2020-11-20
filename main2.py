def load_image(filename):
    image = {}
    image["type"] = ''
    image["size"] = []
    image["comment"] = ''
    image["pixels"] = []

    infile = open(filename, "r")
    instr = infile.read().split('\n')
    image["type"] = instr.pop(0)

    if instr[0][0] == '#':
        image["comment"] = instr.pop(0)

    image["size"] = list(map(int, instr.pop(0).split(' ')))

    for row in instr:
        image["pixels"].append(list(map(int, row.split(' '))))
    return image


def generate_square(size, colour):
    image = {}
    image["type"] = "P1"
    image["size"] = [size, size]
    image["comment"] = ''
    image["pixels"] = []

    for row in range(size):
        line = []
        for col in range(size):
            if colour:
                line.append(0)
            else:
                line.append(1)
        image["pixels"].append(line)

    return image


def negative(image):
    for row in range(image["size"][1]):
        # print(image["pixels"][row])
        for col in range(image["size"][0]):
            if image["pixels"][row][col] == 0:
                image["pixels"][row][col] = 1
            else:
                image["pixels"][row][col] = 0

    return image

def generate_cehssboard(size):
    pass

##############################################

def generate_diagonal(size):
    image = {}
    image["type"] = "P1"
    image["size"] = [size, size]
    image["comment"] = ''
    image["pixels"] = []

for row in range(size):
        line = []
        for col in range(size):
            if row == col:
                line.append(1)
            else:
                line.append(0)
        image["pixels"].append(line)


return image

##############################################

def mirror_y(image):
    pass


def mirror_x(image):
    pass


def save_image(filename, image):
    """
        Saves an image to a filename.
    """

    outfile = open(filename, "w+")  # Open a filename in a write mode
    outfile.write(image["type"] + "\n")
    if image["comment"]:
        outfile.write("# " + image["comment"] + "\n")  # Add comment if there is any
    outfile.write(' '.join(list(map(str, image["size"]))) + '\n')   # Change ints to strs and join them with spaces
    for row in image["pixels"]:
        outfile.write(' '.join(list(map(str, row))) + '\n') # Change ints to strs and join them with spaces

# image = generate_square(5, True)
# # image = load_image("test.pgm")
# save_image("white.pgm", image)
# image = generate_square(5, False)
# # image = load_image("test.pgm")
# save_image("black.pgm", image)

image = load_image("arrow.pgm")
image = negative(image)
save_image("inverted_arrow.pgm", image)
