import json
from . import app, client, cache, create_token, create_token_internal

class TestClientCrud():
    var_id = 0

######### get list
    def test_client_list(self, client):
        token = create_token()
        res = client.get('/client/list',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_client_invalid_list(self, client):
        token = create_token()
        res = client.get('/client/list1', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### get
    def test_client_get(self, client):
        token = create_token()
        res = client.get('/client/7',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_client_invalid_get(self, client):
        token = create_token()
        res = client.get('/client/100', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### post

    def test_client_input(self, client):
        token = create_token()
        data = {
        "client_key": "zulyanoooooo",
        "client_secret": "ganteng123123",
        "status": 0 
        }
        res=client.post('/client', 
                        data=json.dumps(data),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)
        print(res_json)
        TestClientCrud.var_id = res_json['client_id']

        assert res.status_code == 200


    def test_client_invalid_input(self, client):
        token = create_token()
        data = {
        "client_secret": "secret",
        "status": 1
        }
        res=client.post('/client', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400

######### PUT

    def test_client_put(self, client):
        token = create_token()
        data = {
        "client_key": 1,
        "client_secret": 1,
        "status": 0
        }
        res=client.put('/client/7', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_client_invalid_put(self, client):
        token = create_token()
        data = {
        "per_page": 1,
        "keywords":"AUL"
        }
        res=client.put('/client/1000', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400


######### delete
    def test_user_delete(self, client):
        token = create_token_internal()
        res=client.delete('client/' +str(TestClientCrud.var_id), 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_user_invalid_delete(self, client):
        token = create_token_internal()
        res=client.delete('client/100', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 404

        