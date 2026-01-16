def get_age(age: str) -> int:
    return int(age.split()[0])


#Solução mais performática
def get_age(age: str) -> int:
    return int(age[0])