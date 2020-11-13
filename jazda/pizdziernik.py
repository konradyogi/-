
file = open("conf.txt","r+")
czyt = file.read()

file.close()

tablica = czyt.split("asd")

a = tablica[0]
b = tablica[1]
c = tablica[2]

x = 0

file = open("wpis.txt", "w+")


while x <= int(c):
    file.write(str(a) + " ")
    a, b = b, int(a) + int(b)
    x += 1


file.close()


