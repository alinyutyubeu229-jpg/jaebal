import requests
token="http://host8.dreamhack.games:17456/token.php"
result="http://host8.dreamhack.games:17456/high-scores.php"
s=requests.session()
#토큰 받기
r=s.get(token)
token=r.text
print(token)

data={
    "token":token,
    "score":31337
}
response=s.post(result,data=data)
print(response.text)
