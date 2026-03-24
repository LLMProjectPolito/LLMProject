def eat(number, need, remaining):
    total_eaten = number
    remaining_after_meals = remaining - need
    return [total_eaten, remaining_after_meals]