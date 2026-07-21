# with open('hello.txt', 'r',encoding="utf-8") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())

# with open('output1.txt', 'w') as file:
#     file.write("こんにちは、Python!\n")
#     file.write("ファイル操作を学んでいます。")

# lines=["1行目:Pythonでファイル操作\n",
#        "2行目:とても便利です\n",
#        "3行目:試してみよう!"]

# with open('output2.txt', 'w') as file:
#     file.writelines(lines)


with open("memo.txt","w") as file:
    file.write("今日のメモ\n")
    file.write("Pythonでファイル操作を勉強しました")

with open('memo.txt', 'r',encoding="utf-8") as file:
    content = file.read()
    print("--- read()の結果---")
    print(content)