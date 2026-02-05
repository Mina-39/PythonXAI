# 🐍 Python 第四堂課｜小學生也能輕鬆懂筆記

---

## 🖼️ 一、圖片元件（st.image）

```python
st.image("image/apple.png", width=300)
```

👉 可以把圖片顯示在網頁上，就像做相簿 📸

- `width`：圖片寬度
- `caption`：圖片下面的說明文字

### 📂 一次顯示資料夾裡的圖片

```python
image_files = os.listdir("image")
```

👉 先拿到資料夾裡的所有檔案，再用 for 迴圈一張一張顯示

---

## 🔽 二、下拉選單（selectbox）

```python
selected = st.selectbox("請選擇圖片", image_files)
```

👉 像選午餐一樣，用下拉選單選圖片 🍱

---

## 💬 三、網頁訊息元件

| 指令           | 用途        |
| -------------- | ----------- |
| `st.success()` | 成功訊息 ✅ |
| `st.error()`   | 錯誤訊息 ❌ |
| `st.warning()` | 警告訊息 ⚠️ |
| `st.info()`    | 提示訊息 ℹ️ |

👉 常用來告訴使用者「發生什麼事」

---

## 🛒 四、購物平台（圖片＋價格＋庫存）

### 商品資料長這樣：

```python
ss.products[name] = {
  "image_path": "圖片路徑",
  "price": 10,
  "stock": 10
}
```

👉 一個商品就像一張資料卡 🪪

---

### 🧱 用 columns 排版商品

```python
cols = st.columns(3)
```

👉 把商品排成好幾欄，看起來像真正的購物網站

---

### 🛍️ 購買商品

- 如果庫存 > 0 ➜ 可以買
- 如果庫存 = 0 ➜ 顯示「庫存不足」

👉 買完庫存會減 1

---

## ➕ 五、新增庫存

```python
ss.products[name]["stock"] += add_stock
```

👉 幫商品補貨 📦

---

## 🧠 六、什麼是函數（function）？

👉 函數就像「小幫手」🤖

### 最簡單的函數

```python
def hello():
    print("hello")
```

👉 叫一次，就幫你做一次

---

## 🧩 七、有參數的函數

```python
def greet(name):
    print("Hello", name)
```

👉 可以把資料丟進去用

---

## 🎁 八、有回傳值的函數

```python
def two_num_min(a,b):
    return a
```

👉 函數會算好答案再交回來 📤

---

## ⚙️ 九、預設參數

```python
def area(r, pi=3.14):
    return pi * r * r
```

👉 沒給的話，用預設值

---

## 🧠 十、全域變數 vs 區域變數

### 🏠 全域變數

- 在程式外面
- 大家都看得到

### 🚪 區域變數

- 在函數裡
- 只有函數裡能用

👉 同名時，函數裡的會先用（區域優先）

---

## 🔑 十一、return vs global

- `return`：把結果交出來（推薦 👍）
- `global`：直接改外面的變數（要小心 ⚠️）

---
