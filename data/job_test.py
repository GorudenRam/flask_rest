from requests import get, post, delete

print(get('http://localhost:8080/api/jobs').json())
print(get('http://localhost:8080/api/jobs/1').json())
print(get('http://localhost:8080/api/jobs/999').json())
print(get('http://localhost:8080/api/jobs/q').json())
print(post('http://localhost:8080/api/jobs').json())#пустой запрос
print(post('http://localhost:8080/api/jobs', json={'team_leader': 1}).json())  #отсутствие нужных полей
print(post('http://localhost:8080/api/jobs', json={'team_leader': 1, 'id': 1,
                                                   'job': 'nothing', 'work_size': 21,
                                                   'collaborators': '1, 2, 3',
                                                   'is_finished': False}).json())  #работа с существующим id
print(post('http://localhost:8080/api/jobs', json={'team_leader': 1, 'id': 100,
                                                   'job': 'nothing', 'work_size': 21,
                                                   'collaborators': '1, 2, 3',
                                                   'is_finished': False}).json())  #корректный запрос
print(get('http://localhost:8080/api/jobs').json())
print(delete('http://localhost:8080/api/jobs/70').json())
print(delete('http://localhost:8080/api/jobs/80').json())
print(delete('http://localhost:8080/api/jobs/90').json())
print(post('http://localhost:8080/api/jobs', json={'team_leader': 1, 'id': 100,
                                                   'job': 'nothing', 'work_size': 21,
                                                   'collaborators': '1, 2, 3',
                                                   'is_finished': False}).json())
print(delete('http://localhost:8080/api/jobs/100').json())


print(get('http://localhost:8080/api/jobs').json())