Create a python virtual environment with version 3.8 and activate it

python3.8 -m venv env
source env/bin/activate

install the dependencies

pip install -r requirements.txt

usage: python app.py -r <records per page> -f <file name>
Iterates through all the available pages and save the result in a .csv file.

usage2: python app.py -u <user id>
Returns the user who matches the user id specified
