# # 挨拶する関数
# def say_hello():
#     print("やあ！")

# say_hello()

# def greet_name(name):
#     print(f"こんにちは、{name}さん！")

# greet_name("村松燈弥")

# def add_and_show(num1, num2):
#     print(num1 + num2)

# add_and_show(5, 7)

# def add_and_show(num1, num2):
#     print(num1 - num2)

# add_and_show(5, 7)

# def calculate_sum(a, b):
#     return a + b

# print(calculate_sum(100, 200))

# #-----------------------------------------------------------------------------------------------------------------------------

# def calculate_product(a,b):
#     return a*b

# print(calculate_product(125,8))


# def my_favorite_chor(a,b):
#     return f"{a}の好きなキャラは{b}です"

# print(my_favorite_chor("だれかさん","だれかさん"))


a=0
def calculate_discounted_total(price,quantity):
    a=price*quantity
    if quantity>=5:
        a=a*0.9
    return int(a)

print(calculate_discounted_total(300,10))


