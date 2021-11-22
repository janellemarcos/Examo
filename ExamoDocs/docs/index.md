# Welcome to Examo

## Install

* `sudo apt-get install python` - Python itself
* `pip3 install flask` - Flask
* `pip3 install sqlalchemy` - Sqlite database for python
* `pip install -U Flask-WTF` - WTF Forms
* `pip install Flask-Markdown` - Required for markdown render

## Start
* Open project directory and type `python3 run.py`
* Open `http://127.0.0.1:5000/` in the browser

## Project layout
    Examo/
        ExamoDocs/
	       docs/
                index.md  # The documentation homepage.
           mkdocs.yml
        myapp/
	       templates/ # Contains all the html pages
                 ...           # Html pages           
           app.db         # Database
           __init__.py    # Sets up projects and does imports
           forms.py       # Has wtf forms implementations
           models.py      # Object models that work with database
           routes.py      # Home page controller
           routesNotes.py # Notes controller, create/share/edit notes
           routesUser.py  # User controller, login and registration
        .gitignore
        run.py             # Python file to run the website
        Specifications.md  # Use cases markdown file