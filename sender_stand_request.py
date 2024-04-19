import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

#   Obtiene el token de autenticación para un nuevo usuario.
def get_auth_token(user_body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=user_body,
                             headers=data.headers)
    if response.status_code == 201 and "authToken" in response.json():
        return response.json()["authToken"]
    else:
        return None

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)