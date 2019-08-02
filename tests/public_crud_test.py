# import json
# from . import app, client, cache, create_token, create_token_internal

# class TestPublcCrud():

#     id = 0

# ######### get list
#     def test_book_list(self, client):
#         res = client.get('/public/book')        
#         res_json=json.loads(res.data)
#         assert res.status_code == 200

#     def test_book_invalid_list(self, client):
#         res = client.get('public/book')
#         res_json=json.loads(res.data)
#         assert res.status_code == 403
