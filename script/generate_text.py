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

import random
from datetime import datetime, timedelta



def auto_create():
    root = "/root/project/doc/lismin/docs/IELTS/"

    # 设置2025年1月1日作为起始日期
    start_date = datetime(2025, 1, 1)
    # 设置2025年12月31日作为结束日期
    end_date = datetime(2025, 1, 27)

    # 使用 for 循环遍历所有日期
    current_date = start_date
    while current_date <= end_date:
        time_text = current_date.strftime("%Y-%m-%d")  # 输出日期，格式为 YYYY-MM-DD
        current_date += timedelta(days=1)  # 增加一天
        




if __name__ == "__main__":
    auto_create()