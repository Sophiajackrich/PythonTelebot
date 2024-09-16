def decorator(topping):

    def pepper(basic_pizza):

        print(basic_pizza(), "Sprinkled with pepper")

    def tomatoes(basic_pizza):

        print(basic_pizza(), "Decorated with tomatoes")

    def onion(basic_pizza):

        print(basic_pizza(), "Sprinkled with onions")

    if topping == 1:

        return pepper

    elif topping == 2:

        return tomatoes

    else:

        return onion
@decorator(1)
def pepperoni():
    return "Thin dough, smeared with tomato sauce, sprinkled with cheese, sausage and oregano."
