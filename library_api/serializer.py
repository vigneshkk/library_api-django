from rest_framework import serializers
from .models import Books,Borrower


class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model= Books
		fields='__all__'

class BorrowerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Borrower
		fields='__all__'