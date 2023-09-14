from typing import List, Dict
import copy
import random


# Consider using the modules imported above.


class Hat:
    def __init__(self, **colours: str) -> None:
        self.contents = []
        for colour, count in colours.items():
            self.contents.extend([colour] * int(count))

    def draw(self, balls: int) -> List[str]:
        drawn_balls = []
        if balls > len(self.contents):
            drawn_balls = copy.deepcopy(self.contents)
            self.contents = []
        else:
            while balls != 0:
                index = random.randrange(0, len(self.contents))
                drawn_ball = self.contents[index]
                drawn_balls.append(drawn_ball)
                self.contents.remove(drawn_ball)
                balls -= 1

        return drawn_balls


def experiment(hat: Hat, expected_balls: Dict[str, int], num_balls_drawn: int,
               num_experiments: int) -> float:
    num_expected_result = 0
    experiment_count = 0

    while experiment_count < num_experiments:
        hat_copy = copy.deepcopy(hat)
        drawn_balls = convert_drawn_balls(hat_copy.draw(num_balls_drawn))

        if is_subset(expected_balls, drawn_balls):
            num_expected_result += 1
        experiment_count += 1

    probability = num_expected_result / num_experiments
    return probability


def convert_drawn_balls(balls: List[str]) -> Dict[str, int]:
    return {ball: balls.count(ball) for ball in balls}


def is_subset(dict1: Dict[str, int], dict2: Dict[str, int]) -> bool:
    if len(dict1) > len(dict2):
        return False
    else:
        return all(count <= dict2.get(key, 0) for key, count in dict1.items())
