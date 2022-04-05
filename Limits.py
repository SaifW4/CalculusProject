import matplotlib.pyplot as plt
import numpy as np



def example_graph():
    x_axis =[-1,0,1,2,3,4,5,6]
    y_axis =[1,0,2,2,2,1,0.5,0]
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
    print("This program will help you understand how to find limits and their continuity by testing you and providing examples")

    user_input = input("Do you wish to proceed? (This will show you an example. Press y to proceed and n to stop)")
    while user_input != 'n':

        if user_input == 'y':
            example_graph()
            continue

        elif user_input == 'n':
            break

        else:
            print("Invalid input")
    user_input = input("Do you wish to proceed? (This will show you an example. Press y to proceed and n to stop)")



main()




