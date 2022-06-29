Create a python virtual environment with version 3.8 and activate it

### Installation

1. Clone o repositório

2. Crie um ambiente virtual python com a versão 3.8 e o ative
   ```sh
   python3.8 -m venv env
   ```

   ```sh
   source env/bin/activate
   ```

3. Instale as depedências
    ```sh
   pip install -r requirements.txt

### usage: python app.py -r "records per page" -f "file name"

Iterates through all the available pages and save the result in a .csv file.

### usage2: python app.py -u "user id"
Returns the user who matches the user id specified
