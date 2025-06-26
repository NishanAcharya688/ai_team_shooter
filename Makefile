# ai_team_shooter/Makefile
.PHONY: run train analyze

run:
	PYTHONPATH=${PWD} python src/main.py

train:
	PYTHONPATH=${PWD} python src/ai/train.py

analyze:
	PYTHONPATH=${PWD} python src/utils/analyze_logs.py

lint:
	flake8 src/ && mypy src/