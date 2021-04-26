from requests import get, post, delete, put


print(post('http://localhost:8080/api/v2/users', json={'id': '11', 'surname': 'West', 'name': 'Kanye', 'age': '21',
                                                       'position': 'worker', 'speciality': 'research engineer',
                                                       'address': 'module_1', 'email': 'scot@mars.org',
                                                       'password': '123'}).json())
print(post('http://localhost:8080/api/v2/users', json={'id': '1', 'surname': 'West', 'name': 'Kanye', 'age': '21',
                                                       'position': 'worker', 'speciality': 'research engineer',
                                                       'address': 'module_1', 'email': 'scot@mars.org',
                                                       'password': '123'}).json())
print(post('http://localhost:8080/api/v2/users', json={'id': '10', 'name': 'Kanye', 'age': '21',
                                                       'position': 'worker', 'speciality': 'research engineer',
                                                       'address': 'module_1', 'email': 'scot@mars.org',
                                                       'password': '123'}).json())
print(post('http://localhost:8080/api/v2/users').json())
print(get('http://localhost:8080/api/v2/users/1').json())
print(get('http://localhost:8080/api/v2/users/12').json())
print(get('http://localhost:8080/api/v2/users/h').json())
print(delete('http://localhost:8080/api/v2/users/11').json())
print(delete('http://localhost:8080/api/v2/users/11').json())
print(delete('http://localhost:8080/api/v2/users/h').json())
