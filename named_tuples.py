from collections import namedtuple

pres = "Abraham", "Lincoln", "Republican"

print(pres[0], pres[1])

President = namedtuple("President", "first_name last_name party")

pres = President("Abraham", "Lincoln", "Republican")
print(pres[0])
print(pres.first_name, pres.last_name)
