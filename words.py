# 一个最小的单词本。总共 30 多行，每一行我都写了注释。
# 运行方法（在项目文件夹里打开终端）：
#   python words.py add apple 苹果
#   python words.py list

import json      # 用来读写 .json 文件
import os        # 用来判断文件在不在
import sys       # 用来接收你在命令行打的字

FILE = "words.json"


def load():
    """把文件里的单词读出来。文件还不存在，就返回一个空的字典。"""
    if not os.path.exists(FILE):
        return {}
    with open(FILE, encoding="utf-8") as f:
        return json.load(f)


def save(data):
    """把字典写回文件。ensure_ascii=False 是为了让中文正常显示，不变成 你 这种。"""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# sys.argv 是「你在命令行里敲的所有词」
# 比如敲 python words.py add apple 苹果
# sys.argv 就是 ['words.py', 'add', 'apple', '苹果']
command = sys.argv[1] if len(sys.argv) > 1 else "list"

if command == "add":
    word = sys.argv[2]
    meaning = sys.argv[3]
    data = load()          # 先把已有的读出来
    data[word] = meaning   # 加进去
    save(data)             # 再存回去
    print(f"已添加：{word} → {meaning}")

elif command == "remove":
    word = sys.argv[2]
    data = load()
    del data[word]
    save(data)
    print(f"已删除:{word}")
    
elif command == "list":
    data = load()
    if not data:
        print("还没有单词。先试试：python words.py add apple 苹果")
    for word, meaning in data.items():
        print(f"{word}  -  {meaning}")

else:
    print("用法：")
    print("  python words.py add <英文> <中文>")
    print("  python words.py list")
