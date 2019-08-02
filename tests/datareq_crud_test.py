import json
from . import app, client, cache, create_token, create_token_internal

class TestDatareqCrud():
    var_id = 0

######### get list
    def test_datareq_list(self, client):
        token = create_token()
        res = client.get('/datareq/list',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_datareq_invalid_list(self, client):
        token = create_token()
        res = client.get('/datareq/list1', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### get
    def test_datareq_get(self, client):
        token = create_token()
        res = client.get('/datareq/4',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_datareq_invalid_get(self, client):
        token = create_token()
        res = client.get('/datareq/100', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### post

    def test_datareq_input(self, client):
        token = create_token()
        data = {
        "page": 1,
        "per_page": 1,
        "keywords": "tester" 
        }
        res=client.post('/datareq', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        TestDatareqCrud.var_id = res_json['id']

        assert res.status_code == 200


    def test_datareq_invalid_input(self, client):
        token = create_token()
        data = {
        "per_page": "123",
        "keywords": "COBA"
        }
        res=client.post('/datareq', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400

######### PUT

    def test_datareq_put(self, client):
        token = create_token()
        data = {
        "page": 1,
        "per_page": 1,
        "keywords": "louis vuitton"
        }
        res=client.put('/datareq/2', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_datareq_invalid_put(self, client):
        token = create_token()
        data = {
        "per_page": 1,
        "keywords":"AUL"
        }
        res=client.put('/datareq/1000', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400


######### delete
    def test_user_delete(self, client):
        token = create_token_internal()
        res=client.delete(f'/datareq/{self.var_id}' , 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_user_invalid_delete(self, client):
        token = create_token_internal()
        res=client.delete('/datareq/100', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 404

