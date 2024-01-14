
try:
    with open("e.txt") as f:
      for line in f:
        print(line)
except FileNotFoundError as not_found:
  print("Wrong file or file path")
