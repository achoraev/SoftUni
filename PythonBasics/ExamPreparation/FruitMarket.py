strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price - (raspberry_price * 0.4)
banana_price = raspberry_price - (raspberry_price * 0.8)

strawberry_sum = strawberry_quantity * strawberry_price
banana_sum = banana_quantity * banana_price
raspberry_sum = raspberry_quantity * raspberry_price
orange_sum = orange_quantity * orange_price

total_sum = strawberry_sum + banana_sum + raspberry_sum + orange_sum

print(f"{total_sum:.2f}")