# FitnessApp


YouTube video: https://youtu.be/06Gaq2v74UQ


<p align="center">


  <h3 align="center">FitnessAppMadhu</h3>

  <p align="center">
    Women Fitness App built on Django
    <br />
    <a href="https://github.com/madhumithanara/FitnessApp"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://fitness-app-by-madhu.herokuapp.com/">View Demo</a>
    ·
    <a href="https://github.com/madhumithanara/FitnessApp/issues">Report Bug</a>
    ·
    <a href="https://github.com/madhumithanara/FitnessApp/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


## About The Project

  ![alt text](https://github.com/madhumithanara/FitnessAppDemo/blob/main/homepage.PNG?raw=true)
  
There are many great apps that cater to fitness. But, I believe this app is truly 360.

Here's why:
* The app keeps track of all your fitness parameters, ensuring everything is in one place
* Useful demographics to understand your calories, sleep and heart better
* Pre-loaded workouts to reduce number of clicks. You can pick your type of exercise, complexity and duration!
* Keep track of your menstrual cycle and receive predictions about your future dates

Of course, no fitness app can be truly 360, it depends on the user and the circumstances. I look forward to improving the app to cater to these needs.


### Built With

* [Django](https://www.djangoproject.com/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps.

## Install components
```bash
sudo apt-get update
sudo apt-get install python-pip 
```

### Setting up Virtual Environment and Install Requirements
```bash
sudo pip install virtualenv
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

### Running the website locally
```bash
Update settings.py:
  1. Make DEBUG = True
  2. In DATABASES option , uncomment the commented and comment the uncomment 
cd ~/fitnessWebsite
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



<!-- USAGE EXAMPLES -->
## Usage

### Health Goals

The health goals page allows you to set your ideal weight and hence, your ideal BMI. Your current BMI is also calculated and stored. The displayed values are incentive for the user to input lower/higher values in order to reach their fitness goal.

![alt text](https://github.com/madhumithanara/FitnessAppDemo/blob/main/goals.PNG?raw=true)

### Energy Analysis

Energy Analysis keeps track of user's calorie intake and burnt, sleep hours and average resting heart rate. Plots are made on the same for user to analyze their own lifestyle and improve where needed.

![alt text](https://github.com/madhumithanara/FitnessAppDemo/blob/main/energy.PNG?raw=true)


### Start Workout

Feeling motivated after checking your stats? Pick your choice of exercise, duration and complexity - let's go!

![alt text](https://github.com/madhumithanara/FitnessAppDemo/blob/main/workout.PNG?raw=true)

The video is embedded!
### Health Cycle

I know how hard it is to keep track of our menstrual cycle, this will help! It calculates your cycle duration (see a doctor if it troubling!) and also predicts the next period date so that you can be ready for it!

![alt text](https://github.com/madhumithanara/FitnessAppDemo/blob/main/cycle.PNG?raw=true)

The previous dates are shown at the bottom.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/madhumithanara/FitnessApp/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

Madhumitha Nara - [LinkedIn](https://www.linkedin.com/in/madhumitha-nara/) - naramadhumitha@gmail.com

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* Thanks to Mr. Soorya Annadurai for his ideas and suggestions! 
