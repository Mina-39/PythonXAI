# 🐍 Python 第三堂課｜小學生也能輕鬆懂筆記

---

## 🍔 一、點餐機（購物籃概念）

```python
ss = st.session_state
ss.orders = []
```

👉 `session_state` 就像 **記憶盒子**，可以幫我們記住點過的餐點

### 加入餐點

- 使用 `text_input` 輸入餐名
- 按下「加入」➡ 放進購物籃

### 刪除餐點

- 每一個餐點旁邊都有「刪除」按鈕
- 用 `pop(i)` 把不要的餐點拿掉 🗑️

---

## ➕ 二、算數指定運算子（偷懶寫法）

```python
a += b   # a = a + b
a -= b   # a = a - b
a *= b   # a = a * b
```

👉 讓程式寫起來 **更短更快** ✨

---

## 🔁 三、while 迴圈（一直做到不符合為止）

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

👉 只要條件是「對的」，就會一直跑

---

## 🛑 四、break（強制停止）

```python
if i == 3:
    break
```

👉 遇到 break，迴圈立刻停下來 ❌

---

## 🎲 五、random 隨機數

```python
random.randrange(1, 6)
random.randint(1, 5)
```

👉 就像 **擲骰子** 🎲

- `randrange`：範圍比較彈性
- `randint(a,b)`：a 到 b（都包含）

---

## 📊 六、統計出現次數

```python
count[r-1] += 1
```

👉 用串列記錄「每個數字出現幾次」

---

## 🤔 七、猜數字遊戲（文字版）

- 電腦先想一個數字
- 玩家一直猜
- 電腦提示：
  - 再大一點
  - 再小一點
  - 猜對了！🎉

👉 用 `while True` 一直玩到猜對

---

## 🌐 八、猜數字遊戲（Streamlit 版）

```python
ss.target
ss.min_val
ss.max_val
```

👉 用 **session_state 記住範圍與答案**

- 猜對會放氣球 🎈
- 遊戲會自動重來

---

## 🗂️ 九、字典 dict（資料對照表）

```python
D = {"A":90, "B":80}
```

👉 像「姓名 ➜ 分數」的表格

| Key | Value |
| --- | ----- |
| A   | 90    |
| B   | 80    |

---

## 🔍 十、使用字典

```python
D["A"]        # 90
"A" in D      # True
```

👉 用 key 找 value 🔑

---

## 🔁 十一、走訪字典

```python
for key, value in D.items():
    print(key, value)
```

👉 一組一組拿出來看 👀

---

## ✏️ 十二、修改與刪除字典

```python
D["f"] = 6      # 新增
D["a"] = 10     # 修改
D.pop("c")      # 刪除
```

---

## 📏 十三、len 與 in

```python
len(D)
"d" in D
```

👉 看有幾組資料、有沒有這個 key

---

## 🧪 十四、字典＋串列：成績統計

```python
scores = {"國文":[], "英文":[]}
```

👉 每一科都是一個「成績盒子」

- 先隨機產生成績
- 再算平均分數

---
