# Virtuagym Application

This project is to develop an application to manage Workout plans and Users. APIs has been exposed to Load,Create,Update and Delete Workout Plans
and Users using Python Django rest framework.

### Getting Started

Virtuagym Application Backend code modules is available in 'Virtuagym' folder in Git Repository. Clone this repo
to test in your system.

### Prerequisites

1. Python v3.7

### Installing

1. Open cmd and go to the Virtuagym folder

2. Use the below command to install Python Django.

    ```pip install django```
    
3. Use the below command to install Django rest framework

    ```pip install djangorestframework```

4. Use the below command to install Django rest framework JWT module.

   ```pip install djangorestframework_simplejwt```
   
   
### Apply Migrations

1. Open cmd and go to the Virtuagym folder

2. Use the below command to make migrations.

   ```py manage.py makemigrations```
   
3. Use the below command to apply migrations.

   ```py manage.py migrate```


### Start Server

1. Go to the Virtuagym folder and start the Backend server using the below command.

    ```py manage.py runserver 8000```
