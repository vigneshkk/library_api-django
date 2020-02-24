from django.db import models

class Books(models.Model):
	isbn = models.IntegerField(primary_key=True)
	book_name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	no_of_actual_copies=models.IntegerField(default=0)
	no_of_cuurent_copies=models.IntegerField(default=0)


	def __str__(self):
		return str(self.isbn)


class Borrower(models.Model):
	borrower_id=models.IntegerField(primary_key=True)
	isbn = models.ForeignKey(Books, on_delete=models.CASCADE)
	from_date = models.DateField()
	to_date = models.DateField()
	return_date=models.DateField(blank=True,null=True)

	def __str__(self):
		return str(self.borrower_id)
