# -*- coding: utf-8 -*-

while True:
  try:
    words, lines_page, characters_line = [int(x) for x in input().split()]
    phrase = list(input().split())
    characters, lines, pages = len(phrase.pop(0)), 1, 1
    for word in phrase:
      if (characters + len(word) + 1 <= characters_line):
        characters += len(word) + 1
      else:
        characters = len(word)
        lines += 1
        if lines > lines_page:
          pages += 1
          lines = 1
    print(pages)
  except EOFError:
    break
