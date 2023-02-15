import requests

#API URLS
#---------------------------------------
registration_url = "http://127.0.0.1:8000/register/"
login_url = "http://127.0.0.1:8000/login/"
ebooks_list_url = "http://127.0.0.1:8000/all" #add paramaters if required
ebooks_create_url = "http://127.0.0.1:8000/create/" #add fields as necessary
ebooks_update_url = "http://127.0.0.1:8000/update/" #add changes based on the ebook title
ebooks_delete_url = "http://127.0.0.1:8000/ebook/<id>/delete" #add the id of the ebook you want to delete

auth_= {"username":"David",
        "password":"david@123"}

#REGISTER USER
#-----------------------------
# r1 = requests.post(registration_url,json=auth_)
# token = r1.json()['token']
# print("Token :"+token)


r1 = requests.post(login_url,json=auth_)
token = r1.json()['token']
print("\nToken :"+token+"\n")

header = {'Authorization':"Token "+token}

r2 = requests.get(ebooks_list_url+"?title=The Alchemist",headers=header)
print(r2.json())

#INSERT EBOOK
#----------------------------
# ebook_data = {"id": 1,
#               "title": "The Alchemist",
#               "author": "Paulo Coelho",
#               "genre": "mystery",
#               "review": 4,
#               "favourite": True}

# r3 = requests.post(ebooks_create_url,json=ebook_data,headers=header)
# print(r3.json())

#UPDATE EBOOK
#-------------------------
# ebook_data = {"id": 1,
#               "title": "The Alchemist",
#               "author": "xyz",
#               "genre": "Science_Fiction",
#               "review": 5,
#               "favourite": True}

# r3 = requests.post(ebooks_update_url,json=ebook_data,headers=header)
# print(r3.json())

#DELETE EBOOK
#------------------
#r4 = requests.delete("http://127.0.0.1:8000/ebook/1/delete",headers=header)
#print(r4.json())