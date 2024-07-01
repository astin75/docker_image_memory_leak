#!/bin/bash

# Docker 이미지 빌드
docker build -t memory-usage .

# 엔드포인트 목록
endpoints=(
    "process_opencv opencv"
    "process_opencv_rgb opencv_rgb"
    "process_pillow pillow"
    "process_pillow_rgb pillow_rgb"
    "process_byte byte"
)

# 각 엔드포인트에 대해 컨테이너 실행, 클라이언트 호출, 컨테이너 종료 및 삭제
for endpoint in "${endpoints[@]}"; do
    set -- $endpoint
    api=$1
    title=$2

    # Docker 컨테이너 실행
    docker run -d --name memory-usage-container -p 8000:8000 -v $(pwd)/output:/app/output memory-usage

    # 클라이언트 스크립트 실행
    python client.py $api $title

    # 컨테이너 중지 및 제거
    docker stop memory-usage-container
    docker rm memory-usage-container
done
