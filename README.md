# CrystalBall

Welcome to CrystalBall, a project by Nael Al-Assaad, Matthew Frechette, and Enrique Esteve!

## Overview

### Introduction

Our application will allow anyone to see our predictions for any Major League Baseball games. We have created an algorithm, a database, and a website to help reach our goal of predicting scores. Users will have access to our website to see current day predictions. 

### Purpose 

Our purpose is to help sports analyst and teams to see the best possible prediction of that MLB game. By having our predictions at their finger tips, sports analysts can get more insight on how the game will turn out. Teams will also benefit from our machine by seeing who their worst match-ups are and their precentage of winning. Teams can change line-ups to increase their chance of winning by looking at the original prediction.

### Functionality 

This application will take our algorithm, which follows a linear regression model, and take the current day games and post predictions of that game. We have a database in the back that helped train the model to get accurate scores. We've created a webscrapping tool to get stats from ESPN.com and be pushed into our database. This will keep our predictions fresh, up to date, and more accurate. 

## Installation

_Below is how to install and run our project on your machine locally._

1. Clone the repo or download the files locally to your machine, keeping the file scructure exactly!!!
2. Install back-end packages
   ```sh
   pip install -r requirements.txt
   ```
3. Clone the database to your local host using the attached SQL file.
4. Run the linreg.py script to ensure the .pkl files are working.
5. Run the backend.py script to update the database and generate predictions for the day.
6. Run the app.py script and then go to http://127.0.0.1:5000 to access the website.

## Usage

View the video below to see a quick demo. 

[![Crystal Ball](https://i9.ytimg.com/vi_webp/A5NYVScRJEw/mq2.webp?sqp=CPDWubUG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGDQgTSh_MA8=&rs=AOn4CLCUKfUNnEJJziKn9tpCg2KfD1GN_w)](https://youtu.be/A5NYVScRJEw)


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contacts

Nael Al-Assaad - alassaadn@wit.edu <br />
Enrique Esteve - estevee@wit.edu <br />
Matthew Frechette - frechettem1@wit.edu
