def age_assignment(*args, **kwargs):
    names_ages = {}
    for el in args:
        names_ages[el] = 0
    for k, v in kwargs.items():
        for k1, v1 in names_ages.items():
            if k1[0] == k:
                names_ages[k1] += v
    return names_ages


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))