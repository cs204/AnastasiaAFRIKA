fruit_calories = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "KiwiFruit": 90,
    "lemon": 15,
    "Lime": 20,
    "Orange": 80,
    "Peach": 60,
    "Plums": 70,
}

fruit = input("Фрукт: ")

if fruit in fruit_calories:
    calories = fruit_calories[fruit]
    print(f"Калории: {calories}")
else:
    print("")