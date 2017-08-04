import re


def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])


def build(pattern, words, seen, path):
  return [word for word in words
          if re.search(pattern, word) and word not in seen.keys() and
          word not in path]


def find(word, words, seen, target, path):
  current_path = []
  for i in range(len(word)):
    current_path += build(word[:i] + "." + word[i + 1:], words, seen, current_path)
  if len(current_path) == 0:
    return False
  current_path = sorted([(same(w, target), w) for w in current_path])
  for (match, item) in current_path:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in current_path:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()


def populate_dictionary(filename, length):
  fname = "dictionary.txt"
  file = open(fname)
  lines = file.readlines()
  # Populate the dictionary
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == length:
      words.append(word)
  file.close()
  return words


# Main
filename = input("Please enter dictionary name (without .txt): ")
filename += ".txt"
# Check filename
file_desc = open(filename)
file_desc.close()

# Input and validation
start_word = input("Please enter staring word: ").lower().rstrip()
if not start_word.isalpha():
  print("Input words cannot contain numbers or special characters")
  quit()
end_word = input("Please enter target word: ").lower().rstrip()
if not end_word.isalpha():
  print("Input words cannot contain numbers or special characters")
  quit()
if start_word is end_word:
  print("Start and target words cannot be the same")
  quit()
if len(start_word) != len(end_word):
  print("Start and target words must be the same length")
  quit()

words = populate_dictionary(filename, len(start_word))
# Check if the target exists before searching for a path
if end_word not in words:
  print("Target word does not exist in the dictionary")
  quit()

path = [start_word]
seen = {start_word: True}
if find(start_word, words, seen, end_word, path):
  path.append(end_word)
  print(len(path) - 1, path)
else:
  print("No path found")
