from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from books.models import ebook
from django.contrib.auth.models import User
from books.serializers import booksserializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


# USER REGISTRATION
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    user = JSONParser().parse(request)
    try:
        if User.objects.filter(username=user['username']).exists():
            return Response("User already Exists")
        else:
            user_reg = User.objects.create_user(username=user['username'], password=user['password'])
            user_reg.save()
            return Response("Registration Successfull")
    except:
        return Response("Registration Failed")


# USER LOGIN
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response("Please provide both Username and Password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response("Invalid Credentials")
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


# INDEX PAGE
@csrf_exempt
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_ebooks': '/',
        'Search by title': '/?title=title_name',
        'Add': '/create',
        'Update': '/update/title_name',
        'Delete': '/ebook/id/delete'
    }
    return Response(api_urls)


# ADD EBOOKS
@csrf_exempt
@api_view(['POST'])
def add_items(request):
    ebook_data = JSONParser().parse(request)
    if ebook.objects.filter(title=ebook_data['title']).exists():
        return Response("This Ebook Already Exist")
    books_serializer = booksserializer(data=ebook_data)
    if books_serializer.is_valid():
        books_serializer.save()
        return Response("Ebook Added Succesfully")
    return Response("Failed to Add")


# LIST EBOOKS
@csrf_exempt
@api_view(['GET'])
def view_items(request):
    if request.query_params:
        books = ebook.objects.filter(**request.query_params.dict())
    else:
        books = ebook.objects.all()
    books_serializer = booksserializer(books, many=True)
    # return JsonResponse(books_serializer.data,safe=False)
    return Response(books_serializer.data)


# UPDATE EBOOKS
@csrf_exempt
@api_view(['PUT'])
def update_items(request):
    ebook_data = JSONParser().parse(request)
    book = ebook.objects.get(title=ebook_data['title'])
    if book:
        books_serializer = booksserializer(book, data=ebook_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return Response("Ebook Updated Succesfully")
        return Response("Failed to Update")
    else:
        return Response("This E-Book does not exist. Please create a new One.")


# DELETE EBOOKS
@csrf_exempt
@api_view(['DELETE'])
def delete_items(request, pk):
    book = ebook.objects.get(id=pk)
    book.delete()
    return Response('Deleted Succesfully')
