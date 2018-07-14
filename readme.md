
PinYinGUI(拼音/粵拼)
==
使用pypinyin與Jyutping兩個專案,打包成GUI
以csv輸入及輸出

Instruction
--
```
git clone https://github.com/chimin17/pinyingui.git
```
```
pip install pandas
```
```
pip install
```
```
python main.py
```
![Demo](demo.png)

Input example
--
## input.csv
```
chinese
市立文林國小(台北市)
市立義方國小(台北市)
市立立農國小
市立明德國小
市立洲美國小
```


PinYin Database:
--
https://github.com/mozillazg/python-pinyin
- single mode: pinyin-data  https://github.com/mozillazg/pinyin-data
- phrase mode: phrase-pinyin-data https://github.com/mozillazg/phrase-pinyin-data
- self-defined


Jyutping Database
--
https://github.com/imdreamrunner/python-jyutping
- 2013年 kaifangcidian.com   http://www.kaifangcidian.com


Release Note
--
| Date | Model | Version | Note|
| :-------- | :----- | :---------- | :---------- |
| 2018-07-02   | PinYin Jyutping Tool | 0.2 | revise output bug 'Café'(encode error)|
| 2018-06-29   | PinYin Jyutping Tool | 0.1 | Beta|
