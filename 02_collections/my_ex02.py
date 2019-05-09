name = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
for i, n in enumerate(name):
    if n == "Angy":
        print("{0}.My name is {1}".format(i+1,n))
    else:
        print("{0}.{1} is my classmate".format(i+1,n))
    