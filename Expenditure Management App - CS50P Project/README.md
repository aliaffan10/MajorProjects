# **Expenditure Management App**
#### Video Demo: https://youtu.be/shVnF-5JcqY
#### **Description:**

### 1 - What the Project is About?
In the provided code, tkinter is used to create an **expenditure management application**, featuring a window with various widgets like labels, entry fields, buttons, and text areas. These widgets facilitate user interactions such as entering category names, making deposits and withdrawals, displaying balances, showing ledger histories, and generating spend charts.

### 2 - Using the Tkinter Library
A standard GUI **(Graphical User Interface)** toolkit, tkinter is a library in Python which offers developers tools to create windows, buttons, labels among other widgets. Through this developer can build interactive interfaces for desktop applications. Likewise in the following project, tkinter is used to create an expenditure management application that includes **labels, entry fields and buttons as well as text areas on the window.** This assists user interactions like category names inputting deposits and withdrawals balancing indicating ledger histories and creating spend charts.

### 3 - Description of the Main Function in project.py
**To Start off**, my main function asks the user for their name, so that once the GUI Window is open it can give a personalized message to welcome the user, *like "Welcome [UserName]"* and the validation of the username is done through the ***validate_user_name()*** Fuunction **[Line 187]**. Then User is prompted again by the program to enter their choice of theme, weather Dark Mode or Light Mode (D or W), essentially use can type in "Dark Mode", "DARK" or "D" itself and likewise for light mode. But if the User doesnn't type anything, by default the Window will be in light mode. The Settings this function is present if you scroll just a bit down and find the ***finalize_colour_scheme()*** Function **[Line 195}** which sets the values of background and foreground accordingly.

#### **Tkinter Usage and GUI:**
A **'main'** window is creating using the **Tkinter as _tk._** And Further I've utilized more designing features such as 'main' window's header, and setting it background depending on what the user had selected as the theme choice. Futher Widgets have been created, which include **tk.Labels, tk.Entry, tk.ListBox, tk.Button and tk.Text.** Appropriate Text, backgroud colour, foreground colour and **command functions for buttons _(Which we will discuss More about down)_** have been set for each of the widgets from up to button of the GUI interface. Each widget has been then gridded according to what row and column, as well as the column span they take up in the GUI window.

**main.mainloop()** on line 104 is the used to run the GUI window. To exit the App/GUI the user has two options; either to exit and end program or to exit the app and return the final total balance. And to incorporate this I have created the Final Part of the Main function at Lines 107 - 111. That depending on the user's input in the GUI, calculate the Final Remianing Balance using the ***return_remain_balance()*** Function **[Line 386]** and outputs to the user a pesonalized message, finally also prints out an exiting message for the screen

### 4 - Creating the Class Category
Since we are making our app budget at each **Category**, I decided to make this Category as something we can make objects out of, hence created it as a Class. Now, Category Class comes with several methods, which also involves a double underscore str method or **__str__()** method. Which uniquely displays the history of all depoits and withdrawals from that specific category. It displays this when ever the **Show Ledger History** Button is pressed in the GUI.

Further this Class has methods ***deposit()*** and ***withdraw()*** which take three arguments, **1. Instance of the class, 2. Amount and 3. Description** and updates the instance balance of this category, by either adding the amount to the balance in the case of *deposit()* method and deducts in the case of *withdraw()* method.

More methods include the ***transfer()*** method, which takes three arguments. **1. Instance of the class, 2. Amount and 3. other_category(the other category to tranfer the amount to)**, and this function bascially withdraws specified amount of money from the current category to the one passed is in as the argument. Another small method used is the ***get_balance()*** method, which just returns the current balance. Another Method is used in the Class, called the ***cateogory_withdrawals()*** which just takes the instance of the class as the argument, and essentially returns the total amount of withdrawals that have taken place from the specific category. This method is used later in another function.

Finally one of th emost important methods, is ***the check_funds()*** methods which takes two arguments, **1. Instance of the Class, 2. amount**, this method makes sure that there is enough balance/funds in the current category so that any withdrawal operation can take place. This method is used in both ***withdraw()*** and ***transfer()*** methods, to make sure transaction can take place.

### 5 - Custom Functions
Now to the heart of the program, the custom function that make up the firmwall of the program. Lets start with the ***create_spend_chart()*** Function **[Line 214]**. Which creates a graph rounded to the nearest 10, and utilizing the ***cateogory_withdrawals()*** method from the Category Class, it displays a graph showing the **percentage spending in each category** in a form of a bar graph (represented with o's)

#### **Command Functions:**
Further now we move on the **Command Functions** that are created from **Line 272 to Line 384**, these function are what make up the functionality of the GUI/App Window, these functions are executed when the specific button is pressed on the GUI Window. For instance, once we enter our category name in the **tk.Entry Field**, and press the **"Create Category" Button**, the command function ***create_category()*** is executed and the created category is inserted into the listbox under, and contents of the entry field are removed.

All these command function are used with the **try and exception module** buuilt in python, with the cause of an *error*. we are now using the **messeagebox module** that we imported from the **Tkinter package**, that displays an *error message* to the user, that they an easily close and repeat their task.

Rest of the functions also are built on the same logic, and execute the specific task that they are codded about, another example would be the ***show_chart_func()*** which displays the graph that we earlier talked about. Fell free to visit my source code and check all these command function out and their functionality.

#### **Final Function and if __name__ == "__main__""**:
Finally the last but not the least Function of the code is the ***return_remain_balance()*** function, which bascially iterates through all the **values** of the **categories dictionary** that we are updating/adding stuff into as we use the app (bascially the previosu command functions), and the uses the **Category Class** Method ***get_balance()*** to get balance of each category instance and add it to the total_balance variable, and finally we return that variable and display to the user in the end of the **main() function**.
And finally finally, the end of the program happens with the classic if __name__ == "__main__": call main().


## Thank You Very Much for Reading this! This was CS50P and this was Ali Affan...
