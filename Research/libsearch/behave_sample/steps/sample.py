from behave.runner import Context
from behave import given, when, then


@given("an order containig a Chessebuger with Fries {dish_name}")
def setup_order(ctx, dish_name):
    print(dish_name)
    return ctx


@when("I ask for vegan substitutions")
def substitute_vegan(ctx):
    return ctx


@then("I Receive the meal with no animal products")
def check_all_vegan(ctx):
    assert 1 == 2


if __name__ == '__main__':
    context = Context()

    setup_order(context, dish_name='a')
    substitute_vegan(context)
    check_all_vegan(context)
