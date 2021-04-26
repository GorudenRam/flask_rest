from requests import get, post, delete


print(post('http://localhost:8080/api/v2/jobs', json={'team_leader': 1, 'id': 100,
                                                   'job': 'nothing', 'work_size': 21,
                                                   'collaborators': '1, 2, 3',
                                                   'is_finished': False}).json())
print(get('http://localhost:8080/api/v2/jobs/').json())
print(get('http://localhost:8080/api/v2/jobs/1').json())
print(get('http://localhost:8080/api/v2/jobs/999').json())
print(get('http://localhost:8080/api/v2/jobs/q').json())
print(post('http://localhost:8080/api/v2/jobs/').json())
print(post('http://localhost:8080/api/v2/jobs', json={'team_leader': 1}).json())
print(post('http://localhost:8080/api/v2/jobs', json={'team_leader': 1, 'id': 1,
                                                   'job': 'nothing', 'work_size': 21,
                                                   'collaborators': '1, 2, 3',
                                                   'is_finished': False}).json())
print(post('http://localhost:8080/api/v2/jobs', json={'team_leader': 1, 'id': 100,
                                                   'job': 'nothing', 'work_size': 21,
                                                   'collaborators': '1, 2, 3',
                                                   'is_finished': False}).json())
print(get('http://localhost:8080/api/v2/jobs/').json())
print(delete('http://localhost:8080/api/v2/jobs/70').json())
print(delete('http://localhost:8080/api/v2/jobs/80').json())
print(delete('http://localhost:8080/api/v2/jobs/90').json())
print(delete('http://localhost:8080/api/v2/jobs/100').json())
print(get('http://localhost:8080/api/v2/jobs').json())