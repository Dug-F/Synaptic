<a name="top"></a>
# Synaptic Multi-player Quiz Project

## Contents
1. [Problem](#problem)
2. [Solution](#solution)
3. [Demo And How To Use The App](#usage)
4. [What I Learned](#lessons)
5. [Tech Stack](#techStack)
6. [How To Install And Run Locally - Easier Version Using Docker](#installEasier)
7. [How To Install And Run Locally - Harder Version Minimally Using Docker](#installHarder)
8. [Attributions](#attributions)

<a name="#problem"></a>
# 1. Problem

I have a group of friends who meet up online every so often and one of the things we like to do is have a friendly and fun quiz.  We take it in turns to create and run the quiz.  At first we used Kahoot, but found it had some features which were somewhat limiting:
- if you leave the quiz for a while, it times out.  You cannot rejoin the quiz and retain your previous progress: you are joined as effectively a new user.
- it is the same if you get disconnected, e.g. you temporarily lose your wifi connection.  You cannot rejoin and retain your previous progress
- if the quiz host made a mistake when compiling the quiz and accidentally (or deliverately!) marked the wrong answer as correct, there is no way of correcting it
- once you enter your answer you cannot change it, even if other players are still considering their answer
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

As per the brief, the solution was implemented using Django, Django Channels and JavaScript.  

The application operates in 2 parts, which are connected via the database:
- creating and amending quizzes, which is done in usual Django syncronous fashion using views and forms, etc.
- playing the quizzes, which is done asynchronously using websockets, Django Channels and consumers.

For the asyncronous components, Django Channels was used as a layer on top of websockets to enable persistent two-way connection between the players and the server.  This keeps all the players in sync so that as nearly as possible, all players are seeing the same thing at the same time.  Django Channels uses async asgi communication and therefore I have incorporated the Daphne server within Django to handle the async calls.  Daphne is incorporated into and starts and ASGI/Daphne version of the development server when the runserver command is executed.

The server sends the countdown timer through the websockets to the client browsers and when the next question is due the formatted question is sent over the websocket to the client.  As well as keeping everything in sync, this is to prevent users requesting questions/answers directly themselves from the browser and so getting an unfair advantage.

A large part of the solution was written before I understood as much about SOLID principles as I do now.  As I look at the code now, there are many things I would like to change to better incorporate SOLID principles.  However, that is a significant undertaking and I will address it slowly over time.  

The code is far from perfect, but it has proven to be pretty robust - it has been used very many times in my circle of friends for quite some time.  There have been a few hiccups, but all have been resolved quickly.  In live operation, the app is hosted on a friends Raspberry Pi, running Ubuntu.

[Back to top](#top)

<hr>

<a name="usage"></a>
# 3. Demo and How To Use The App

Here are a couple of videos that demonstrate the Synaptic app and show you how to use it.

<h3>Demo/how to video for creating and updating a quiz</h3>

<a href="https://youtu.be/xkSxxRp5_-o" title="Watch the video">
    <img src="/synaptic/static/synaptic/SynapticCreateQuiz.png" alt="Watch the video" width="500"/>
</a>

<h3>Demo/how to video for how to play a quiz</h3>

<a href="https://youtu.be/239R66ovHYw" title="Watch the video">
    <img src="/synaptic/static/synaptic/SynapticPlayQuiz.png" alt="Watch the video" width="500"/>
</a>

<br>

<br>

[Back to top](#top)

<hr>

<a name="lessons"></a>
# 4. What I Learned

This is probably the project that taught me most out of any of the recent projects I have undertaken.  It was my first project in Django and is the project which really kick-started my journey into the world of web development.

Before I started the project I was reasonably experienced in Python (which I why I decided to go with Django) but knew nothing about Django, web protocols, animations, websockets, Django Channels, Redis and very little about JavaScript - I had to learn all of it as I went along.

Through undertaking the project, I have learned huge amounts about all of the above topics and I used it as a launching pad to embark on a much deeper exploration of web development which ultimately took me to the School of Code.

[Back to top](#top)

<hr>

<a name="techStack"></a>
# 5. Tech Stack

Python, Django, Django Channels, Redis, JavaScript, GSAP (for animations), Ajax, Bootstrap, FontAwesome

[Back to top](#top)

<hr>

<a name="installEasier"></a>
# 6. How To Install And Run Locally - Easier Version Using Docker

## 6.1 If Docker Desktop is not already installed on your machine, install it
- install Docker Desktop by following the instructions [here](https://www.docker.com/products/docker-desktop/)
	- you wil probably need to re-start your machine to complete the installation

## 6.2 Clone the Github repo to the synaptic folder
- navigate to the folder where you want to install Synaptic
- from the synaptic folder: `git clone https://github.com/Dug-F/Synaptic.git`
	- this will create a new directory called `Synaptic` in your current folder
- change directory into the Synaptic folder: `cd Synaptic`

## 6.3 Create a .env file
- the .env file contains secret details which are not published to Github
- you need to create your own version of .env
- create an empty .env file in /Synaptic (i.e. the same folder as manage.py)
- the key entries are shown in the `env_keys.txt` file
	- copy these keys into the .env file
- the keys then need to have values set for them:

>[!important] 
**the values for the keys must not have any surrounding quotes, otherwise they will not work correctly**
	
- for the SECRET_KEY, a new key can be generated using: 
	- `docker build -t keygen \keygen`
	- and then `docker run --rm keygen`
	- this prints a new secret key and key value in the terminal window
	- copy and paste the whole secret key line into the .env file (replace any secret key already there)

- for the `EMAIL_USER=` and `EMAIL_PASS=` keys, these must be a valid email user and password
	- these are only used for sending password reset emails
	- for demo purposes, if you can live without resetting passwords, you can leave the values here empty
	- if you use a gmail address, you will probably need to enable ["less secure apps"](https://knowledge.workspace.google.com/kb/how-to-enable-less-secure-application-access-000006971)
	- it is recommended to set up a new dedicated email for this purpose

## 6.4 Start the docker services
- make sure you are in the Synaptic directory, i.e. the one that contains manage.py
- enter the following command: `docker compose up`
- you can stop the docker services with `docker compose down`
- note that the docker services are currently configured such that the database is deleted and rebuilt whenever the services are brought down and back up
	- I will probably change that on a future update to create a database that persists across restarts.

<a name="installHarder"></a>
# 7. How To Install And Run Locally - Harder Version Minimally Using Docker

>[!Note]
>The instructions below are for installation on a Windows machine.
>On other operating systems there may be slight variations, most notably with creating and/or activating the virtual environment.  Please use the equivalent operations for your OS.

## 7.1 Install Python
- make sure you have Python 3.10+ installed on your machine.  
- this app has not been tested with Python 3.10, only with 3.11.3
- the version of python installed and active determines the version that is used to build the virtual environment in the next step
	- so make sure that the version of Python you intend to use is active using `python --version`
- instructions for installing Python are [here](https://www.python.org/about/gettingstarted/)

## 7.2 Create virtual environment
- create new folder for project: synaptic
- `cd synaptic
- create virtual environment: `python -m venv venv`
- activate the virtual environment: `venv\Scripts\activate`

## 7.3 Clone the Github repo to the synaptic folder
- from the synaptic folder: `git clone https://github.com/Dug-F/Synaptic.git`
- change directory into the Synaptic folder: `cd Synaptic`

## 7.4 Install Python dependencies
- install the required python modules: `pip install -r requirements.txt`

## 7.5 Create a .env file
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

## 7.6 Build and initialise the database
- make the database migrations: `python manage.py makemigrations`
- apply the migrations: `python manage.py migrate`
- install the required database reference data: `python manage.py seed_data`

>[!important]
>Only run `seed_data` once to avoid the possibility of duplicate entries in the database

## 7.7 Install and run Redis

- Django Channels requires Redis to manage websocket communicationbetween multiple clients
- Redis does not natively run on all platforms
- probably the easiest way to install and run Redis is by using Docker
- install Docker Desktop by following the instructions [here](https://www.docker.com/products/docker-desktop/)
	- you wil probably need to re-start your machine to complete the installation
 - once Docker is installed, you can install and run a Redis in a container with `docker run --rm -p 6379:6379 redis:7-alpine`

## 7.8 Start the database
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
- register new users(s) and log in.

[Back to top](#top)

<hr>

<a name="attributions"></a>
## 8. Attributions

Attributions for the images used in the demo quiz:

- Batman: Photo by [Marcin Lukasik](https://unsplash.com/@lusik?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/batman-illustratin-uYpOYyJdhRE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- TopGun: Photo by [Peter Pryharski](https://unsplash.com/@meteorphoto?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/blue-and-white-jet-plane-in-mid-air-oapXDz7x_YE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

[Back to top](#top)

<hr>
