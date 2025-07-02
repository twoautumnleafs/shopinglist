BASE_PRICES = {
    "bread": 1.6, "milk": 1.0, "apples": 2.0, "cheese": 3.5, "eggs": 2.2,
    "butter": 2.5, "banana": 1.8, "chicken": 5.0, "rice": 1.3, "tomatoes": 2.1,
    "potatoes": 1.0, "onions": 0.8, "carrots": 1.1, "yogurt": 0.9,
    "orange": 1.5, "coffee": 4.0, "tea": 3.0, "sugar": 1.4, "salt": 0.5, "pepper": 1.7,
}

unit_groups = {
    "p": {"bread", "eggs", "yogurt", "coffee"},
    "l": {"milk"},
    "kg": {"apples", "cheese", "butter", "banana", "chicken", "rice", "tomatoes",
           "potatoes", "onions", "carrots", "orange", "tea", "sugar", "salt", "pepper"},
}
units = {}
for unit, items in unit_groups.items():
    for item in items:
        units[item] = unit