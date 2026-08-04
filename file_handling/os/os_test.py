import os

currentDir = (os.getcwd())

print(f"現在のディレクトリ: {currentDir}")

with open("testfile.txt", "w",encoding='utf-8') as file:
    file.write("正しく実行されました") 

os.rename("testfile.txt", "renamed_test.txt")