# Basic Development Notes

I highly doubt someone is going to add upon this, but it's likely since Wagtail is new, someone will look at this for referencing purposes

I created a dummy layout and design in order to revamp  [my personal website here
](http://https://github.com/Munnu/PersonalWebsite)

Now I'm learning Django and Wagtail concurrently to build the web application version of the website. This is currently WIP as I'm chugging along and duking it out.

# Virtual Environments

In order to run this, you will need to create a virtual environment.

1. If you haven't done so, [look up how to install a virtual environment-making capabilities onto your machine here](https://virtualenv.pypa.io/en/stable/installation/).

2. Afterwards, you will need to take whatever requirements.txt info I have, and install those to your virtual environment.

    1. Activate your virtual environment by doing:

        `source env/bin/activate`, I'm assuming your virtual environment is called **env**.

    2. `pip install -r requirements.txt` does the trick
    
Then there's the usual `python manage.py runserver` and whatever else you've learned from Django and the Wagtail documentation.

Ex: creating a superuser to access the administration panel, or you may have to override the username and password for development purposes, I'm sure there's something on stackoverflow for that. Since I'm not aware on what is needed as I have not cloned my own project, I'm not sure.