from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager

# Create your models here.
class Exercise(models.Model):
    """Model for Excercise"""
    exercise_name = models.CharField(max_length=200)

    def __str__(self):
        return self.exercise_name

class Days(models.Model):
    """Model for Days in a workout plan"""
    day_number = models.IntegerField()

    def __str__(self):
        return str(self.day_number)

class WorkoutPlan(models.Model):
    """Model for Workout plans"""
    plan_name = models.CharField(max_length=200)

class User(AbstractBaseUser):
    """Model for user"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100,unique=True,null=False)
    plans = models.ManyToManyField(WorkoutPlan)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

class PlanDaysExercise(models.Model):
    """Model for Workout plan details"""
    plan = models.ForeignKey(WorkoutPlan,on_delete=models.CASCADE)
    day = models.ForeignKey(Days,on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)



