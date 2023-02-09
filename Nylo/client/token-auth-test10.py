import requests

def client():
    token_h = 'Token 118ae12ebd6e87f248c328da6b79472942282394'
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/sellers/",
                            headers=headers)


    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()
