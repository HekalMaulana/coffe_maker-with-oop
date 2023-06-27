from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_process = MoneyMachine()
coffe_maker_stop = False

while not coffe_maker_stop:
    print("ORDER COFFE MACHINE PROGRAM")

    drink_choose = input(f"Which drink you want order {menu.get_items()} :? ").lower()


    if drink_choose == "report":
        coffee_maker.report()
        money_process.report()
    elif drink_choose == "off":
        print("Thanks for use this program")
        coffe_maker_stop = True
    else:
        drink_item = menu.find_drink(drink_choose)
        if coffee_maker.is_resource_sufficient(drink_item) and money_process.make_payment(drink_item.cost):
            print(f"Cost for your {drink_item.name} : {drink_item.cost}")
            coffee_maker.make_coffee(drink_item)
