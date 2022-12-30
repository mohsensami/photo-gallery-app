# Photo Gallery

* This is a photo gallery app 

## You have to follow following steps to run this project

### 1. Run this command on your terminal 
       1. git clone https://github.com/mohsensami/photo-gallery-app.git
       2. cd photo-gallery-app
### 2. Create virtual enviroment to install required libraries 
       1. pip install virtualenv
       2. virtualenv venv
       3. pip install -r requirements.txt
### 3. Run the project
       1. python manage.py makemigrations
       2. python manage.py migrate
       3. python manage.py createsuperuser
       4. python manage.py runserver
### 4. Access Admin Page
open this link on your browser `http://127.0.0.1:8000/`

* To Access Admin Page goto `http://127.0.0.1:8000/admin` and enter `username` and `password` of your superuser
### 5. See Demo here
`https://imgsami.pythonanywhere.com`

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Gallery Page
</p>
<img src="https://github.com/mohsensami/photo-gallery-app/blob/main/screenshot/screenshot1.png?raw=true">
</td> 
<td width="50%">
<br>
<p align="center">
  LightBox
</p>
<img src="https://github.com/mohsensami/photo-gallery-app/blob/main/screenshot/screenshot2.png?raw=true">  
</td>
</table>