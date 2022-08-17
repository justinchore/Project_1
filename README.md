# The Little Command Line Book Store on the Corner 
Command line interface bookstore using mySQL and python 3


<!-- ## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact) -->


## General Information
- This project is a command line interface for a fictional book store.
- The goal of this project is to demonstrate handling of mySQL queries, user input handling, admin permissions, and persisting data
- Implemented an MVC (Model-View-Controller) architectural pattern for clear, logical separation of tasks
<!-- - Why did you undertake it? -->
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Python - 3.10.5
- mySQL (Reading/writing functionality with database)
- Regex (User input validations)
- bcrypt (Hashing user passwords for security)
- logging (Tracking application interaction with mySQL)
- PrettyTable/emoji (Formatted output for user experience)


<!-- ## Screenshots
![Example screenshot](./img/screenshot.png) -->
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
<!-- What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project. -->
To run the program, clone or copy project folder onto local machine. Then:

Installing packages:
```
pip install bcrypt
pip install PrettyTable
pip install emoji

```
To execute program:

```
python main.py

```


<!-- ## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here` -->


<!-- ## Project Status
Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why. -->


## Room for Improvement
<!-- Include areas you believe need improvement / could be improved. Also add TODOs for future development. -->

Room for improvement:
- Refactor methods to avoid repeated code
- Optimize controllers by increasing modularity

To do:
- Admin functionality:
    - Permission granting
    - Stats (best sellers, loyal customers, etc)
    - Delete/Add Users
    - Delete/Edit Orders


<!-- ## Acknowledgements
Give credit here.
- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to... -->


## Contact
<!-- Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me! -->
Created by Justin Cho


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->