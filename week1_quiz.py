def showGroceryList(name, prices, products):
    print("**************************")
    print(name + "'s grocery list:")
    print("**************************")

    totalPrice=0
    for i in range(len(products)):
        totalPrice+=prices[i]
        print("$" + str(prices[i]) + ":" + products[i])
    print("--------------------")
    print("$" + str(totalPrice))
    print("")

showGroceryList("Pat", [1.23, 1.11, 2.08], ['Apples', 'Peaches', 'Pears'])

showGroceryList("May", [2.13, 1.11, 2.08], ['Carrots', 'Beets', 'Cucumbers'])