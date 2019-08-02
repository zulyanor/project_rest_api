# import json
# from . import app, client, cache, create_token, create_token_internal

# class TestApiluarCrud():    
    
#     def test_apiluar_get(self, client):
#         token = create_token()
#         res = client.get('/apiluar',
#                         headers={'Authorization': 'Bearer ' + token})
        
#         res_json=json.loads(res.data)
#         assert res.status_code == 200

#     def test_apiluar_invalid_get(self, client):
#         token = create_token()
#         res = client.get('/apiluar', 
#                         headers={'Authorization': 'Bearer ' + token})
#         res_json=json.loads(res.data)
#         assert res.status_code == 404