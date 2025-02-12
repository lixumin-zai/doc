import json

import time
from zhipuai import ZhipuAI
import base64

class Chator:
    def __init__(
        self,
        api_key=""
    ):
        self.client = ZhipuAI(api_key=api_key)

    def chat(self, content):
        response = self.client.chat.completions.create(
            model="glm-4-flash",  # 请填写您要调用的模型名称
            messages=[
                {
                    "role": "system",
                    "content": """
# Role
你是一个雅思英语老师

# Task
给定5个单词，帮我组个雅思难度的句子, 只输出英文句子，并给出中文释义, 以及句子中其他短语的中文意思
                    """
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
            stream=True,
        )

        for chunk in response:
            yield chunk.choices[0].delta.content


    def vision_chat(self, image_bytes):
        img_base = base64.b64encode(image_bytes).decode('utf-8')
        response = self.client.chat.completions.create(
            model="glm-4v-flash",
            messages=[
            {
                "role": "user",
                "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": img_base
                    }
                },
                {
                    "type": "text",
                    "text": "识别图片中的打印体文本, 不要有其他解读，不需要对图片做描述，公式化学使用latex"
                }
                ]
            }
            ]
        )
        return response.choices[0].message.content, response.usage.completion_tokens

from volcenginesdkarkruntime import Ark
class doubao:
    def __init__(self):
        self.client = Ark(
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            region="cn-beijing"
        )

    def __call__(self, text):
        completion = self.client.chat.completions.create(
            model="ep-20250113150931-d9mt5",
            messages = [
                {"role": "system", "content": "你是一个见多识广的雅思老师"},
                {"role": "user", "content": f"将{text}组个雅思难度的句子，并输出中文释义，这些词使用**包裹"},
            ],
            # 免费开启推理会话应用层加密，访问 https://www.volcengine.com/docs/82379/1389905 了解更多
            extra_headers={'x-is-encrypted': 'true'},
        )
        return completion.choices[0].message.content
            

import random
from datetime import datetime, timedelta
import os
from db_process import Database
db = Database("./sentence.db")
chat = doubao()

def create_file():
    root = "/root/project/doc/lismin/docs/IELTS/"

    # 设置2025年1月1日作为起始日期
    start_date = datetime(2025, 1, 1)
    # 设置2025年12月31日作为结束日期
    end_date = datetime(2025, 1, 27)
    words_list = get_words()
    # 使用 for 循环遍历所有日期
    current_date = start_date

    data = db.get_data()
    i= 0
    while current_date <= end_date:
        
        month_text = current_date.strftime("%Y-%m")
        day_text = current_date.strftime("%Y-%m-%d")  # 输出日期，格式为 YYYY-MM-DD
        print(day_text)
        current_date += timedelta(days=1)  # 增加一天
        os.path.exists(root+month_text) or os.makedirs(root+month_text)
        gen_sentence = "\n\n___\n\n".join([text[2]for text in data[i:i+10]])
        with open(root+month_text+f"/{day_text}.mdx", "w") as f:
            f.write(gen_sentence)
        i+=1

def get_words():
    with open("./merge.json", "r") as f:
        words = json.load(f)
    words = [words[i:i+10] for i in range(0, len(words)+1, 10)]
    # for i in range(10):
    #     print(words.pop(0))
    return words

def auto_create():
    words_list = get_words()
    while True:
        words = words_list.pop(0)
        text = str(words)[1:-1]
        gen_sentence = chat(text)
        print(len(words_list), text)
        db.create_data(
            words=str(words),
            sentence=gen_sentence
        )
        if len(words_list) == 0:
            break

if __name__ == "__main__":
    create_file()

