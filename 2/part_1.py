import re

game_re = re.compile(r"Game (\d+):")
draws_re = re.compile(r"(?:(\d+) (blue|red|green))")

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

game_id_sum = 0

for line in open("input.txt"):
    game_id = game_re.match(line)[1]
    draws = line.split(";")
    is_bad = False
    for draw in draws:
        print(game_id, draws_re.findall(draw))
        for num, color in draws_re.findall(draw):
            if int(num) > LIMITS[color]:
                print(game_id)
                is_bad = True
                break
        if is_bad:
            break

    if not is_bad:
        game_id_sum += int(game_id)

print(game_id_sum)
