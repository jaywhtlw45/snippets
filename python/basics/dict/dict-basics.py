def processItems(price: dict[str, float]):
    for item_name, item_price in price.items():
        print(item_name, item_price)
    
prices = { 
    "car": 4.3,
    "truck": 2.3
}

processItems(prices)