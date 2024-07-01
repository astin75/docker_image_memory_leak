import cv2
from PIL import Image
import psutil
import matplotlib.pyplot as plt
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

def save_fig(timestamps: list, memory_usages: list, memory_actuals: list, title: str, epoch: int):
    # 메모리 사용량 그래프 시각화
    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.set_xlabel('Time')
    ax1.set_ylabel('Memory Usage (%)', color='tab:blue')
    ax1.plot(timestamps, memory_usages, label='Memory Usage (%)', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Memory Usage (MB)', color='tab:red')
    ax2.plot(timestamps, memory_actuals, label='Memory Usage (MB)', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    fig.tight_layout()
    plt.title(f'Memory Usage Over Time during {title.capitalize()} Processing')
    plt.grid(True)
    plt.xticks(rotation=45)
    image_path = f"output/memory_usage_{title}_{epoch}.png"
    plt.savefig(image_path)

@app.get("/process_opencv")
def process_opencv():
    img = cv2.imread("test.jpg")
    memory_info = psutil.virtual_memory()
    return {"memory_percent": memory_info.percent, "memory_used": memory_info.used / (1024 ** 2)}  # MB 단위

@app.get("/process_opencv_rgb")
def process_opencv_rgb():
    img = cv2.imread("test.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    memory_info = psutil.virtual_memory()
    return {"memory_percent": memory_info.percent, "memory_used": memory_info.used / (1024 ** 2)}  # MB 단위

@app.get("/process_pillow")
def process_pillow():
    img = Image.open("test.jpg")
    memory_info = psutil.virtual_memory()
    return {"memory_percent": memory_info.percent, "memory_used": memory_info.used / (1024 ** 2)}  # MB 단위

@app.get("/process_pillow_rgb")
def process_pillow_rgb():
    img = Image.open("test.jpg")
    img = img.convert("RGB")
    memory_info = psutil.virtual_memory()
    return {"memory_percent": memory_info.percent, "memory_used": memory_info.used / (1024 ** 2)}  # MB 단위

@app.get("/process_byte")
def process_byte():
    with open("test.jpg", "rb") as f:
        img = f.read()
    memory_info = psutil.virtual_memory()
    return {"memory_percent": memory_info.percent, "memory_used": memory_info.used / (1024 ** 2)}  # MB 단위
