import cv2
from tqdm import tqdm
from PIL import Image
import psutil
import matplotlib.pyplot as plt
from datetime import datetime
import gc




EPOCH = 10000
def save_fig(timestamps: list, memory_usages: list, memory_actuals:list, title: str):

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
    image_path = f"output/memory_usage_{title}_{EPOCH}.png"  
    plt.savefig(image_path)      


def run_opencv():
    print("run_opencv")
    timestamps = []
    memory_usages = []    
    memory_actuals = []
    for i in tqdm(range(EPOCH)):
        img = cv2.imread("test.jpg")
        
        # 메모리 사용량 측정
        timestamps.append(datetime.now())
        memory_info = psutil.virtual_memory()
        memory_usages.append(memory_info.percent)
        memory_actuals.append(memory_info.used / (1024 ** 2))  # MB 단위
    
    save_fig(timestamps, memory_usages, memory_actuals, "opencv")
    print("run_opencv done")
    
def run_opencv_rgb():
    print("run_opencv_rgb")
    timestamps = []
    memory_usages = []    
    memory_actuals = []
    for i in tqdm(range(EPOCH)):
        img = cv2.imread("test.jpg")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        if i % 100 == 0:
            gc.collect()
        
        # 메모리 사용량 측정
        timestamps.append(datetime.now())
        memory_info = psutil.virtual_memory()
        memory_usages.append(memory_info.percent)
        memory_actuals.append(memory_info.used / (1024 ** 2))  # MB 단위
    
    save_fig(timestamps, memory_usages, memory_actuals, "opencv_rgb")
    print("run_opencv_rgb done")
 
        
def run_pillow():
    print("run_pillow")
    timestamps = []
    memory_usages = []      
    memory_actuals = []
    for i in tqdm(range(EPOCH)):
        img = Image.open("test.jpg")
        
        # 메모리 사용량 측정
        timestamps.append(datetime.now())
        memory_info = psutil.virtual_memory()
        memory_usages.append(memory_info.percent)
        memory_actuals.append(memory_info.used / (1024 ** 2))  # MB 단위

    save_fig(timestamps, memory_usages, memory_actuals, "pillow")  
    print("run_pillow done")    
    
def run_pillow_convert_rgb():
    print("run_pillow_rgb")
    timestamps = []
    memory_usages = []      
    memory_actuals = []
    
    for i in tqdm(range(EPOCH)):
        img = Image.open("test.jpg")
        img = img.convert("RGB")
        
        # 메모리 사용량 측정
        timestamps.append(datetime.now())
        memory_info = psutil.virtual_memory()
        memory_usages.append(memory_info.percent)
        memory_actuals.append(memory_info.used / (1024 ** 2))  # MB 단위

    save_fig(timestamps, memory_usages, memory_actuals, "run_pillow_rgb")  
    print("run_pillow_rgb done")       
        

def run_byte():
    print("run_byte")
    timestamps = []
    memory_usages = []   
    memory_actuals = []
       
    for i in tqdm(range(EPOCH)):
        with open("test.jpg", "rb") as f:
            img = f.read()
            
        # 메모리 사용량 측정
        timestamps.append(datetime.now())
        memory_info = psutil.virtual_memory()
        memory_usages.append(memory_info.percent)
        memory_actuals.append(memory_info.used / (1024 ** 2))  # MB 단위

    save_fig(timestamps, memory_usages, memory_actuals, "byte")    
    print("run_byte done")          
