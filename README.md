# Charity Donation Web App

A small Django web application that lets users submit donations and view a public leaderboard.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)



## Table of Contents
- [About](#about)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Requirements](#requirements)
- [License](#license)


## About

This is a lightweight Django project built to collect donations and display them on a leaderboard that requires minimal setup.  



## Features

- Submit donations with name, amount, and message  
- Anonymous donations supported  
- Responsive frontend  
- Leaderboard showing latest donations  
- Django admin panel included  


## Screenshots




![Homepage Screenshot](media/frontpage.png)

![Thank you page Screenshot](media/thankyou.png)
![Leaderboard Screenshot](media/leaderboard.png)




## Installation

```bash
git clone https://github.com/fallenexistence0/charity-donation-webapp.git
cd charity-donation-webapp.git
```

```
python -m venv venv
```
On linux and Macos
```bash
source venv/bin/activate
```

On windows 
```
venv\Scripts\activate
```
Then run the following to install the requirements

```bash
pip install -r requirements.txt
python manage.py migrate
```


## Running the App

Make sure your virtual environment is active and then run:

```bash
python manage.py runserver
```

Open your browser and go to the following link:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```




## Requirements

- Python: Make sure you have the latest version of python, and don't forget to install the requirements txt folder.
- Django: Realistically, all you need is python and Django, the requirements.txt file is there in case future updates add new dependencies.



## License

This project is licensed under the MIT License.


## Contact

Feel free to reach out if you want to contribute or have questions.

