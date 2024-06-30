#!/bin/bash

# Docker 이미지 빌드
docker build -t memory-usage .

# OpenCV 작업 실행
docker run --rm -v $(pwd)/output:/app/output --name memory-usage-opencv memory-usage poetry run python -c "from main import run_opencv; run_opencv()"

# OpenCV RGB 작업 실행
docker run --rm -v $(pwd)/output:/app/output --name memory-usage-opencv memory-usage poetry run python -c "from main import run_opencv_rgb; run_opencv_rgb()"

# Pillow 작업 실행
docker run --rm -v $(pwd)/output:/app/output --name memory-usage-pillow memory-usage poetry run python -c "from main import run_pillow; run_pillow()"

# Pillow RGB 작업 실행
docker run --rm -v $(pwd)/output:/app/output --name memory-usage-pillow memory-usage poetry run python -c "from main import run_pillow_convert_rgb; run_pillow_convert_rgb()"


# Byte 작업 실행
docker run --rm -v $(pwd)/output:/app/output --name memory-usage-byte memory-usage poetry run python -c "from main import run_byte; run_byte()"
