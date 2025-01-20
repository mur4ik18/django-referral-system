<div align="center" id="top"> 
  <img src="https://www.tivix.com/wp-content/uploads/2017/01/django-logo-negative-1-1110x0-c-default.png" alt="Djang Referral System" />

  &#xa0;

  <!-- <a href="https://djangreferralsystem.netlify.app">Demo</a> -->
</div>

<h1 align="center">Django Referral System</h1>

<p align="center">
  <img alt="Github language" src="https://img.shields.io/github/languages/top/mur4ik18/django-referral-system?color=success">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/mur4ik18/django-referral-system?color=success">
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Djang Referral System 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/mur4ik18" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

I created django referral system and I wanna show it for other people! If you wanna contrib you are welcome! 

## :sparkles: Features ##

:heavy_check_mark: New user can signUp only with referral code;\
:heavy_check_mark: Each new user get 3 referral codes for friends;\
:heavy_check_mark: Each new admin get 5 referral codes;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Djano Rest Framework](https://www.django-rest-framework.org/)
- [Djoser](https://djoser.readthedocs.io/en/latest/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) + [Poetry](https://python-poetry.org/) installed.
In the project I used postgresql, you need to start postgresql so you need [Docker-compose](https://docs.docker.com/compose/).

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/mur4ik18/django-referral-system && cd django-referral-system

# Install dependencies
$ poetry install

# Run env
$ poetry shell

# Run postgresql (If you don't have)
$ docker-compose -f db.yml up --build -d

# Start project
$ python src/manage.py runserver
```

## :checkered_flag: Works with api ##
### Create account: ###
```
POST http://127.0.0.1:8000/auth/jwt/create/
body={
"username":"admin",
"password":"admin"
}
```
It return:
```
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```
### Get tokens list: ###
```
GET http://127.0.0.1:8000/api/v1/get_tokens/
Headers={
"Authorization":"JWT access_token",
}
```
It return:
```
[
    {
        "token": "w3iP8GJt1woqLRM6MNrNx88JxuI",
        "user": 1,
        "refer_relations": [
	   {
	    "employer": 1,
	    "employee": 10,
	    "refer_token": 1
            }
	]
    },
    {
        "token": "E6VQuA4qFucR028UW0XL6FAW8vw",
        "user": 1,
        "refer_relations": []
    },
    ...
]
```
### Create new account: ###
```
POST http://127.0.0.1:8000/auth/users/
body={
"username":"user",
"password":"password1",
"email":"user@gmail.com",
"referral_token":"E6VQuA4qFucR028UW0XL6FAW8vw",
}
```
It return:
```
{
    "referral_token": "E6VQuA4qFucR028UW0XL6FAW8vw",
    "email": "test@test.com1",
    "username": "test1sdas",
    "id": 11
}
```

## :memo: License ##
Made with :heart: by <a href="https://github.com/mur4ik18" target="_blank">mur4ik18</a>

&#xa0;

<a href="#top">Back to top</a>
