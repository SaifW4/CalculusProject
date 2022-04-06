import matplotlib.pyplot as plt
import numpy as np



def example_graph_1():
    x_axis =[-1,0,1,2,3,4,5,6]
    y_axis =[1,0,2,2,2,1,0.5,0]
    plt.title("This is an example graph")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x_axis,y_axis, color= "blue")
    plt.show()

def example_graph_2():
    x_axis =[0,1,2,2,3,5,6]
    y_axis =[0,1,1,2,3,0,0]
    plt.title("This is an example graph")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x_axis,y_axis, color= "blue")
    plt.show()


#def quiz_graph():
 #   x_axis =
  #  y_axis =

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

    user_input = input("Do you wish to proceed? (By pressing y you will be shown an example. Pressing n will take you to the next step)")
    while user_input != 'n':

        if user_input == 'y':
            print("Q1: Find the limit at x = 1")
            example_graph_1()
            print("If you take x = 1 from the right (1.0000000001) and from the left (0.9999999999), you will find that")
            print("as x approaches x = 1 from the right, y is equal to 2 and as x approaches x = 1 from the left, y is also equal to 2 ")
            print("Therefore the limit is equal to 2.")
            break
        elif user_input == 'n':
            break


        else:
            print("Invalid input")
    user_input = input("Do you wish to proceed? (Press y to see another example. Pressing n will take you to the next step)")
    while user_input != 'n':
       if user_input == 'n':
            break
       elif user_input == 'y':
           print("Q2: Find the limit at x = 2")
           example_graph_2()
           print("If you take x = 2 from the right (2.0000000001) and from the left (1.9999999999), you will find that")
           print(
               "as x approaches x = 2 from the right, y is equal to 2 and as x approaches x = 2 from the left, y is also equal to 2 ")
           print("Therefore the limit is equal to 2.")
           break
       else:
           print("Invalid input")

main()




