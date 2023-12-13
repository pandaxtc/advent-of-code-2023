import math
import re

game_re = re.compile(r"Game (\d+):")
draws_re = re.compile(r"(?:(\d+) (blue|red|green))")
game_power_sum = 0

for line in open("input.txt"):
    game_id = game_re.match(line)[1]
    draws = line.split(";")

    max_per_color = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for draw in draws:
        for num, color in draws_re.findall(draw):
            if int(num) > max_per_color[color]:
                max_per_color[color] = int(num)

    game_power_sum += math.prod(max_per_color.values())

print(game_power_sum)
