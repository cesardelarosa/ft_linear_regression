VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

all: $(VENV)

$(VENV): requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@touch $(VENV)

train: $(VENV)
	$(PYTHON) train.py

predict: $(VENV)
	$(PYTHON) predict.py

clean:
	rm -f params.json
	rm -rf __pycache__

fclean: clean
	rm -rf $(VENV)

re: fclean all
	
.PHONY: all train predict clean fclean re
