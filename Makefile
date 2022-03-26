install:
	pip install -r requirements.txt
format:
	autopep8 --in-place --aggressive --aggressive  *.py
lint:
	pylint *.py
test:
	coverage run -m "py.test" . -v
	coverage html 
	coverage report 
start:
	main.py -c 0,0 0,1 0,2 1,2 2,1
clean:
	rm -rf .venv
	find . -iname "*.pyc" -delete
	coverage erase