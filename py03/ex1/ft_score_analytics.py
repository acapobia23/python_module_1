import sys

class ScoreError(Exception):
    def __init__(self, message="Unknown score error"):
        super().__init__(message)


class ScoreInputError(ScoreError):
    def __init__(self, message="No scores provided. Usage:"\
                "python3 ft_score_analytics.py <score1> <score2> ..."):
        super().__init__(message)


class InvalidParameterError(ScoreError):
    def __init__(self, message="Invalid parameter:"):
        super().__init__(message)


def list_init(argv: list) -> list:
    numbers= []
    i = 0
    while i < len(argv):
        try:
            num = int(argv[i])
            numbers.append(num)
        except ValueError as e:
            print("Invalid parameter:", argv[i])
        i += 1
    if not numbers:
        raise ScoreInputError()
    return numbers


def argv_init(argv: list) -> list:
    if len(argv) <= 1:
        raise ScoreInputError()
    return argv[1:]

def score_players()-> int:
    nums = []
    print("=== Player Score Analytics ===")
    try:
        argv = argv_init(sys.argv)
        nums = list_init(argv)
    except ScoreInputError as e:
        print(e)
        return 1
    
    tot = len(nums)
    somma = sum(nums)
    print("Scores processed:", nums)
    print("Total players:", tot)
    print("Total score:", somma)
    print("Average score:", somma / tot)
    print("High score:", max(nums))
    print("Low score:", min(nums))
    print("Range score:", max(nums) - min(nums))

if __name__ == "__main__":
    score_players()
    print()