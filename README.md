# vocab-cli

一个命令行单词本：增删查、每日抽考、记录正确率。

## 功能

- `add` / `remove` / `list`：管理单词，数据存在 `words.json`
- `quiz`：随机抽 10 个词考自己，正确率追加到 `stats.csv`

## 运行

```bash
python vocab.py add apple 苹果
python vocab.py list
python vocab.py quiz
```

## 技术栈

Python 3.10+，只用标准库（json / random / argparse / pathlib），零第三方依赖。

## 为什么用 JSON 而不是数据库

300 个词的规模，JSON 够用、能直接打开看、方便调试。
等词量上千或需要多端同步再换 SQLite——这是取舍，不是能力不足。

## 进度

- [x] 项目初始化
- [x] add / list
- [x] remove
- [ ] quiz + 正确率统计
