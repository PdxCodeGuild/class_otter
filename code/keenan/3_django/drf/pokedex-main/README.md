# Pokedex Starter

## Installation

Make sure you have Python and Pipenv installed on your computer.

Download the repo and save it to your code folder in the class repo. *make sure you download it, don't clone it or it won't upload to the class repo correctly*

If you are not running Python 3.8, edit the last line of the `Pipfile` to refer to your version instead.

Navigate to the pokedex folder in the terminal and do the following:

- `pipenv install` Create the virtual enviroment and install dependencies.
- `pipenv shell` Enter the new virtual enviroment.
- `python manage.py migrate users` Migrate the user model. *this django project uses a custom user model, you MUST migrate the users app before migrating the rest!*
- `python manage.py migrate` Migrate all other models.
- `python manage.py createsuperuser` Create yourself a super user.
- `python manage.py load_pokemon` Load Pokemon into the database.

You're good to go! This Django project comes with a database full of Pokemon, login/logout/registration pages, and a `home.html` template for you to create your Vue app.


<!-- Part 2 - Basic API
Create an API for the Pokedex in Django Rest Framework. Your API needs to have endpoints for all the Pokemon, as well as some sort of nested serializers so that your API returns the names of the types that each Pokemon belongs to, not just the pk of those types.

Use the WSVincent DRF tutorial and the in-class examples as references.

Part 3 - Vue Frontend
Build a Vue frontend for our Pokedex! I already provided you with a home.html template you can use. Make sure to leave the links to the login/logout/signup pages so that a user can get themselves authenticated (otherwise the API won't work!).

Your frontend should display a list of Pokemon upon loading.

DRF and Vue
Axios

Part 4 - More Features
You must implement ONE of the following features into your app. You can implement more if you'd like.

Edit Pokedex
Add the ability to create new Pokemon, update the stats of existing Pokemon, and delete Pokemon. Make sure that only registered users can edit your list of Pokemon. You are not required to implement the ability to add types to newly created Pokemon, but it's good practice.

User Lists
Add a list to your Pokedex of all Pokemon that a logged in user has caught. Add the ability to mark a pokemon as caught or remove a marked pokemon from the caught list.

The models are already set up to do this. Pokemon has a many-to-many relationship with CustomUser. You will also need API endpoints for the users. To add a Pokemon to a user's list, add the pk of that Pokemon to the caught array and send a PUT/PATCH request with the new array of caught Pokemon. To remove a Pokemon from a user's list, remove the pk of that Pokemon from the caught array and send a PUT/PATCH request with the new array of caught Pokemon. -->


