# for loop that consist 1-5 ^square

for i in range(1,6):
    print(i**2)

# function divison, a and b , print a/b (if b==0, exception handling)

def divison(a,b):
    if b != 0:
        return a / b
    else:
        print("division by 0 is undefined")

    """
    try:
        res = a / b 
    except ValueError:
        print("division by 0 is undefined")
    """

d = divison(3,4)
print(d)
divison(3,0)

def wordCounter(filename):
    f = open(f'{filename}', "r")
    lines = f.readlines()
    n = 0
    for line in lines:
        n += len(line.strip().split(" "))
    
    return n

kelimesayisi = wordCounter('test.txt')
print(kelimesayisi)