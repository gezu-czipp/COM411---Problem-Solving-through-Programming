print("What is your name?")
n = input()
#

if len(n) > 9:
  print("You have a very loooong name!")
  print("Your name contains {} letters". format(len(n)))
elif len(n) > 6:
  print("Your name is a bit long. Consider a nickname")
elif len(n) < 3:
  print("Your name is veeeery short")
else:
  print("Your name is quite okay")
print("This is the END of the program!")