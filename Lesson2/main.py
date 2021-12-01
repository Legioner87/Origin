string = ["The quick brown fox jumps over the lazy dog"]
print(string)
#2
anystring = ["lol", True, None, 111, 22.22, ["", 42], []]
print(anystring)
for elem in anystring:
    print(elem)
    print("")
#3

my_dict = {
    1: "one",
    "1": "one",
    (1, 2): "one, two"
    }


print(my_dict)
my_dict["numbers"] = list(range(0, 100))
print(my_dict)
print ("")
#4

def squared():
    for i in range(0, 10):
        if i % 10 != 0:
            print(i * i, end="\t")
squared()
print ("")
#5
a = 2
b = "balls"
print("I have", a,"big", b)

#6
d1 = dict()
d2 = {}

#7 another method
def generate_dict(number):
    d= {}
    for i in range(1,number+1):
        d[i] = (i ** 2,i ** 2,i ** 2)
    return d
print(generate_dict(10))