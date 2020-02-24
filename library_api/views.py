from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import json
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Books,Borrower
from django.views.generic.edit  import CreateView
from .serializer import BooksSerializer,BorrowerSerializer

def home(request):
    return render(request,'pages/index.html')


class BooksList(APIView):
	def get(self,request):
		book1=Books.objects.all()
		serializer1=BooksSerializer(book1,many=True)	
		return Response(serializer1.data)


	def post(self, request, *args, **kwargs):
		post=Books()
		data=json.loads(request.body)
		post.isbn=data.get('isbn')
		post.book_name=data.get('book_name')
		post.author=data.get('author')
		post.no_of_actual_copies=data.get('no_of_actual_copies')
		post.no_of_cuurent_copies=data.get('no_of_cuurent_copies')
		post.save()
		book1=Books.objects.all()
		serializer1=BooksSerializer(book1,many=True)	
		return Response(serializer1.data,  status=status.HTTP_201_CREATED)


	def put(self,request,*args,**kwargs):
		data=json.loads(request.body)
		update= Books.objects.get(isbn=data.get('isbn'))
		update.book_name=data.get('book_name')
		update.author=data.get('author')
		update.no_of_actual_copies=data.get('no_of_actual_copies')
		update.no_of_cuurent_copies=data.get('no_of_cuurent_copies')
		update.save()
		return redirect("/books")

	def delete(self,request,*args,**kwargs):
		data=json.loads(request.body)
		delet = Books.objects.get(isbn=data.get('isbn'))
		delet.delete()
		return redirect("/books")



class BorrowerList(APIView):
	def get(self,request):
		borrower1=Borrower.objects.all()
		borrower_serializer=BorrowerSerializer(borrower1,many=True)
		return Response(borrower_serializer.data)


	def post(self, request, *args, **kwargs):
		post=Borrower()
		data=json.loads(request.body)
		post.borrower_id=data.get('borrower_id')
		post.isbn=Books.objects.get(isbn=data.get('isbn'))
		post.from_date=data.get('from_date')
		post.to_date=data.get('to_date')
		post.save()
		book1=Books.objects.get(isbn=data.get('isbn'))
		book1.no_of_cuurent_copies-=1
		book1.save()
		return redirect("/borrower")


	def put(self,request,*args,**kwargs):
		data=json.loads(request.body)
		update= Borrower.objects.get(borrower_id=data.get('borrower_id'))
		update.isbn=Books.objects.get(isbn=data.get('isbn'))
		update.from_date=data.get('from_date')
		update.to_date=data.get('to_date')
		update.save()
		if(update.return_date !=data.get('return_date')):
			update.return_date=data.get('return_date')
			book1=Books.objects.get(isbn=data.get('isbn'))
			book1.no_of_cuurent_copies+=1
			book1.save()
		return redirect("/borrower")

	def delete(self,request,*args,**kwargs):
		data=json.loads(request.body)
		delet = Borrower.objects.get(borrower_id=data.get('borrower_id'))
		if(delet.return_date is None):
			messages.add_message(request, messages.INFO, 'Book is not returned')
			return redirect("/borrower")
		else:
			delet.delete()
			return redirect("/borrower")