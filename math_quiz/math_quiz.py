import random


def create_random_int(min, max):
    
    """
    returns a random integer between min and max.

        Parameters:
            min(int): the lower border 
            max(int): the higher border

        Returns:
            random integer between min and max
    """

    return random.randint(min, max)


def select_math_operation():

    """
    selects randomly one of the operations additions, subtraction and multiplication

        Parameters:
            None

        Returns:
            string containing the chosen math_operation
    """

    return random.choice(['+', '-', '*'])


def calculate_random_operation(n1, n2, operation):

    """
    creates the math_equation out of two numbers and the operation type

        Parameters:
            n1(int): first number of the equation
            n2(int): second number of the equation
            operation(string): math_operation used for the two numbers
        Returns:
            question(string): math_equation in written form
            result(int): result of the euqation
    """

    question = f"{n1} {operation} {n2}"
    if operation == '+': 
        #if additions was randomly chosen
        result = n1 + n2
    elif operation == '-': 
        #if subtraction was randomly chosen
        result = n1 - n2
    else: 
        #if multiplication was randomly chosen
        result = n1 * n2
    return question, result

def math_quiz():

    """
    interactive math_quiz containing of 3 questions
    provides math euqations for the user and gives feedback about the answers

        Parameters:
            None
        Returns:
            None
    """

    score = 0 #score of the user
    rounds = 3 #nuber of rounds that are played

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(rounds):
        n1 = create_random_int(1, 10) #creates first number of operation 
        n2 = create_random_int(1, 5) #creates second number of operation
        operation = select_math_operation() #chooses operation type

        question, result= calculate_random_operation(n1, n2, operation) #creates random math problem along with the result for it
        print(f"\nQuestion: {question}") #user gets the math operation as question
        
        useranswer = input("Your answer: ") #user is asked to enter the answer and reads input
        try:
            useranswer = int(useranswer) #convert answer to int
        except ValueError:
            print("the input is not valid, the input must be an integer number")

        if useranswer == result: #checks if the answer of the user is correct
            print("Correct! You earned a point.")
            score += 1 #due to correct answer the score is increased by one
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {score}/{rounds}") #return percentage of correct answered questions

if __name__ == "__main__":
    math_quiz()
