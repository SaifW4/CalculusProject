import matplotlib.pyplot as plt
import numpy as np
import time



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
    print("This program will help you understand how to find limits and their continuity by explaining the concept, testing you and providing examples")
    user_input = input("Do you wish to proceed? (By pressing y, you will be taught the concept of limits and continuity and how to find them. Pressing n will take you to the next step)")
    while user_input != 'n':
        if user_input == 'y':
            print("")
            break


        elif user_input == 'n':
            break
        else:
            print("Invalid input")
            break

    user_input = input("Do you wish to proceed? (By pressing y you will be shown an example. Pressing n will take you to the next step)")
    while user_input != 'n':

        if user_input == 'y':
            print("Q1: Find the limit at x = 1 and determine if there is continuity at that point or not:")
            example_graph_1()
            print("If you take x = 1 from the right (1.0000000001) and from the left (0.9999999999), you will find that")
            print("as x approaches x = 1 from the right, y is equal to 2 and as x approaches x = 1 from the left, y is also equal to 2 ")
            print("Therefore the limit is equal to 2.")
            print("Since the limit from the right is equal to the limit from the left, there is continuity at this point.")
            break
        elif user_input == 'n':
            break


        else:
            print("Invalid input")
            break
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - -")
    user_input = input("Do you wish to proceed? (Press y to see another example. Pressing n will take you to the next step)")
    while user_input != 'n':
       if user_input == 'n':
            break
       elif user_input == 'y':
           print("Q2: Find the limit at x = 2")
           example_graph_2()
           print("If you take x = 2 from the right (2.0000000001) and from the left (1.9999999999), you will find that")
           print(
               "as x approaches x = 2 from the right, y is equal to 2 and as x approaches x = 2 from the left, y is equal to 1 ")
           print("Therefore the limit does not exist.")
           print("Since the limit does not exist, there is no continuity at this point.")
           print("Note that even though the function is not continuous at x = 2, it still has a left-side continuity because f(2) = 1 and the limit from the left is equal to 1")
           break
       else:
           print("Invalid input")
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("The answer structure should be as follows: 'Limit answer (Number)', 'Continuity answer (either Yes or No)'")
    user_input = input("Are you ready to start the quiz? (y if yes and n if no)")
    for i in range(1,6):
        time.sleep(1)
        print(i)

    while user_input != 'n':
        if user_input == 'n':
            break
        elif user_input == 'y':
            print("Answer the following questions based on the following graph. You only have one try. Write DNE if the limit does not exist and/or the continuity does not exist")
            quiz_graph()
            user_answer = input("Q1: What is the limit at x = 1.5 and is there continuity at this point?")
            while user_answer != 432:
                if user_answer == "1, Yes":
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break
            quiz_graph()
            user_answer = input(
                "Q2: What is the limit at x = 3 and is there continuity at this point?")
            while user_answer != 432:
                if user_answer == "DNE, DNE":
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break
            quiz_graph()
            user_answer = input(
                "Q3: What is the limit at x = 4 and is there continuity at this point?")


            while user_answer != 432:
                if user_answer == "3, Yes":
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break
            quiz_graph()
            user_answer = input(
                "Q4: What is the limit at x = 5 and is there continuity at this point?")
            while user_answer != 432:
                if user_answer == 1:
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break
            quiz_graph()
            print("For this question the structure is as follows: 'Limit answer (Number)', 'Continuity answer (either Yes or No), one-side continuity answer (LSC or RSC)' ")
            print("LSC = LEFT-SIDE CONTINUITY")
            print("RSC = RIGHT-SIDE CONTINUITY")
            user_answer = input(
                "Q5: What is the limit at x = 7 and is there continuity at this point? If not, is there a one-side continuity? If there is, what is it?")
            while user_answer != 432:
                if user_answer == 'DNE, no, LSC':
                    print("Correct!")
                    break
                else:
                    print("Incorrect")
                    break

            break


main()




