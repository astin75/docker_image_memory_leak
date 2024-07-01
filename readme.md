docker build -t memory-usage .
docker run -d --name memory-usage-container -v $(pwd)/output:/app/output memory-usage
docker exec memory-usage-container poetry run python -c "from main import run_opencv; run_opencv()"
docker exec memory-usage-container poetry run python -c "from main import run_pillow; run_pillow()"
docker exec memory-usage-container poetry run python -c "from main import run_byte; run_byte()"


docker stop memory-usage-container
docker rm memory-usage-container
docker exec memory-usage-container poetry run python -c "from main import run_byte; run_byte()"
