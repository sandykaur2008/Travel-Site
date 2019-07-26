# My Travels
This project is called "My Travels" and the aim is to practice using what I've learned so far in my journey to become a developer - HTML (including responsive images with the help of Grunt and GraphicsMagick), CSS (using Sass and Simple Grid), and Python (using Flask). This is a blog with entries on countries I have visited. It is Dockerized and deployed with Amazon Fargate at https://spk.sandytravelstheuniverse.com.
Static resources are served via Amazon S3 buckets. 

# Getting Started

To grab code:
- Navigate to this repo: sandykaur2008/Travel-Site
- Follow these instructions: https://help.github.com/articles/cloning-a-repository/

# Prerequisites
Aside from a working browser and Python 3, you will also need:

- Sass: https://sass-lang.com/install 
- the dependencies in requirements.txt 

## To build css from scss files

To run Sass from the command line, make sure you're in root directory of repo and execute:

```sass app/static/scss/main.scss app/static/css/main.css```

## To install dependencies in requirements.txt

Make sure you're in root directory of repo and execute:

```pip install -r requirements.txt```

## To actually run website once repo cloned, css compiled, and dependencies installed

- Navigate to root directory
- Execute: 

```export FLASK_APP=mytravels.py```

```flask run```

- Navigate to link provided 

# Built With
- Visual Studio Code 1.23.1
- Ruby Sass 3.5.6 
- Flask 1.0.2 (see requirements.txt for extensions used)
- Grunt 0.4.5 

# Authors
Satinder Kaur 

# License
Just a note on images - images that are not originally mine are free for use and modification via Google Images. 

# Acknowledgments
Thanks, @github/markalexandercastillo, for reviewing and giving me tips.

Also, found https://blog.miguelgrinberg.com/ and https://medium.com/@ariklevliber/aws-fargate-from-start-to-finish-for-a-nodejs-app-9a0e5fbf6361 very helpful.
