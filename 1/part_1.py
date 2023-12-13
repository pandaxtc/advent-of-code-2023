import re

# print(
#   sum(
#     (lambda line:
#       (lambda words={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}:
#         (lambda digits=re.findall(r"(?=(\d|" + "|".join(words.keys()) + r"))", line):
#           (words.get(digits[0]) or int(digits[0])) * 10 + (words.get(digits[-1]) or int(digits[-1]))
#         )()
#       )()
#     )(line)
#     for line in open("input.txt")
#   )
# )

print(
  sum(
    (lambda line:
        (lambda digits=re.findall(r"(?=(\d))", line):
          (int(digits[0])) * 10 + (int(digits[-1]))
        )()
    )(line)
    for line in open("input.txt")
  )
)
