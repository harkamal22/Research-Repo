# Research-Repo
 Spiral.py is a Python program that draws a colorful spiral using the Turtle graphics library. 

### Step-by-Step Explanation:

1. First, the program imports the turtle library and creates a Turtle screen and a Turtle object. 


2. Next, it defines a function called draw_spiral that takes three parameters: num_turns, initial_length, and angle_increment. 
 - num_turns specifies the number of turns the spiral should have. 
 - initial_length specifies the length of the first segment of the spiral. 
 - angle_increment specifies the angle by which the turtle should turn after each segment.


3. Inside the draw_spiral function, it creates a list of colors that will be used to draw the spiral. 


4. Then, it uses a for loop to draw the spiral. Inside the loop, it sets the pen color of the turtle to the next color in the list. 


5. Next, it increases the pen size of the turtle and moves it forward by the current length. 


6. After that, it turns the turtle right by 90 degrees and increases the angle by the angle increment. 


7. Finally, it increases the length for the next segment and repeats the loop. 


8. Back in the main program, it sets the parameters for the spiral and calls the draw_spiral function to draw it. 


9. Finally, it closes the Turtle graphics window when the user clicks on it.
