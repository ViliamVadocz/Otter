from random import random, randint
from typing import Any, List, Tuple, Callable

from matplotlib.pyplot import plot, show


def random_sign() -> float:
    return 1 if random() > 0.5 else -1


class Tuner:
    """
    Tunes a function's parameters to recreate recorded data.
    """

    def __init__(
        self,
        recorded: Tuple[List[float], List[float]],
        func: Callable[[Any], float],
        variables: List[float],
        apply_factor: float = 0.0001,
    ):
        self.recorded: Tuple[List[float], List[float]] = recorded
        self.func: Callable[[Any], float] = func
        self.variables: List[float] = variables
        self.apply_factor: float = apply_factor
        self.deltas: List[float] = [abs(var) for var in self.variables]

    def graph(self):
        plot(self.recorded[0], self.recorded[1])
        plot(
            self.recorded[0], [self.func(x, *self.variables) for x in self.recorded[0]]
        )
        show()

    def tune(self):
        iter: int = 1
        last_random_deltas: List[float] = [0] * len(self.variables)
        while True:
            random_deltas: List[float] = [
                random_sign() * self.deltas[i] for i in range(len(self.variables))
            ]
            one: List[float] = [
                self.variables[i] - random_deltas[i] for i in range(len(self.variables))
            ]
            two: List[float] = [
                self.variables[i] + random_deltas[i] for i in range(len(self.variables))
            ]
            random_index: int = randint(0, len(self.recorded[0]) - 1)
            if abs(
                self.func(self.recorded[0][random_index], *one)
                - self.recorded[1][random_index]
            ) < abs(
                self.func(self.recorded[0][random_index], *two)
                - self.recorded[1][random_index]
            ):
                self.variables = [
                    self.variables[i] - self.apply_factor * random_deltas[i]
                    for i in range(len(self.variables))
                ]
            else:
                self.variables = [
                    self.variables[i] + self.apply_factor * random_deltas[i]
                    for i in range(len(self.variables))
                ]
            self.deltas = [
                self.deltas[i]
                * (
                    (1 - self.apply_factor)
                    if (random_deltas[i] * last_random_deltas[i] < 0)
                    else 1
                )
                for i in range(len(self.deltas))
            ]
            last_random_deltas = random_deltas
            if all([delta * self.apply_factor < 10 ** -13 for delta in self.deltas]):
                print(str(iter) + ": " + str(self.variables))
                break
            if iter % 10000 == 0:
                print(str(iter) + ": " + str(self.variables))
            iter += 1
