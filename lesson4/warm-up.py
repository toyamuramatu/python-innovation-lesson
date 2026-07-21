smartphone={"name":"スマートフォン","price":65000,"color":"黒","memory":"128GB"}
print(smartphone["price"])
smartphone["kamera"]="高性能カメラ搭載"
smartphone["color"]="青"
del smartphone ["memory"]
for key,value in smartphone.items():
    print(key)
    print(value)