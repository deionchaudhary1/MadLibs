f = open('madlibs.txt','r')
madlibText = f.readlines()
year = input("Enter a year: ")
thing = input("Enter a thing: ")
deathage = input("Enter an old age: ")
age1 = input("Enter a young age: ")
group1 = input("Enter a group of people: ")
game = input("Enter a game: ")
group2 = input("Enter another group of people: ")
place1 = input("Enter a place: ")
animals = input("Enter plural animal: ")
country = input("Enter a country: ")
age2 = input("Enter an age between the old and young age: ")
job = input("Enter a job: ")
place2 = input("Enter another place: ")
noth = input(' ')

for line in madlibText:
  line = line.replace("YEAR", year)
  line = line.replace("THING", thing)
  line = line.replace("DEATHAGE", deathage)
  line = line.replace("AGE", age1)
  line = line.replace("GROUPOFPEOPLE1", group1)
  line = line.replace("GAME", game)
  line = line.replace("GROUPOFPEOPLE2", group2)
  line = line.replace("PLACE1", place1)
  line = line.replace("ANIMALS", animals)
  line = line.replace("COUNTRY", country)
  line = line.replace("AGE2", age2)
  line = line.replace("JOB", job)
  line = line.replace("PLACE2", place2)
  print(line)