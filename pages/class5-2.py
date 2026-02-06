import openai
from dotenv import load_dotenv
import os

load_dotenv()  # 載入 .env 檔案內容

# 設置 API 金錀
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    user_input = input("你:")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = openai.chat.completions.create(
        model="gpt-5.1-chat-latest",
        messages=[
            {"role": "system", "content": "請用繁體中文進行後續對話"},
            {"role": "user", "content": user_input},
        ],
    )

    assistant_message = response.choices[0].message.content
    print(f"AI: {assistant_message}")
