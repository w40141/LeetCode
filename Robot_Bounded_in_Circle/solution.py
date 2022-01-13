from typing import Tuple


def isRobotBounded(instructions: str) -> bool:
    def go(now: Tuple[int, int], face: Tuple[int, int]):
        x = now[0] + face[0]
        y = now[1] + face[1]
        return (x, y)

    def turn_left(face: Tuple[int, int]):
        if face == (0, 1):
            return (-1, 0)
        elif face == (-1, 0):
            return (0, -1)
        elif face == (0, -1):
            return (1, 0)
        else:
            return (0, 1)

    def turn_right(face: Tuple[int, int]):
        if face == (0, 1):
            return (1, 0)
        elif face == (1, 0):
            return (0, -1)
        elif face == (0, -1):
            return (-1, 0)
        else:
            return (0, 1)

    now: Tuple[int, int] = (0, 0)
    face: Tuple[int, int] = (0, 1)
    instructions = instructions + instructions[: instructions.find("G") + 1]
    for s in instructions:
        if s == "G":
            now = go(now, face)
        elif s == "L":
            face = turn_left(face)
        else:
            face = turn_right(face)
        print(now)
    return True


s = input()
isRobotBounded(s)
    # ans = 0
    # for s in instructions:
    #     if "L":
    #         ans += 1
    #     elif "R":
    #         ans -= 1
    #     else:
    #         ans += 0
    #
    # if ans:
    #     return True
    # return False
