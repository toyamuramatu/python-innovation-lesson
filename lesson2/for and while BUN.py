a=0
for i in range(1,101):
    a+=i
print(a)

b=0
c=0
while c==5050:
    b+=1
    c+=b
print(c)



for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz3️⃣ 5️⃣")
    elif i%3==0:
        print("Fizz3️⃣")
    elif i%5==0:
        print("Buzz5️⃣")
    else:
        print(i)