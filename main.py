from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_options = Menu()
CoffeeMachine = CoffeeMaker()
moneyCheck = MoneyMachine()
drinkinfo = MenuItem('name', 'water', 'milk', 'coffee','cost')

def proccessor(drink):
    drinkinfo = MenuItem(menu_options.find_drink(drink),menu_options.find_drink(drink).ingredients,menu_options.find_drink(drink).ingredients,menu_options.find_drink(drink).ingredients,menu_options.find_drink(drink).cost)
    if CoffeeMachine.is_resource_sufficient(menu_options.find_drink(drink)):
        if moneyCheck.make_payment(drinkinfo.cost):
            CoffeeMachine.make_coffee(menu_options.find_drink(drink))


run = True
while run:
    drink_choice = input(f"What would you like? {menu_options.get_items()}: ")
    if drink_choice == 'report':
        print(CoffeeMachine.report())
    elif not menu_options.find_drink(drink_choice):
        run = False
    else:
        proccessor(drink_choice)






