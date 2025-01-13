import json
import os
import random

def merge_word():
    merge_data = []
    root_path = "./IELTS/"
    files_name = os.listdir(root_path)
    for file_name in files_name:
        file_path = root_path + file_name
        with open(file_path, "r") as f:
            word_data = json.load(f)
            word_data = [i["name"] for i in word_data]
            merge_data.extend(word_data)
    print(len(merge_data))
    random.shuffle(merge_data)
    with open("merge.json", "w") as f:
        json.dump(merge_data, f, ensure_ascii=False)
    
        
if __name__ == "__main__":
    merge_word()