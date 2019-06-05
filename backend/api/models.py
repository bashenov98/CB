from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class ReviewManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class Review(models.Model):
    title = models.CharField(max_length=35)
    rating = models.IntegerField(range(1,5),)
    ip_address = models.CharField(max_length=20)
    summary = models.CharField(max_length=300, default=1)
    submissionDate = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    objects = ReviewManager()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)

    def to_json(self):
        return {
            'ids': self.id,
            'name': self.title,
            'rating': self.rating,
            'summary': self.summary,
            'ip_address': self.ip_address,
            'submission_date': self.submissionDate
        }
