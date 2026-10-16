VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

REQUIREMENTS = requirements.txt

OUTPUT = params.json

all: $(VENV)

$(VENV): $(REQUIREMENTS)
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQUIREMENTS)
	@touch $(VENV)

train: $(VENV)
	$(PYTHON) train.py

predict: $(VENV)
	$(PYTHON) predict.py

plot: $(VENV)
	$(PYTHON) plot.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

fclean: clean
	rm -rf $(OUTPUT) $(VENV)

re: fclean all
	
.PHONY: all train predict plot clean fclean re
