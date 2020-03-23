import requests
import json

headers = {}

payload = {
    "token" : "ya29.a0Adw1xeX4GDBf0S8BQCunefNIMBk2qbeI3i3q8WZ52E_UrRsSxZWLau6N386TE_8zwyq0gYM8KK1UKkrSkTJYqreIYjugUQI4f_33FXg1yZFsSYBuRn5-oaQEk_fRvtUmNZmZJAGZ5c06lvw0qtL5mLga32wqw4JJYow"
    }

# headers["content-type"] = "application/json"

headers["Authorization"] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg0OTYyMzgyLCJqdGkiOiJlZWMxMTlmYTcwMjA0NmFmYWZmZGNlMjI4NDk4NWFhOSIsInVzZXJfaWQiOjN9.Qu1mNgzIzt7F37CJCSXla0NDa3UpPVfIwdPVTLmu7kQ'

r = requests.get('http://localhost:8000/app/category', headers=headers)

# r = requests.post('http://localhost:8000/google/',data=json.dumps(payload) , headers=headers)

print(r.text)
