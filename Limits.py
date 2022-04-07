import matplotlib.pyplot as plt
import numpy as np



def limits_cont_teach():
    print("Limit is defined as the value a function approaches the output for the given input value.")
    print("In order to find a limit, you need to check the right side and left side of the input value given.")
    print("Lim (f(x)) x -> a")
    print("If the right side is equal to the left side, then the limit does exist and is the value found in both sides")
    print("lim (f(x)) x -> a^+ = lim (f(x)) x -> a^- ")
    print("However, If the sides aren't equal to each other, then the limit does not exist.")
    print("lim (f(x)) x -> a^+ != lim (f(x)) x -> a^- ")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("A function is continuous if the following conditions are met:")
    print("1- f(x) is defined")
    print("2- The limit exists")
    print("3- Limit = f(x)")
    print("Note that there could be a one-side continuity which means that even if a function is not continuous at a certain point, if either the right side or the left side is equal to f(x)")
    print("Then it is called a one-side continuity and its named depending on which side is equal to f(x)")
    print("Right-side continuity if f(x) = Lim(f(x)) x->a^+")
    print("Left-side continuity if f(x) = Lim(f(x)) x->a^-")


def example_graph_1():
    x_axis =[-1,0,1,2,3,4,5,6]
    y_axis =[1,0,2,2,2,1,0.5,0]
    plt.title("Example graph")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x_axis,y_axis, color= "blue")
    plt.show()

def example_graph_2():
    x_axis =[0,1,2,2,3,5,6]
    y_axis =[0,1,1,2,3,0,0]
    plt.title("Example graph")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x_axis,y_axis, color= "blue")
    plt.show()

def quiz_graph():
    x_axis = [1,1,3,3,4,5,6,7]
    y_axis = [0,1,1,3,3,2,0.5,0]
    plt.title("f(x)")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x_axis, y_axis, color="red")
    plt.show()

def main():
    print("Knowing how to find limits is quite important in calculus as you can find"
          " where a function is going at a certain point even if the function isn't defined at that point!")
    print("You can also find out if a function is continuous or not by using limits.")
    print("-- -- -- -- -- - - - -- -- -- -- --")
    print("This program will help you understand how to find limits and continuity.")
    user_input = input("Do you wish to proceed? (By pressing y, an explanation for limits and continuity will appear. Pressing n will take you to the next step)")

    while user_input != 'n':
        if user_input == 'y':
            limits_cont_teach()
            break
        elif user_input =='n':
            break
        else:
            print("Invalid input")
        user_input = input(
            "Do you wish to proceed? (By pressing y, you will be taught the concept of limits and continuity and how to find them. Pressing n will take you to the next step)")

    user_input = input("Do you wish to proceed? (By pressing y you will be shown an example. Pressing n will take you to the next step)")
    while user_input != 'n':
        if user_input == 'y':
            print("Q1: Find the limit at x = 1 and determine if there is continuity at that point or not:")
            example_graph_1()
            print("If you take x = 1 from the right (1.0000000001) and from the left (0.9999999999), you will find that")
            print("as x approaches x = 1 from the right, y is equal to 2 and as x approaches x = 1 from the left, y is also equal to 2 ")
            print("Therefore the limit is equal to 2.")
            print("Since f(x) is defined, the limit exists and f(x) is equal to the limit, there is continuity at this point.")
            break
        elif user_input =='n':
            break
        else:
            input("Invalid input")
        user_input = input(
            "Do you wish to proceed? (By pressing y you will be shown an example. Pressing n will take you to the next step)")
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - -")
    user_input = input("Do you wish to proceed? (Press y to see another example. Pressing anything else will take you to the next step)")
    while user_input != 'n':
       if user_input == 'y':
           print("Q2: Find the limit at x = 2")
           example_graph_2()
           print("If you take x = 2 from the right (2.0000000001) and from the left (1.9999999999), you will find that")
           print(
               "as x approaches x = 2 from the right, y is equal to 2 and as x approaches x = 2 from the left, y is equal to 1 ")
           print("Therefore the limit does not exist.")
           print("Since the limit does not exist, there is no continuity at this point.")
           print("Note that even though the function is not continuous at x = 2, it still has a left-side continuity because f(2) = 1 and the limit from the left is equal to 1")
           break
       elif user_input == 'n':
           break
       else:
           print("Invalid input")
       user_input = input(
           "Do you wish to proceed? (Press y to see another example. Pressing anything else will take you to the next step)")
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("The answer structure should be as follows: 'Limit answer (Number)', 'Continuity answer (either Yes or No)'")
    print("Please save the graph figure in order to have it always displayed next to the questions.")
    answers = []
    user_input = input("Are you ready to start the quiz? (y if yes and n if no)")
    while user_input != 'n':
        if user_input == 'n':
            break
        elif user_input == 'y':
            print("Answer the following questions based on the following graph. You only have one try. Write DNE if the limit does not exist and/or the continuity does not exist")
            quiz_graph()
            user_answer1 = input("Q1: What is the limit at x = 1.5 and is there continuity at this point?")

            while user_answer1 != 432:
                if user_answer1 == "1, Yes":
                    answers.append('Q1: 1, Yes')
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break
            quiz_graph()
            user_answer2 = input(
                "Q2: What is the limit at x = 3 and is there continuity at this point?")

            while user_answer2 != 432:
                if user_answer2 == "DNE, DNE":
                    answers.append("Q2: DNE, DNE")
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break
            quiz_graph()
            user_answer3 = input(
                "Q3: What is the limit at x = 4 and is there continuity at this point?")


            while user_answer3 != 432:
                if user_answer3 == "3, Yes":
                    answers.append("Q3: 3, Yes")
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break
            quiz_graph()
            user_answer4 = input(
                "Q4: What is the limit at x = 5 and is there continuity at this point?")

            while user_answer4 != 432:
                if user_answer4 == '2, Yes':
                    answers.append('Q4: 2, Yes')
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break
            quiz_graph()
            print("For this question the structure is as follows: 'Limit answer (Number)', 'Continuity answer (either Yes or No), one-side continuity answer (LSC or RSC)' ")
            print("LSC = LEFT-SIDE CONTINUITY")
            print("RSC = RIGHT-SIDE CONTINUITY")
            user_answer5 = input(
                "Q5: What is the limit at x = 7 and is there continuity at this point? If not, is there a one-side continuity? If there is, what is it?")

            while user_answer5 != 432:
                if user_answer5 == 'DNE, No, LSC':
                    answers.append('Q5: DNE, No, LSC')
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break


        else:
            print("Invalid input")
            user_input = input("Are you ready to start the quiz? (y if yes and n if no)")
        break

    print("These are the questions that you got right:", answers)
    for i in range(0,3):
        print("-- -- -- -- -- -- -- -- -- -- -- -- -- --")
    print("I genuinely hope that you found this program helpful and useful and I hope that your knowledge in terms of limits and continuity is now better!")

main()




