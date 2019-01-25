
from rest_framework import serializers
from .models import  Exercise,Days,WorkoutPlan,PlanDaysExercise,User


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer class for Excercise Model Data"""
    class Meta:
        model = Exercise
        fields = ('id','exercise_name')

class DaysSerializer(serializers.ModelSerializer):
    """Serializer class for Days model Data"""
    class Meta:
        model = Days
        fields = ('id','day_number')

class WorkoutPlanSerializer(serializers.ModelSerializer):
    """Serializer class for Workout plan model data"""
    class Meta:
        model = WorkoutPlan
        fields = ('id','plan_name')

class UserSerializer(serializers.ModelSerializer):
    """Serializer class for User """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class UserPlanSerializer(serializers.ModelSerializer):
    """Serialzer class for User Plans"""
    plans = WorkoutPlanSerializer(many=True)
    class Meta:
        model = User
        fields = ('id','first_name','plans')


class PlanDetailsSerializer(serializers.ModelSerializer):
    """Serializer class for Plan details"""
    plan = WorkoutPlanSerializer
    day = DaysSerializer
    exercises = ExerciseSerializer(many=True)
    class Meta:
        model = PlanDaysExercise
        fields = ('id','plan', 'day','exercises')







