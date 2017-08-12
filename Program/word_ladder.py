import re
import queue
from warnings import warn

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


def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])


def build(pattern, words, seen, path):
  return [word for word in words
          if re.search(pattern, word) and word not in seen.keys() and
          word not in path]

def build_basic(words, visited, current_word):
  neighbors = set()
  for word in words:
    if word not in visited:
      if same(word, current_word) == len(word)-1:
        neighbors.add(word)
  return neighbors


def find(word, words, seen, target, path, outer_fitness=0):
  current_path = []
  for i in range(len(word)):
    current_path += build(word[:i] + "." + word[i + 1:], words, seen, current_path)
  if len(current_path) == 0:
    return False
  # Sorted in reverse to put best candidate words first
  current_path = sorted([(same(w, target), w) for w in current_path], reverse=True)
  # Looks for target word
  for (fitness, item) in current_path:
    if fitness == len(target) - 1:
      path.append(item)
      return True
    seen[item] = True
  # Otherwise recurses through words in current path
  for (fitness, item) in current_path:
    if fitness >= outer_fitness:
      path.append(item)
      if find(item, words, seen, target, path, fitness):
        return True
      path.pop()


def short_path(words, start_word, target_word):
  q = queue.Queue()
  visited = {}
  q.put([start_word])
  while q:
    path = q.get()
    vertex = path[-1]
    if vertex not in visited:
      visited[vertex] = True
    if same(vertex, target_word) == len(target_word)-1:
      return path
    neighbors = build_basic(words, visited, vertex)
    for neighbor in neighbors:
      if neighbor not in visited:
        visited[neighbor] = True
        new_path = list(path)
        new_path.append(neighbor)
        q.put(new_path)


def init():
  # Input and validation
  start_word = input("Please enter staring word: ").lower().rstrip()
  if not start_word.isalpha():
    warn("Input words cannot contain numbers or special characters", UserWarning)
    quit()
  end_word = input("Please enter target word: ").lower().rstrip()
  if not end_word.isalpha():
    warn("Input words cannot contain numbers or special characters", UserWarning)
    quit()
  if start_word == end_word:
    warn("Start and target words cannot be the same", UserWarning)
    quit()
  if len(start_word) != len(end_word):
    warn("Start and target words must be the same length", UserWarning)
    quit()
  return [start_word, end_word]

# Main
if __name__ == "__main__":
  # Get dictionary file name
  filename = input("Please enter dictionary name (without .txt): ")
  filename += ".txt"
  # Check file exists
  file_desc = open(filename)
  file_desc.close()

  # Get user input
  user_input = init()

  # Extract start/end words
  start_word = user_input[0]
  end_word = user_input[1]

  # Generate the word list
  words = populate_dictionary(filename, len(start_word))
  # Check if the target exists before searching for a path
  if end_word not in words:
    warn("Target word does not exist in the dictionary", UserWarning)
    quit()


  path = [start_word]
  seen = {start_word: True}

  path = short_path(words, start_word, end_word)
  path.append(end_word)
  print(path)
  # if find(start_word, words, seen, end_word, path):
  #   path.append(end_word)
  #   print(len(path) - 1, path)
  # else:
  #   print("No path found")