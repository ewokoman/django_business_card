from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Owner(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Comment(models.Model):
    comment_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text[:10]


class Projects(models.Model):
    name = models.CharField(max_length=100, default='NAme')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    comment_text = models.CharField(max_length=400)
    date_start = models.DateTimeField('date start')
    date_end = models.DateTimeField('date end')

    def __str__(self):
        return self.comment_text[:10]


class Owner_site(models.Model):
    first_name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', blank=True)
    last_name = models.CharField(max_length=10)
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    about = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Contacts(models.Model):
    name = models.CharField(max_length=150)
    link = models.URLField()
    name_icon_fa = models.CharField(
        max_length=100, default='fa-regular fa-envelope')
    owner_site = models.ForeignKey(Owner_site, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
