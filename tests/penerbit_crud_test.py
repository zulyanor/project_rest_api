# import json
# from . import app, client, cache, create_token, create_token_internal

# class TestinternalCrud():

# ######### get list
#     def test_book_list(self, client):
#         token = create_token()
#         res = client.get('/rent',
#                         headers={'Authorization': 'Bearer ' + token})
        
#         res_json=json.loads(res.data)
#         assert res.status_code == 200

#     def test_book_invalid_list(self, client):
#         token = create_token_internal()
#         res = client.get('/rent', 
#                         headers={'Authorization': 'Bearer ' + token})
#         res_json=json.loads(res.data)
#         assert res.status_code == 403

# ######### get
#     def test_rent_get(self, client):
#         token = create_token()
#         res = client.get('/rent/4',
#                         headers={'Authorization': 'Bearer ' + token})
        
#         res_json=json.loads(res.data)
#         assert res.status_code == 200

#     def test_rent_invalid_get(self, client):
#         token = create_token()
#         res = client.get('/rent/3', 
#                         headers={'Authorization': 'Bearer ' + token})
#         res_json=json.loads(res.data)
#         assert res.status_code == 404

# ######### post

#     def test_rent_input(self, client):
#         token = create_token()
#         data = {
#         "book_id": 3,
#         "user_id": 2
#         }
#         res=client.post('/rent', 
#                         headers={'Authorization': 'Bearer ' + token},
#                         data=json.dumps(data),
#                         content_type='application/json')

#         res_json=json.loads(res.data)

#         assert res.status_code == 200


#     def test_rent_invalid_input(self, client):
#         token = create_token()
#         data = {
#         "book_id": 2,
#         "user_id": 3
#         }
#         res=client.post('/rent', 
#                         headers={'Authorization': 'Bearer ' + token},
#                         data=json.dumps(data),
#                         content_type='application/json')

#         res_json=json.loads(res.data)
#         assert res.status_code == 500

