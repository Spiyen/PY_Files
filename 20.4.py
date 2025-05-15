import json
from collections import defaultdict

# Чтение данных из файла
with open('orders.txt', 'r', encoding='utf-8') as file:
    orders = json.load(file)

# 1. Самый дорогой заказ
most_expensive_order = max(orders.items(), key=lambda x: x[1]['price'])
print(f"Самый дорогой заказ: {most_expensive_order[0]} (цена: {most_expensive_order[1]['price']})")

# 2. Заказ с самым большим количеством товаров
largest_quantity_order = max(orders.items(), key=lambda x: x[1]['quantity'])
print(f"Заказ с наибольшим количеством товаров: {largest_quantity_order[0]} (количество: {largest_quantity_order[1]['quantity']})")

# 3. День с наибольшим количеством заказов
date_counts = defaultdict(int)
for order in orders.values():
    date_counts[order['date']] += 1
busiest_day = max(date_counts.items(), key=lambda x: x[1])
print(f"День с наибольшим количеством заказов: {busiest_day[0]} ({busiest_day[1]} заказов)")

# 4. Пользователь с наибольшим количеством заказов
user_order_counts = defaultdict(int)
for order in orders.values():
    user_order_counts[order['user_id']] += 1
most_active_user = max(user_order_counts.items(), key=lambda x: x[1])
print(f"Самый активный пользователь: ID {most_active_user[0]} ({most_active_user[1]} заказов)")

# 5. Пользователь с наибольшей суммарной стоимостью заказов
user_total_spent = defaultdict(int)
for order in orders.values():
    user_total_spent[order['user_id']] += order['price']
biggest_spender = max(user_total_spent.items(), key=lambda x: x[1])
print(f"Пользователь с наибольшими тратами: ID {biggest_spender[0]} (потратил: {biggest_spender[1]})")

# 6. Средняя стоимость заказа
average_order_price = sum(order['price'] for order in orders.values()) / len(orders)
print(f"Средняя стоимость заказа: {average_order_price:.2f}")

# 7. Средняя стоимость товара (общая сумма / общее количество товаров)
total_items = sum(order['quantity'] for order in orders.values())
average_item_price = sum(order['price'] for order in orders.values()) / total_items
print(f"Средняя стоимость товара: {average_item_price:.2f}")