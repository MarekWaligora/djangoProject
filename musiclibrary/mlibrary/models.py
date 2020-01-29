from django.db import models

# Create your models here.
class Artist(models.Model):
   #lista stalych gdzie nie bedzie mozna wpisac niczego innego
    # UNITS=[
    #     ('pcs',"szt")
    # ]

    artName=models.CharField(max_length=200,verbose_name="Artist Name",unique=True)
    artKind=models.CharField(max_length=100,verbose_name="Kind of Music")
    artEstDate=models.DateTimeField(verbose_name="Raise Date")

    #classs Meta ?????
    def __str__(self):
        return self.artName



#to change columns' name  

class Album(models.Model):
    #foreign key artist PK
    albartist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    albname=models.CharField(max_length=100,verbose_name="Album Name")
    albreleasedate=models.DateTimeField(verbose_name="Relase Date")
    albmusickind=models.CharField(max_length=100,verbose_name="Music Kind")
    alblabel=models.CharField(max_length=100,verbose_name="Labelled by")
    albtype=models.CharField(max_length=50,verbose_name="carrier type")
    #currently borrowed or free
    albstatus=models.CharField(max_length=2,verbose_name="status"
    

    
    def __str__(self):
        return self.albName


class Borrow(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE,verbose_name="Album Id"),
    borrower=models.ForeignKey('Borrower',on_delete=models.CASCADE,verbose_name="Borrower ID")
    borrow_date=models.DateTimeField(verbose_name="Borrow Date")
    exp_return_date=models.DateTimeField(verbose_name="Expect Return Date")
    return_date=models.DateTimeField(verbose_name="Return Date")
    first_monit_date=models.DateTimeField(verbose_name="1st Monit Date")
    second_monit_date=models.DateTimeField(verbose_name="2nd Monit Date")
    

class Borrower(models.Model):
    brName=models.CharField(max_length=100,verbose_name="Name")
    brSurname=models.CharField(max_length=100,verbose_name="Surname")
    brMail=models.CharField(max_length=40,verbose_name="Mail")
    brPhone=models.CharField(max_length=20,verbose_name="Phone")
    brBorrow=models.ManyToManyField(
        Album,
        through='Borrow',
    )


    def __str__(self):
        return self.borName










