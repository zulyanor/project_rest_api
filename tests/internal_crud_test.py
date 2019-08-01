import json
from . import app, client, cache, create_token, create_token_internal

class TestInternalCrud():

######### get list
    def test_book_list(self, client):
        token = create_token_internal()
        res = client.get('/internal/buku',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_book_invalid_list(self, client):
        token = create_token()
        res = client.get('/internal/buku', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 403

######### get
    def test_book_get(self, client):
        token = create_token_internal()
        res = client.get('/internal/buku/4',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_book_invalid_get(self, client):
        token = create_token_internal()
        res = client.get('/internal/buku/3', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### post

    def test_book_input(self, client):
        token = create_token_internal()
        data = {
        "isbn": "123",
        "title": "COBA",
        "pengarang": "AUL",
        "penerbit": "PT AUL",
        "harga": 5000,
        "status": "show",
        "client_id": 1 
        }
        res=client.post('/internal/buku', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_book_invalid_input(self, client):
        token = create_token_internal()
        data = {
        "isbn": "123",
        "title": "COBA",
        "pengarang": "AUL",
        "penerbit": "PT AUL",
        "harga": 5000,
        "status": "show",
        "client_id": 1000
        }
        res=client.post('/internal/buku', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 500

######### PUT

    def test_book_put(self, client):
        token = create_token_internal()
        data = {
        "isbn": "123",
        "title": "COBA",
        "pengarang": "AUL",
        "penerbit": "PT AUL",
        "harga": 5000,
        "status": "show",
        "client_id": 1 
        }
        res=client.put('/internal/buku/1', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_book_invalid_put(self, client):
        token = create_token_internal()
        data = {
        "isbn": "123",
        "title": "COBA",
        "pengarang": "AUL",
        "penerbit": "PT AUL",
        "harga": 5000,
        "status": "show",
        "client_id": 1000
        }
        res=client.put('/internal/buku/1000, 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 500


######### delete
    def test_user_delete(self, client):
        token = create_token_internal()
        res=client.delete('internal/buku/1', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_user_invalid_delete(self, client):
        token = create_token_internal()
        res=client.delete('internal/buku/1', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 404

        