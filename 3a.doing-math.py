#By default, the input function outputs a string value, therefore you can not run calculations directly

num = input("How much is that phone?")
price = int(num)

discount_price = price * 0.8
message = f"The price of the phone is {price}, but I will sell you at a discount for {discount_price}"

print(message)

