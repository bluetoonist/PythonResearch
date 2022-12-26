from __future__ import annotations

from pubsub import pub

from order import Order


def notification_customer_that_meal_is_done(arg):
    print(arg)


pub.subscribe(notification_customer_that_meal_is_done, 'meal-done')

pub.sendMessage('meal-done', arg={
    'order': Order(1)
})
