import requests

import csv

import argparse

def getSingleUser(id):
    url = 'https://reqres.in/api/users/' + id
    r = requests.get(url)
    status = r.status_code

    if(r.status_code == 200):
        data = r.json()['data']
        print(data['first_name'], data['last_name'])

    else:
        print('User ID does not exist')

def getUserList(records_per_page, file_name='users'):
    pageNumber = 1
    records = []

    while True:
        r = requests.get('https://reqres.in/api/users', params={'page': pageNumber})
        response = r.json()
        data = response['data']
        per_page = response['per_page']

        if not data:
            break

        for i in range(int(records_per_page)):
            if(i >= per_page):
                break
            records.append(data[i])
        pageNumber = pageNumber + 1

    header = ["id","email","first_name","last_name","avatar"]
    file_name = file_name + '.csv'
    try:
        with open(file_name, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write multiple rows
            for record in records:
                writer.writerow(list(record.values()))
    except Exception as e:
        print('Something went wrong while trying to write the file')
        print(e)
        return;
    else:
        print(file_name, ' created successfully')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retriving data from reqres api')
    parser.add_argument('-r','--records',  help='Records per page')
    parser.add_argument('-f','--file',  help='Output file name', default="users")
    parser.add_argument('-u','--user',  help='User id')
    args = parser.parse_args()

    if(args.records is not None):

        getUserList(args.records, args.file)

    elif(args.user is not None):
        getSingleUser(args.user)
