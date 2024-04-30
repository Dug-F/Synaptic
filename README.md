<a name="top"></a>
# Synaptic Multi-player Quiz Project

## Contents
1. [Problem](#problem)
2. [Solution](#solution)
3. [How To Use The App](#usage)
4. [What I Learned](#lessons)
5. [Tech Stack](#techStack)
6. [How To Install And Run Locally](#install)
7. [Attributions](#attributions)

<a name="#problem"></a>
# 1. Problem

I have a group of friends who meet up online every so often and one of the things we like to do is have a friendly and fun quiz.  We take it in turns to create and run the quiz.  At first we used Kahoot, but found it had some features which were somewhat limiting:
- if you leave the quiz for a while, it times out.  You cannot rejoin the quiz and retain your previous progress: you are joined as effectively a new user.
- it is the same if you get disconnected, e.g. you temporarily lose your wifi connection.  You cannot rejoin and retain your previous progress
- if the quiz host made a mistake when compiling the quiz and accidentally (or deliverately!) marked the wrong answer as correct, there is no way of correcting it
- the process of creating the quiz is not very friendly:
  - re-ordering questions is cumbersome
  - getting a summary of the questions and the questions marked as correct is not easy
 
- and so on

Being experienced in Python and Having recently studied Django I decided to write an alternative as a learning project.

The objectives were to:
- address all of the irritations identified above
- add some other fun features
- have fun and learn Django to a good level
- there was no requirement to create a mobile app, but the web app should be mobile-friendly

[Back to top](#top)

<hr>

<a name="solution"></a>
# 2. Solution

As per the brief, the solution was implemented using Django.  Since it is a real-time multi-player game, Django Channels was used as a layer on top of websockets to enable persistent two-way connection between the players and the server.

[Back to top](#top)

<hr>

<a name="usage"></a>
# 3. How To Use The App

TODO

[Back to top](#top)

<hr>

<a name="lessons"></a>
# 4. What I Learned

TODO

[Back to top](#top)

<hr>

<a name="techStack"></a>
# 5. Tech Stack

Python, Django, Django Channels, Redis, JavaScript, Ajax, Bootstrap, FontAwesome

[Back to top](#top)

<hr>

<a name="install"></a>
# 6. How To Install And Run Locally

## 6.1 Install Python
- make sure you have Python 3.10+ installed on your machine.  
- this app has not been tested with Python 3.10, only with 3.11.3
- the version of python installed and active determines the version that is used to build the virtual environment in the next step
	- so make sure that the version of Python you intend to use is active using `python --version`
- instructions for installing Python are [here](https://www.python.org/about/gettingstarted/)
## 6.2 Create virtual environment
- create new folder for project: synaptic
- `cd synaptic
- create virtual environment: `python -m venv venv`
- activate the virtual environment: `venv\Scripts\activate`

## 6.3 Clone the Github repo to the synaptic folder
- from the synaptic folder: `git clone https://github.com/Dug-F/Synaptic.git`
- change directory into the Synaptic folder: `cd Synaptic`

## 6.4 Install Python dependencies
- install the required python modules: `pip install -r requirements.txt`

## 6.5 Create a .env file
- the .env file contains secret details which are not published to Github
- you need to create your own version of .env
- create an empty .env file in /Synaptic (i.e. the same folder as manage.py)
- the key entries are shown in the `env_keys.txt` file
	- copy these keys into the .env file
- the keys then need to have values set for them:

>[!important] 
**the values for the keys must not have any surrounding quotes, otherwise they will not work correctly**
	
- for the SECRET_KEY, a new key can be generated using: `python manage.py generate_secret_key`
	- this prints a new secret key in the terminal window
	- copy and paste this new key after `SECRET_KEY=` in .env

- for the `EMAIL_USER=` and `EMAIL_PASS=` keys, these must be a valid email user and password
	- these are only used for sending password reset emails
	- for demo purposes, if you can live without resetting passwords, you can leave the values here empty
	- if you use a gmail address, you will probably need to enable ["less secure apps"](https://knowledge.workspace.google.com/kb/how-to-enable-less-secure-application-access-000006971)
	- it is recommended to set up a new dedicated email for this purpose

## 6.6 Build and initialise the database
- make the database migrations: `python manage.py makemigrations`
- apply the migrations: `python manage.py migrate`
- install the required database reference data: `python manage.py seed_data`
- if desired, add demo users
	- similarly to the .env file, demo users are kept in a secret file which is not in Github
	- create a new empty file `Synaptic/synaptic/management/commands/demo_users.py`
	- populate the contents with something like this:
		```python
		DEMO_USERS = [
		    {"username": "Player1", "email": "", "password": "synaptic#default"},
		    {"username": "Player2", "email": "", "password": "synaptic#default"},
		    {"username": "Player3", "email": "", "password": "synaptic#default"},
			{"username": "Player4", "email": "", "password": "synaptic#default"},
		]
		```
	- you can then create these users with `python manage.py create_demo_users`
	- any user can create a quiz, but they need to be the one who runs it
- alternatively, you can create users using the Register page when the app is up and running

>[!important]
>Only run `seed_data` and `create_demo_users` once to avoid the possibility of duplicate entries in the database

## 6.8 Install and run Redis

- Django Channels requires Redis to manage websocket communicationbetween multiple clients
- Redis does not natively run on all platforms
- probably the easiest way to install and run Redis is by using Docker
- install Docker Desktop by following the instructions [here](https://www.docker.com/products/docker-desktop/)
	- you wil probably need to re-start your machine to complete the installation
 - once Docker is installed, you can install and run a Redis in a container with `docker run --rm -p 6379:6379 redis:7-alpine`

## 6.7 Start the database
- you should now be able to start the server: `python manage.py runserver`
	- if it starts successfully, the terminal log should look something like this:
		```bash
		Performing system checks...
		
		System check identified no issues (0 silenced).
		April 29, 2024 - 21:26:15
		Django version 5.0.4, using settings 'quiz.settings'
		Starting ASGI/Daphne version 4.1.2 development server at http://127.0.0.1:8000/
		Quit the server with CTRL-BREAK.
		```
- you can now access the synaptic app from a browser by clicking [here](http://localhost:8000/synaptic) or [here](http://127.0.0.1:8000/synaptic) or entering `http://localhost:8000/synaptic` or `http://127.0.0.1:8000/synaptic`in the address bar
- log in with one of the users you created earlier, or register a new user

[Back to top](#top)

<hr>

<a name="attributions"></a>
## 7. Attributions

Attributions for the images used in the demo quiz:

- Batman: Photo by [Marcin Lukasik](https://unsplash.com/@lusik?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/batman-illustratin-uYpOYyJdhRE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- TopGun: Photo by [Peter Pryharski](https://unsplash.com/@meteorphoto?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/blue-and-white-jet-plane-in-mid-air-oapXDz7x_YE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

[Back to top](#top)

<hr>
