from django.db import models

# Create your models here.
class Book(models.Model):
    READ = 1
    UNREAD = 2
    READING = 3
    BOOK_STATUS = (
        (READ, 'Read'),
        (UNREAD, 'Unread'),
        (READING,'Reading'),
    )

    REVIEW = (
        ('Good','Good'),
        ('Fair','Fair'),
        ('Bad','Bad'),
    )
    user=models.ForeignKey('auth.user',on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30, blank=True)
    pages = models.IntegerField(blank=True, null=True)
    review = models.CharField(choices=REVIEW,max_length=4)
    book_status = models.PositiveSmallIntegerField(choices=BOOK_STATUS)

    def __str__(self):
        return self.title +' '+ 'by' +' '+ self.author