#!/usr/bin/env python
limits = {"red": 12, "green": 13, "blue": 14}


def game_possible(games):
    games_list = [pair.strip().split(",") for pair in games.split(";")]
    is_possible = True
    for game in games_list:
        pairs = {pair.split()[1]: int(pair.split()[0]) for pair in game}
        if not possible(pairs):
            is_possible = False
    return is_possible


def possible(totals):
    is_possible = True
    for color, limit in limits.items():
        try:
            if totals[color] > limit:
                is_possible = False
        except KeyError:
            pass
    return is_possible


def get_power_of_fewest(games):
    highest_power = {"red": 0, "green": 0, "blue": 0}
    games_list = [pair.strip().split(",") for pair in games.split(";")]
    for game in games_list:
        pairs = {pair.split()[1]: int(pair.split()[0]) for pair in game}
        for color, count in pairs.items():
            if highest_power[color] < count:
                highest_power[color] = count
    result = 1
    for number in highest_power.values():
        if number:
            result *= number
    return result


def main():
    with open("day2", "r") as file:
        lines = file.readlines()

    sum_ids = 0
    for line in lines:
        game, games = line.split(":")
        game_id = game.split()[-1]
        if game_possible(games):
            sum_ids += int(game_id)
    print(sum_ids)

    total_powers = 0
    for line in lines:
        _, games = line.split(":")
        total_powers += get_power_of_fewest(games)

    print(total_powers)


if __name__ == "__main__":
    main()
