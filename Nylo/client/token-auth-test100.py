import requests

def client():



    data = {
        "username": "viviana",
        "password1": "cambiami12",
        "password2": "cambiami12",
        "email": "viviana@rest.com"
    }





    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
                            data=data)


    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()
