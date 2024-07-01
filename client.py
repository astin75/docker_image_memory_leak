import requests
import matplotlib.pyplot as plt
from datetime import datetime
import time

EPOCH = 2000
SERVER_URL = "http://localhost:8000"

def call_api(endpoint):
    response = requests.get(f"{SERVER_URL}/{endpoint}")
    data = response.json()
    return data["memory_percent"], data["memory_used"]

def collect_data(endpoint):
    timestamps = []
    memory_usages = []
    memory_actuals = []

    for _ in range(EPOCH):
        timestamp = datetime.now()
        memory_percent, memory_used = call_api(endpoint)
        timestamps.append(timestamp)
        memory_usages.append(memory_percent)
        memory_actuals.append(memory_used)
        time.sleep(0.01)  # 약간의 지연을 추가하여 서버 과부하 방지

    return timestamps, memory_usages, memory_actuals

def save_fig(timestamps, memory_usages, memory_actuals, title):
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
    plt.title(f'[FASTAPI] Memory Usage Over Time during {title.capitalize()} Processing')
    plt.grid(True)
    plt.xticks(rotation=45)
    image_path = f"output/memory_usage_{title}_{EPOCH}.png"
    plt.savefig(image_path)
    plt.close(fig)

def main(endpoint, title):
    timestamps, memory_usages, memory_actuals = collect_data(endpoint)
    save_fig(timestamps, memory_usages, memory_actuals, title)

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
