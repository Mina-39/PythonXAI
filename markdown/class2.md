這是 class 2 的筆記

# 🐍 Python 第二堂課｜小學生也能懂的筆記

---

## 🌐 一、Streamlit 數字輸入（number_input）

```python
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50, step=1)
```

👉 這是一個 **可以用滑鼠點的數字輸入框**

- `min_value`：最小值
- `max_value`：最大值
- `value`：一開始顯示的數字
- `step`：一次加或減多少

---

## 🧮 二、成績等第判斷（if / elif / else）

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"
```

👉 像在說：

- 如果成績很高 ➜ A
- 不然如果次高 ➜ B
- 其他 ➜ F

---

## 🎈 三、按鈕特效（button）

```python
if st.button("點我"):
    st.balloons()
```

👉 按一下按鈕就會出現 🎈 或 ❄️

---

## 🔁 四、for 迴圈（重複做事情）

```python
for i in range(5):
    print("hello")
```

👉 `range(5)` 表示 **做 5 次**

| 寫法            | 意思    |
| --------------- | ------- |
| `range(5)`      | 0~4     |
| `range(2,6)`    | 2~5     |
| `range(2,10,2)` | 2,4,6,8 |

---

## 🔺 五、數字金字塔

```python
for i in range(1, height+1):
    st.write(str(i) * i)
```

👉 第 1 行 1 個數字
👉 第 2 行 2 個數字

---

## ⭐ 六、箭頭金字塔

- 空白：用來排位置
- `*`：畫圖案
- `\n`：換行

👉 用「慢慢把字串接起來」畫出圖形 ✨

---

## 📦 七、串列 List（像盒子）

```python
L = [1, 2, 3]
```

👉 串列可以放很多東西

| 串列           | 說明         |
| -------------- | ------------ |
| `[1,2,3]`      | 數字         |
| `["a","b"]`    | 文字         |
| `[1,"a",True]` | 混合         |
| `[1,[2,3]]`    | 裡面還有盒子 |

---

## 👉 八、取串列的東西

```python
L = [1,2,3,[4,5]]
L[0]     # 1
L[3][0]  # 4
```

👉 電腦從 **0 開始數** ⚠️

---

## ✂️ 九、串列切片

```python
L = [1,2,3,"a","b","c"]
L[1:4]    # 2,3,a
L[::2]    # 1,3,b
```

👉 可以剪出一部分

---

## 📏 十、len（有幾個）

```python
len([1,2,3])  # 3
```

👉 看盒子裡有幾樣東西

---

## 🔄 十一、走訪串列（for）

```python
for item in L:
    print(item)
```

👉 一個一個拿出來看 👀

---

## ✏️ 十二、改串列內容

```python
a = [1,2,3]
a[0] = 10
```

👉 串列裡的東西 **可以改**

⚠️ `b = a` 會共用同一個盒子

---

## ➕➖ 十三、串列常用功能

| 指令        | 功能         |
| ----------- | ------------ |
| `append(x)` | 加到最後     |
| `remove(x)` | 移除第一個 x |
| `pop()`     | 拿掉最後     |
| `sort()`    | 排序         |

---

## 📂 十四、讀檔案

```python
with open(file,"r") as f:
    content = f.read()
```

👉 把檔案內容讀進來

---

## 📁 十五、找資料夾裡的檔案

```python
os.listdir("資料夾")
```

👉 可以找出指定副檔名 `.md`

---

## 🧱 十六、Streamlit 排版（columns）

```python
col1, col2 = st.columns(2)
```

👉 把畫面切成欄位 📐

---

## ⌨️ 十七、文字輸入框

```python
text = st.text_input("請輸入文字")
```

👉 使用者可以打字

---

## 🧠 十八、Session State（記住資料）

```python
ss = st.session_state
ss.ans += 1
```

👉 **就算重新整理，數字也不會消失！**
