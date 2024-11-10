import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between `min_value` and `max_value` (inclusive).

    Args:
    - min_value (int): The lower bound of the random number.
    - max_value (int): The upper bound of the random number.

    Returns:
    - int: A random integer between `min_value` and `max_value`.
     """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Randomly selects one of the operators: '+', '-', or '*'.

    Returns:
    - str: A randomly selected operator.
    """
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer(n1, n2, operator):
    """
    Generates a math problem as a string and calculates the answer based on the operator.

    Args:
    - n1 (int): The first number in the math problem.
    - n2 (int): The second number in the math problem.
    - operator (str): The operator to use in the math problem ('+', '-', or '*').

    Returns:
    - tuple: A tuple where the first element is the math problem as a string, 
             and the second element is the calculated answer (int).
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    return problem, answer


def math_quiz():
    """
    The main function to run the Math Quiz game. The player is presented with 5 questions.
    The player must enter the correct answer to earn points.
    """
    score = 0
    total_questions = 5  # Total number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        try:
            # Generate random numbers and operator
            num1 = generate_random_integer(1, 10)
            num2 = generate_random_integer(1, 5)  # The second number is between 1 and 5
            operator = generate_random_operator()

            # Generate problem and answer
            problem, correct_answer = generate_problem_and_answer(num1, num2, operator)

            # Display the problem to the user
            print(f"\nQuestion: {problem}")

            # Get user's answer and handle invalid input
            user_answer = input("Your answer: ")

            # Convert user input to integer and check if valid
            try:
                user_answer = int(user_answer)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue  # Skip to the next question if input is invalid

            # Check if the user's answer is correct
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")

        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop if an unexpected error occurs

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()

