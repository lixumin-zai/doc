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
import os


def auto_create():
    root = "/root/project/doc/lismin/docs/IELTS/"

    # 设置2025年1月1日作为起始日期
    start_date = datetime(2025, 1, 1)
    # 设置2025年12月31日作为结束日期
    end_date = datetime(2025, 1, 27)

    # 使用 for 循环遍历所有日期
    current_date = start_date
    while current_date <= end_date:
        month_text = current_date.strftime("%Y-%m")
        day_text = current_date.strftime("%Y-%m-%d")  # 输出日期，格式为 YYYY-MM-DD
        current_date += timedelta(days=1)  # 增加一天
        os.path.exists(root+month_text) or os.makedirs(root+month_text)
        with open(root+month_text+f"/{day_text}.mdx", "w") as f:
            f.write("""

The **ballet** troupe, operating on a shoestring **budget**, found themselves in a tricky situation. There was a **degradation** in the enthusiasm of the audience, perhaps due to the repetitive **pattern** of their shows. To address this, they decided to toss out the old **generalisation** that simplicity was best and embrace something **exotic**. They brought in a choreographer to **refine** the routines, adding in new and exciting movements. The dancers worked hard to improve their **grip** on these complex steps. As a result, the tickets sales started to **soar**. But this transformation didn't come without a **toll**; the stress on the dancers was high, and the management had to **soften** the training regime a bit to keep everyone's spirits up. 

中文释义：这个靠微薄预算运营的**芭蕾舞**团陷入了棘手的境地。观众的热情有所**减退**，可能是因为他们演出的**模式**过于重复。为了解决这个问题，他们决定摒弃 “简约至上” 这种旧有的**普遍观念**，去接纳一些充满**异域风情**的元素。他们请来一位编舞师对舞蹈动作进行**优化**，加入了新颖又刺激的舞步。舞者们努力提升对这些复杂舞步的**掌控**能力。结果，门票销量开始**飙升**。但这种转变并非毫无**代价**；舞者们承受的压力很大，管理层不得不稍微**放宽**训练制度，以此来鼓舞大家的士气 。  

""")
        break




if __name__ == "__main__":
    auto_create()