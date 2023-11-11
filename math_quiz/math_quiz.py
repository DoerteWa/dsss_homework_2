import random


def GetRandomInteger(min, max):
    """
    Returns a random integer between two given values.

    Args:
        min (int): the lower value
        max (int): the higher value

    Returns: 
        int: the random integer between min and max
    """
    return random.randint(min, max)


def GetRandomOperator():
    """
    Returns a random operator: +, - or *.

    Args:
        None
    Returns: 
        str: the random chosen operator of +, - and *.
    """
    return random.choice(['+', '-', '*'])


def CalculateResult(element1, element2, operator):
    """
    Calculates the result of the calculation.

    Args:
        element1: first element of the calculation
        element2: second element of the calculation
        operator: operator for the calculation
    Returns: 
        str: the merged calculation
        int: result of the calculation
    """
    calculation = f"{element1} {operator} {element2}"
    # Calculate result depending on the operator
    if operator == '-': result = element1 - element2
    elif operator == '+': result = element1 + element2
    else: result = element1 * element2
    return calculation, result

def math_quiz():
    """
    Conducts a math quiz game with a specified number of rounds.
    
    The game generates random math problems, prompts the user for answers, 
    and awards points for correct answers. The final score is displayed at the end.

    Args:
        None
    Returns: 
        None
    """

    points = 0 # variable for counting correct answers
    round = 3 # variable for defining how many rounds are played

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(round):
        # Create Calculation with two random integers and a random operator
        element1 = GetRandomInteger(1, 10); element2 = GetRandomInteger(1, 5); operator = GetRandomOperator()
        calculation, result = CalculateResult(element1, element2, operator)

        print(f"\nQuestion: {calculation}")

        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except ValueError:
            print('Input value must be a number. Float is cast to integer')
            useranswer = input("Last Chance. Your answer: ")
            useranswer = int(useranswer)
            
        # Compare the user's answer and the result and award a point when it's correct
        if useranswer == result:
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {points}/{round}")

if __name__ == "__main__":
    math_quiz()
