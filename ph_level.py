ph = int(input("Enter ph value(1-14): "))

if ph>7:
  print("Basic")
elif ph<7:
  print("Acidic")
else:
  print("Neutral")