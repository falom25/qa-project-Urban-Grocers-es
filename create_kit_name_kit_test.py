import sender_stand_request
import data

auth_token = sender_stand_request.get_auth_token(data.user_body)

def test_create_kit_one_characte():
    kit_body = {"name": "a"}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_create_kit_long_name():
    long_name = "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    kit_body = {"name": long_name}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_create_kit_empty_name():
    kit_body = {"name": ""}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)

    assert kit_response.status_code == 400

def test_create_kit_long_name_exceeds_limit():
    long_name = "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    kit_body = {"name": long_name}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)

    assert kit_response.status_code == 400

def test_create_kit_special_characters():
    kit_body = {"name": "№%@"}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_create_kit_with_spaces():
    kit_body = {"name": " A Aaa "}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_create_kit_with_numbers():
    kit_body = {"name": "123"}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_create_kit_missing_parameter():
    kit_body = {}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)

    assert kit_response.status_code == 400

def test_create_kit_wrong_parameter_type():
    kit_body = {"name": 123}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token)

    assert kit_response.status_code == 400