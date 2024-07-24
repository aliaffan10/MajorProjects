import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def main():
    # Get User Name to create a personalized welcome message on the App Page
    user_name = input("Enter Your Username Here: ").strip().title()
    # Validate the User Name so that user doesn't perovide White Space
    validate_user_name(user_name)

    # Promp User for what color scheme they want in the app
    theme_choice = input("Select One: Dark Mode or Light Mode (You Can Type D or L) ---- ")
    # Using User's Option, set background colour and font colour
    bg, fg = finalize_colour_scheme(theme_choice.strip())


    """ Creating the GUI using TKinter Modules """

    # Creating the Window (Name, Color, Etc)
    main = tk.Tk()
    main.title("Expenditure Management Application")
    main.configure(bg=bg)

    # Creating the Header
    header_style = ttk.Style()
    header_style.configure("TLabel", font=('Arial', 22), foreground=fg)
    welcome_widget1 = ttk.Label(main, text="Expenditure Management App", background=bg, style="TLabel")
    welcome_widget2 = ttk.Label(main, text=f"Welcome {user_name}", background=bg, foreground=fg)
    welcome_widget1.grid(row=0, column=0, columnspan=3, pady=10)
    welcome_widget2.grid(row=1, column=1, columnspan=1)

    #Creating New Category Line (Widget 1)
    text_category = tk.Label(main, text="Category Name:", background=bg, foreground=fg)
    enter_category = tk.Entry(main, background=bg, foreground=fg)
    button_to_create_category = tk.Button(main, text="Create New Category", background=bg, foreground=fg,command=lambda: create_category(enter_category, listbox_categories))
    #Creat Empty Lines
    ttk.Label(main, text="   ",background=bg).grid(row=2, column=0)
    #Grid Lines for Widget 1
    text_category.grid(row=3, column=0, columnspan=1)
    enter_category.grid(row=3, column=1)
    button_to_create_category.grid(row=3, column=2)


    #Creating Category List and the Show Category Balance Button (Widget 2)
    tk.Label(main, text="List of Categories:",background=bg, foreground=fg).grid(row=4, column=1)
    listbox_categories = tk.Listbox(main, background=bg, foreground=fg)
    show_balance = tk.Button(main, text="Show Balance", height=3, background=bg, foreground=fg,command=lambda: show_balance_func(listbox_categories)) 
    #Grid Lines for Widget 2
    listbox_categories.grid(row=5, column=1)
    show_balance.grid(row=5, column=2)

    #Creating Entry Amount and Description Buttons (Widget 3)
    amount_label = tk.Label(main, text="Enter Amount", background=bg, foreground=fg)
    amount_entry = tk.Entry(main, background=bg, foreground=fg)
    description_label = tk.Label(main, text="Description", background=bg, foreground=fg)
    description_entry = tk.Entry(main, background=bg, foreground=fg)
    #Grid Lines for Widget 3
    amount_label.grid(row=7, column=0)
    amount_entry.grid(row=7, column=1)
    description_label.grid(row=8, column=0)
    description_entry.grid(row=8, column=1)

    #Creating Deposit and Withdraw Buttons (Widget 4)
    deposit_button = tk.Button(main, text="DEPOSIT", background=bg, foreground=fg,command=lambda: deposit_func(listbox_categories, amount_entry, description_entry))
    withdraw_button = tk.Button(main, text="WITHDRAW", background=bg, foreground=fg,command=lambda: withdraw_func(listbox_categories, amount_entry, description_entry)) 
    #Grid Lines for Widgets 4
    deposit_button.grid(row=7, column=2)
    withdraw_button.grid(row=8, column=2)

    #Creating Transfer and And Entry to enter the category name (Widget 5)
    transfer_label = tk.Label(main, text="Trasfer to", background=bg, foreground=fg)
    entry_transfer = tk.Entry(main, background=bg, foreground=fg)
    transfer_button = tk.Button(main, text="Transfer", background=bg, foreground=fg,command=lambda: transfer_func(listbox_categories, entry_transfer, amount_entry))
    #Grid Lines for Widget 5
    transfer_label.grid(row=9, column=0)
    entry_transfer.grid(row=9, column=1)
    transfer_button.grid(row=9, column=2)

    ttk.Label(main, text="   ",background=bg).grid(row=10, column=0)

    #Creating Ledger button to show whole expenses of the category (Widget 6)
    button_show_ledger = tk.Button(main, text="Show Ledger History", background=bg, foreground=fg,command=lambda: show_ledger_func(listbox_categories, print_ledger_text))
    print_ledger_text = tk.Text(main, width=50, height=8, background=bg, foreground=fg)
    #Grid Lines for Widget 6
    button_show_ledger.grid(row=11, column=1)
    print_ledger_text.grid(row=12, column=0, columnspan=3, pady=5)

    #Creating Show Chart Button, to show a bar graph of the expenses (Widget 7)
    button_show_chart = tk.Button(main, text="Show Spend Chart", background=bg, foreground=fg,command=lambda: show_chart_func(print_chart_text))
    print_chart_text = tk.Text(main, width=50, height=15, background=bg, foreground=fg)
    #Grid Lines for Widget 7
    button_show_chart.grid(row=13, column=1)
    print_chart_text.grid(row=14, column=0, columnspan=3, pady=5)

    #Creating Exit Button (WIdget 8)
    exit_button = tk.Button(main, text="Exit & Show Total Balance", background=bg, foreground='white', command=lambda: exit_and_show_bal_func(main), width=25)
    exit_button.grid(row=15, column=0, columnspan=2)

    # Full Exit Butto Widget 9 
    exit_button = tk.Button(main, text="Exit", background='red', foreground='white', command=exit, width=15)
    exit_button.grid(row=15, column=2)
    
    #Running the Final Window
    main.mainloop()

    #To return the Final Balance Of the Customer
    remain_balance = return_remain_balance(categories)
    print(f"Fetching Remaining Balance.....\n\nMr/Mrs. {user_name}\nYour Remaining Balance is {remain_balance:.2f} AED")

    #Final Exit Message
    print("\nExiting...................\n")
    
    """END OF PROGRAM"""

class Category:
    # Initiate object
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    # How to print format
    def __str__(self):
        #Print Initial Category Header
        title = f"*************{self.category}*************\n"
        items = ""
        
        #Iterate over each item in the ledger list
        for item in self.ledger:
            # Slice the Description so that only 23 character fit in the output
            description = item["description"][:23]
            # Print amount as 7 characters wide
            amount = f"{item['amount']:>7.2f}"
            # Append the Description and Amount into mylist
            items += f"{description:<23}{amount}\n"
        # Make the final Total price line and join them
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


    def deposit(self, amount, description=""):
        #Add Amount and description of it to the ledger list
        self.ledger.append({"amount": amount,"description": description})
        # Increment balance by the amount
        self.balance += amount

    def withdraw(self, amount, description=""):
        # Check if funds are available 
        if self.check_funds(amount):
            # If Available then append amount in negative
            self.ledger.append({"amount": -amount, "description": description})
            # Deduct amount from balance
            self.balance -= amount
            return True
        else:
            return False
        
    def get_balance(self):
        # Just returns the current balance
        return self.balance
    
    def transfer(self, amount, other_category):
        # Check if funds are available
        if self.check_funds(amount):
            # Transfer funds to other category by withdrawing from current
            self.withdraw(amount, f"Transfer to {other_category.category}")
            # Deposit in other category
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        # Checks funds if the amount is less than or equal to balance
        return amount <= self.get_balance()

    def cateogory_withdrawals(self):
        total_withdrawals = 0
        # Iterate over each item in ledger
        for item in self.ledger:
            # If amount is less then 0
            if item["amount"] < 0:
                # Add it to the total
                total_withdrawals += item['amount']
        return total_withdrawals

def validate_user_name(name):
    #Taking in user's input name, check if it has only white spaces or it empty
    if name == "" or name.isspace():
        # If yes, raise Value Error
        raise ValueError("Error12! Name not provided.")
    #Else return True, it is Valid
    return True
                   
def finalize_colour_scheme(theme_choice):
    # If User tells Dark Mode
    theme_choice = theme_choice.strip()
    if theme_choice.upper() == "DARK" or theme_choice.upper() ==  "DARK MODE" or theme_choice.upper() == "D":
        # Set BG AND FG
        background = "black"
        foreground = 'white'
    # Else if user specifies White Mode
    elif theme_choice.upper() == "LIGHT" or theme_choice.upper() == "LIGHT MODE" or theme_choice.upper() == "L":
        # Set BG AND FG
        background = "#8cbed6"
        foreground =  "black"
    else:
        #Default 
        background = "#8cbed6"
        foreground =  "black"
    # Return
    return background, foreground

def create_spend_chart(categories):
    total_withdrawals = 0
    # Add all the withdrawal amounts, to make a total
    for category in categories:
        total_withdrawals += category.cateogory_withdrawals()
    
    category_percentages = []
    # Iterate over each category in the provided list
    for category in categories:
        # Calculate percentage of each indivudal Category
        percentage = (category.cateogory_withdrawals()/ total_withdrawals) * 100
        # Append percentage into the percentage list
        category_percentages.append(percentage)

    rounded_percentages = []
    # Iterate over each percentage in the list
    for percentage in category_percentages:
        # ROund that percentage to the nearest 10
        rounded_percentages.append(int(percentage) // 10 * 10)
    
    #Create Bar Chart Header
    chart = "Percentage spent by category \n\n"

    #Create the bar chart
    for i in range(100, -1, -10):
        chart  += f"{i:>3}| "
        for percent in rounded_percentages:
            if percent >= i:
                chart += "o "
            else:
                chart += "  "
        chart += '\n'

    #Adding Horizontal Line
    chart += "    " + "-" * (len(categories) * 3-1) + '\n'

    #Find maximum length of category names
    max_len = 0
    for category in categories:
        if len(category.category) > max_len:
            max_len = len(category.category)

    #Add cateogry names below the chart
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + " "
            else:
                chart += "  "
        chart += '\n'

    # Return the final Chart
    return chart.rstrip("\n")



# Create Global Empty Dictionary
categories = {}
def create_category(enter_category, listbox_categories):
    
    # Get the Name entered by user and assign to the name
    name = enter_category.get()
    # If name Exists and it is not already the categories Dict
    if name and name not in categories:
        #Add category name inside the list from the Category Class
        categories[name] = Category(name)
        # Add the Category name to the list box in the TKinter Window
        listbox_categories.insert(tk.END, name)
    #Finally delete the entry from the entry field in the Tkinter Window
    enter_category.delete(0, tk.END)


def deposit_func(listbox_categories, amount_entry, description_entry):
    try:    
        #Select Category Name from the Category List 
        category_name = listbox_categories.get(listbox_categories.curselection())
        #Get the Deposit amount from entry field
        deposit_amount = float(amount_entry.get())
        # Get Descrioption from the that respective field
        description = description_entry.get()
        if deposit_amount:
            #Access the Category class method (deposit) to deposit amount at the category
            categories[category_name].deposit(deposit_amount, description)
        #Delete the entries from the fields
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
    except:
        #If User doesnt select a category, then show this error
        messagebox.showerror("ERROR!", "You Should Select a Category First")


def show_balance_func(listbox_categories):
    try:
        #Select Category Name from the Category List
        category_name = listbox_categories.get(listbox_categories.curselection())
        #Use the Category Class to get the balance using the get_balance() methods
        balance = categories[category_name].get_balance()
        #Show Message of the current balance
        messagebox.showinfo("Balance", f"Your Balance: {balance} AED")
    except: 
        #If User doesnt select a category, then show this error
        messagebox.showerror("ERROR!", "You Should Select a Category First")

def withdraw_func(listbox_categories, amount_entry, description_entry):
    try:    
        #Select Category Name from the Category List 
        category_name = listbox_categories.get(listbox_categories.curselection())
        #Get the Withdraw amount from entry field
        withdraw_amount = float(amount_entry.get())
        # Get Descrioption from the that respective field
        description = description_entry.get()
        #Access the Category class method (deposit) to deposit amount at the category
        transaction = categories[category_name].withdraw(withdraw_amount, description)
        if withdraw_amount and transaction:
            # Delete Entries
            amount_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)
        else:
            #If Class Category's method withdraw() returns False, then give error
            messagebox.showerror("ERROR!", "You dont have enough funds")
    except:
        #If User doesnt select a category, then show this error
        messagebox.showerror("ERROR!", "You Should Select a Category First")

def transfer_func(listbox_categories, entry_transfer, amount_entry):
    try:
        #Select Category Name from the Category List, which shows where we are tranferring from        
        transfer_from = listbox_categories.get(listbox_categories.curselection())
        #Get the ctaegry to tranfer to, from the entry field
        transfer_to = entry_transfer.get()
        # Get the transfer amount from amount entry field
        transfer_amount = float(amount_entry.get())
        # Using Category Class and transfer() method, tranfser the amount
        if categories[transfer_from].transfer(transfer_amount, categories[transfer_to]):
            #Delete the entered data
            amount_entry.delete(0, tk.END)
            entry_transfer.delete(0, tk.END)
        else:
            #IF tranfer() method returns False, hence funds are not enough, generate error
            messagebox.showerror("ERROR!", "You dont have enough funds")
    except:
        #If User doesnt select a category, then show this error
        messagebox.showerror("ERROR!", "You should Select a Category First")
    
def show_ledger_func(listbox_categories, print_ledger_text):
    try:
        #Select Category Name from the Category List
        category_name = listbox_categories.get(listbox_categories.curselection())
        #Delete the Previous Contents of the Print Box
        print_ledger_text.delete(1.0, tk.END)
        #Use the __str__ method of the Category Class to output the ledger text
        print_ledger_text.insert(tk.END, str(categories[category_name]))
    except:
        #If User doesnt select a category, then show this error
        messagebox.showerror("ERROR!", "You should Select a Category First")
        
def show_chart_func(print_chart_text):
    try:    
        #Delete the cprevious contents of the Chart Window 
        print_chart_text.delete(1.0, tk.END)
        #Call the create Spend Char function, and print it in the chart window after button pressed
        print_chart_text.insert(tk.END, create_spend_chart(list(categories.values())))
    except:
        #If User doesnt select a category, then show this error
        messagebox.showerror("ERROR!", "You should Select a Category First")

def exit_and_show_bal_func(window):
    #If User Selects to Exit and Return Total
    window.destroy()
    print("\nClosing the Application........\n ")

def return_remain_balance(categories):
    #Initialize VARIABLE To 0 
    total_balance = 0
    # For each category in the category dictionary from what we added
    for category in categories.values():
        # Add the remaining balance of each Category
        total_balance += category.get_balance()
    #Return Total
    return total_balance

if __name__ == "__main__":
    main()