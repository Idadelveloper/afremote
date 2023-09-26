from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


class Education(models.Model):
    school = models.CharField(max_length=80)
    qualification = models.CharField(max_length=30)
    study_area = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.school + " - " + self.qualification


class Experience(models.Model):
    company = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.company + " - " + self.role
        
class JobHunterProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    education = models.ForeignKey(
        Education,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE,
    )
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





# class Skills(models.Model):
#     skills = ArrayField(
#         models.CharField(max_length=20),
#         size=15
#     )
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )

#     def __str__(self):
#         return self.skills


# class Interest(models.Model):
#     interests = ArrayField(
#         models.CharField(),
#         size=5
#     )
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )

#     def __str__(self):
#         return self.interests




