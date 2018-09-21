def funnel(input, target):
  for i in range(len(input)):
    if popped(input, i) == target:
      return True
  return False

def popped(input, index):
  return input[:index] + input[index+1:]

def bonus(input):
  response = []

  url_file = './enable'
  with open(url_file) as file:
    content = [line.strip() for line in file]

  for i in range(len(input)):
    if popped(input, i) in content:
      response.append(popped(input, i))

  return list(set(response))

def bonus_count(input):
  count = 0

  url_file = './enable'
  with open(url_file) as file:
    content = [line.strip() for line in file]

  for i in range(len(input)):
    if popped(input, i) in content:
      count = count + 1

  return count

def bonus2():
  response = []

  url_file = './enable'
  with open(url_file) as file:
    content = [line.strip() for line in file if len(line.strip()) > 5]

  for item in content:
    # print(item, end='  ')
    # print(bonus_count(item))
    if bonus_count(item) == 5:
      response.append(item)
      print(item)
      print(len(response))
    if len(response) >= 28:
      break

if __name__ == "__main__":
  # assert funnel("leave", "eave") == True
  # assert funnel("reset", "rest") == True
  # assert funnel("dragoon", "dragon") == True
  # assert funnel("eave", "leave") == False
  # assert funnel("sleet", "lets") == False
  # assert funnel("skiff", "ski") == False

  # assert set(bonus("dragoon")) == set(["dragon"])
  # assert set(bonus("boats")) == set(["oats", "bats", "bots", "boas", "boat"])
  # assert set(bonus("affidavit")) == set([])

  bonus2()