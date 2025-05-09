# Kitchen Service
> Kitchen management system for restaurants: dishes, categories, and assigned chefs
This web application is designed to help manage kitchen and restaurant operations efficiently.

  Cook Capabilities:
 - Add new cooks to the system.
 - Create, edit, and delete dishes, dish types and ingredients.

    Search Functionality:
 - Dishes can be searched by name.


## Getting started

A quick introduction of the minimal setup you need to get started.

# After cloning the project create a virtual environment:
python -m venv venv
venv\Scripts\activate # for Windows
source venv/bin/activate # for macOS/Linux

pip install -r requirements.txt 
python manage.py migrate

python manage.py initial_data.json  # to add data to DB
python manage.py runserver

python manage.py createsuperuser  # for creating superuser

```

You can also login with:
username: user
password: user12345

```

```

After executing all commands, you can run the server and the Kitchen Service will work.


## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch.