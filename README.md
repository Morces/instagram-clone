# instagram-clone
>[MOSES KARANI](https"//github.com/Morces)

## Description  
This is a clone of  Instagram where people share their  images and videos for other users to view. 
Users can sign up, login, view and post photos, search and follow other users.

## Screenshot 
### Homepage

![instagram](https://user-images.githubusercontent.com/97943808/172605450-7fe3bbe5-0fd4-4839-ab53-c006f7362c33.png)
### User Story
One should be able to:
* Sign in to the application to start using.  
* Upload a pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline.  

### Setup Instructions

Clone the repo
```bash
https://github.com/Morces/instagram-clone.git
```
Navigate into the cloned repo
```bash
cd instagram-clone 
```
Install and activate venv
```bash
- python3 -m venv virtual - source virtual/bin/activate
- pip install -r requirements.txt
```
Set up database, host the and migrate.
```bash
python3 manage.py makemigrations migram
```
Migrate
```bash
python3 manage.py migrate
```

Run the application
```bash
python3 manage.py runserver
```

### Technologies Used
- Django4.0 - for development of the application.
- Heroku -  for deployment.
- Git - for version control

### Contibutions and Support
Pull Requests are welcomed

### Contact information 
Reach me through email [karanim594@gmail.com]

### License
[MIT license](https://github.com/Morces/instagram-clone/blob/master/LICENSE)
