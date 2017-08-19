import re
import queue
from warnings import warn

def populate_dictionary(filename, length, banned_filename=""):
  # If the user desides to use banned words
  banned_words = []
  if banned_filename != "":
    banned_fd = open(banned_filename)
    lines = banned_fd.readlines()
    for line in lines:
      if len(line.rstrip()) == length:
        banned_words.append(line.rstrip())
    banned_fd.close()
  # Read in the words from dictionary 
  file = open(filename)
  lines = file.readlines()
  # Populate the dictionary
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == length and word not in banned_words:
      words.append(word)
  file.close()
  return words


def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])


# Requires regex pattern
def build(pattern, words, seen, path):
  return [word for word in words
          if re.search(pattern, word) and word not in seen.keys() and
          word not in path]

# Does not require regex pattern | Faster implementation for bfs
def build_basic(words, visited, current_word):
  neighbors = set()
  for word in words:
    if word not in visited:
      if same(word, current_word) == len(word)-1:
        neighbors.add(word)
  return neighbors


def find(word, words, seen, target, path, outer_fitness=0):
  adjacent = []
  for i in range(len(word)):
    adjacent += build(word[:i] + "." + word[i + 1:], words, seen, adjacent)
  if len(adjacent) == 0:
    return False
  # Sorted in reverse to put best candidate words first
  adjacent = sorted([(same(w, target), w) for w in adjacent], reverse=True)

  # Looks for target word
  for (fitness, item) in adjacent:
    if fitness == len(target) - 1:
      path.append(item)
      return True
    seen[item] = True
  # Otherwise recurses through words in current path
  for (fitness, item) in adjacent:
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


# Add a function so that the module can be callable
def run():
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

  # Used Banned Words File?
  banned_filename = input("Please enter a filename for banned words. (Press enter if not required): ")
  if len(banned_filename) != 0:
    banned_fd = open(banned_filename)
    banned_fd.close()
    banned = True
  else:
    banned = False

  # Generate the word list
  if banned:
    words = populate_dictionary(filename, len(start_word), banned_filename)
  else:
    words = populate_dictionary(filename, len(start_word))
  # Check if the target exists before searching for a path
  if end_word not in words:
    warn("Target word does not exist in the dictionary (You may have banned it?)", UserWarning)
    quit()

  # Short or long path?
  path_option = input("Enter 'y' if you would like to evaluate a mininal path (Press enter if not required): ")
  if path_option.lower() == "y":
    path = short_path(words, start_word, end_word)
    path.append(end_word)
    print(len(path) - 1, path, sep='\t')
  else:
    path = [start_word]
    seen = {start_word: True}
    if find(start_word, words, seen, end_word, path):
      path.append(end_word)
      print(len(path) - 1, path, sep='\t')
    else:
      print("No path found")

# Main
if __name__ == "__main__":
  run()

  