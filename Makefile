create:
	python3 -m venv convertisseur_de_devise
run:
	cd bin source activate
start:
	python3 main.py
install:
	pip3 install -r requirement.txt
stop:
	deactivate