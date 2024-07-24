from project import validate_user_name, finalize_colour_scheme, create_spend_chart, return_remain_balance, Category
import pytest

def test_get_user_name():
    assert validate_user_name("Ali Affan") == True
    assert validate_user_name("        Ali Affan            ") == True
    assert validate_user_name(" Ali     Affan") == True
    with pytest.raises(ValueError):
        validate_user_name("")
    with pytest.raises(ValueError):
        validate_user_name("     ")

def test_finalize_colour_scheme():
    # Test Case 1 - Dark Mode
    bg, fg = finalize_colour_scheme("dark")
    assert bg == "black"
    assert fg == "white"
    bg, fg = finalize_colour_scheme("  dArk MoDe   ")
    assert bg == "black"
    assert fg == "white"
    bg, fg = finalize_colour_scheme("d")
    assert bg == "black"
    assert fg == "white"
    bg, fg = finalize_colour_scheme("D")
    assert bg == "black"
    assert fg == "white"

    #Test Case 2- Light Mode
    bg, fg = finalize_colour_scheme("light")
    assert bg == "#8cbed6"
    assert fg == "black"
    bg, fg = finalize_colour_scheme("   liGht MoDe    ")
    assert bg == "#8cbed6"
    assert fg == "black"
    bg, fg = finalize_colour_scheme()
    assert bg == "#8cbed6"
    assert fg == "black"
    bg, fg = finalize_colour_scheme("L")
    assert bg == "#8cbed6"
    assert fg == "black"

def test_return_remain_balance():
    #Test 1 ----
    food = Category("Food")
    games = Category("Games")
    food.deposit(100)
    food.withdraw(30)
    games.deposit(60)
    games.withdraw(25)
    categories = {'Food': food, 'Games': games}
    # Final
    assert return_remain_balance(categories) == 105

    #Test 2 ----
    books = Category("Books")
    uni = Category("University")
    books.deposit(500, "Saving")
    books.withdraw(400, "AS level Course Books")
    uni.deposit(15000, "Annual Fee")
    uni.withdraw(7000, "Sem Fee")
    categories = {'University': uni, 'Books': books}
    #Final
    assert return_remain_balance(categories) == 8100