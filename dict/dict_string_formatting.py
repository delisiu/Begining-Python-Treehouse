def favorite_food(dict):
    print("Hi, I'm {name} and I love to eat {food}!".format(**dict))
    return "Hi, I'm {name} and I love to eat {food}!".format(**dict)


favorite_food({'name' : 'AJ', 'food' : 'enchiladas'})
