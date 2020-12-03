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
