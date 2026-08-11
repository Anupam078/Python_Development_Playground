shop = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
 
items = list(shop.items())
 
for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] < items[j + 1][1]:
            temp = items[j]
            items[j] = items[j + 1]
            items[j + 1] = temp
 
for i in range(3):
    print(items[i][0], items[i][1])