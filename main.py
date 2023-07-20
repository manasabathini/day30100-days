print("30 Days Down- what do you think")
print()
for i in range(1,31):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"you thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()