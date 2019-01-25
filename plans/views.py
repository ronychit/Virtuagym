from rest_framework import viewsets, status
from rest_framework.response import Response
from . import serializers
from .models import Exercise,Days,WorkoutPlan,PlanDaysExercise,User
from rest_framework.permissions import IsAuthenticated


class ExerciseViewSet(viewsets.ModelViewSet):
    """API for Exercise endpoint - Load,Add,Update,Remove Exercises"""
    permission_classes = (IsAuthenticated,)
    queryset = Exercise.objects.all()
    serializer_class = serializers.ExerciseSerializer

class DaysViewSet(viewsets.ModelViewSet):
    """API for Days endpoint - Load,Add,Update,Remove Days"""
    permission_classes = (IsAuthenticated,)
    queryset = Days.objects.all()
    serializer_class = serializers.DaysSerializer

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    """API for workout plan endpoint - Load,Add,Update,Remove Plans"""
    permission_classes = (IsAuthenticated,)
    queryset = WorkoutPlan.objects.all()
    serializer_class = serializers.WorkoutPlanSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API for User endpoint - Load,Add,Update,Remove User"""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    #Override create method for user password hashing.
    def create(self, request, *args, **kwargs):
        try:
            userdetails = request.data
            user_obj = User.objects.create(first_name=userdetails['first_name'],last_name=userdetails['last_name'],
                                       email=userdetails['email'])
            user_obj.set_password(userdetails['password'])
            user_obj.save()
            return Response("User created successfully",status=status.HTTP_201_CREATED)
        except Exception as e:
            return  Response("User not created, Error : " + repr(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserPlanViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """API for User Plans endpoint - Load,Add,Remove plans of a user"""
    queryset = User.objects.select_related().all()
    serializer_class = serializers.UserPlanSerializer

    #Override create method to add plans for a user.
    def create(self, request, *args, **kwargs):
        try:
            userPlans_data = request.data
            user_obj = User.objects.get(id=userPlans_data['id'])
            for plan in userPlans_data['plans']:
                plan_obj = WorkoutPlan.objects.get(id=plan)
                user_obj.plans.add(plan_obj)
            user_obj.save
            return Response("Plans added for user successfully", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response("Plans not added for the user, Error : " + repr(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #Override destroy method to remove plans for a user.
    def destroy(self, request, *args, **kwargs):
        try:
            userPlans_data = request.data
            user_obj = User.objects.get(id=userPlans_data['id'])
            for plan in userPlans_data['plans']:
                plan_obj = WorkoutPlan.objects.get(id=plan)
                user_obj.plans.remove(plan_obj)
            user_obj.save
            return Response("Plans removed for user successfully", status=status.HTTP_200_OK)
        except Exception as e:
            return Response("Plans not removed for the user, Error : " + repr(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PlanDaysDetailsViewSet(viewsets.ModelViewSet):
    """API for Plan days endpoint - Add,Delete days from a workout plan"""
    permission_classes = (IsAuthenticated,)
    queryset = PlanDaysExercise.objects.select_related().all()
    serializer_class = serializers.PlanDetailsSerializer

    def create(self, request, *args, **kwargs):
        try:
            planDays = PlanDaysExercise.objects.filter(plan=request.data['plan'],day=request.data['day'])
            if planDays.exists():
                return Response("Plan Details already present", status=status.HTTP_200_OK)
            else:
                plan = WorkoutPlan.objects.get(id=request.data['plan'])
                day = Days.objects.get(id=request.data['day'])
                plandetails = PlanDaysExercise.objects.create(plan = plan,day = day)
                for exercise_id in request.data['exercises']:
                    exercise = Exercise.objects.get(id=exercise_id)
                    plandetails.exercises.add(exercise)
                plandetails.save()
                return Response("Plans details added successfully", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response("Plan details not added, Error : " + repr(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            plandetails_obj = PlanDaysExercise.objects.filter(plan=request.data['plan'],day=request.data['day'])
            if plandetails_obj.exists():
                plandetails_obj.delete()
                return Response("Day removed from Plan successfully", status=status.HTTP_200_OK)
        except Exception as e:
            return Response("Day is not removed from Plan, Error : " + repr(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PlanExerciseDetailsViewSet(viewsets.ModelViewSet):
    """API for Plan Exercise endpoint - Add,Delete Exercises from a Day in workout plan"""
    permission_classes = (IsAuthenticated,)
    queryset = PlanDaysExercise.objects.select_related().all()
    serializer_class = serializers.PlanDetailsSerializer

    def create(self, request, *args, **kwargs):
        try:
            planDays = PlanDaysExercise.objects.filter(plan=request.data['plan'],day=request.data['day'])
            if planDays.exists():
                planDays_obj = PlanDaysExercise.objects.get(plan=request.data['plan'], day=request.data['day'])
                for exercise_id in request.data['exercises']:
                    exercise = Exercise.objects.get(id=exercise_id)
                    planDays_obj.exercises.add(exercise)
                planDays_obj.save()
                return Response("Exercise details added in the plan successfully", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response("Exercise details not added, Error : " + repr(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)








