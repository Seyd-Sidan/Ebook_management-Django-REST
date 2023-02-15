DJANGO EBOOK MANAGEMENT API

Steps to Run:

1. Create a virtual environment to install dependencies in and activate it

2. Run the Command: "pip3 install -r requirements.txt"

3. Run the commands: "python manage.py makemigrations" and after that "python manage.py migrate"

4. Python manage.py Runserver
    - After running the above command we get a url for running the api in localhost 
    - The URL is : "http://127.0.0.1:8000"

Testing Using Postman
---------------------
4. Register User -
    - User-registration-URL : "http://127.0.0.1:8000/register/"
    - Open Postman and enter the registration-URL in the url section
    - Select the request method as POST
    - Enter the User Details in the body section in JSON format
    - Click on the Send Button to register the user
    - If Succesfull a "Registration Succesfull" message Response will be recieved

5. Login - 
    - Login-url : "http://127.0.0.1:8000/login/"
    - Enter this URL in the URL Section in Postman
    - Select the request method as POST
    - Enter the username and password and click on the Send Button
    - If the Login is Succesfull, a Token will be generated and will be given as a response
    - This token will be used to Authenticate the user for the ebook CRUD operations

4. CRUD Operation - 
    - ebooks_list_url = "http://127.0.0.1:8000/all" 
        - Add paramaters if required
        - Add the Token recieved in the header section with the Key as "Authorization"
        - Ex: url = "http://127.0.0.1:8000/all?title=title_name"
        - Select the request method as GET
        - If Successfull, the Response will include the Ebook Data

    - ebooks_create_url = "http://127.0.0.1:8000/create/" 
        - Add data to the Body Section in JSON Format
        - Add the Token recieved in the header section with the Key as "Authorization"
        - Select the request method as POST
        - If Succesfull, the Response will be "Ebook Added Succesfully"

    - ebooks_update_url = "http://127.0.0.1:8000/update/" 
        - updates the data based on the ebook title
        - Add the Token recieved in the header section with the Key as "Authorization"
        - Select the request method as PUT
        - If Successfull, the Response will be "Ebook Updated Succesfully"

    - ebooks_delete_url = "http://127.0.0.1:8000/ebook/<id>/delete" 
        - add the id of the ebook you want to delete
        - Add the Token recieved in the header section with the Key as "Authorization"
        - Select the request method as DELETE
        - If Successfull, the Response will be "Deleted Succesfully"

    - Add the Required URL in the URL Section of the Postman
    - Add Data in the Body section for Create and Update Operations

Testing Using Python Scripts
----------------------------
#After following the First four steps
#Run the test.py python script for testing
----------------------------
1. Install Requests Library
2. data = {"username":"enter_username",
            "password":"enter_password"}
3. Register the user - 
    - Response_variable = requests.post("http://127.0.0.1:8000/register/",json=data)

4. Login - 
    - Response_variable = requests.post("http://127.0.0.1:8000/login/",json=data)
    - the Response_variable will have the token

5. CRUD -
    - URL = "Enter the Required Url"
    - data = {EBOOK_DATA}
    - header = {"Authorization": "Token <token>"}
    - Response_variable = requests.request_method(URL,json=data,headers=header)
    - Print Response_variable.json()
