from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    objective = models.TextField()


class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year_of_passing = models.CharField(max_length=4)
    grade = models.CharField(max_length=10)


class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experience', on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Skill(models.Model):
    resume = models.ForeignKey(Resume, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class create(models.Model):
    create=models.FileField(upload_to='files/')

class LoginData(models.Model):
    # username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(blank=True,unique=True)
    # phone=models.CharField(max_length=15)

    def __str__(self):
        return self.email
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField()
    phone=models.CharField(max_length=15)
    feedback=models.TextField()
    
    def __str__(self):
        return self.name