# Similar-Tweeters
- A Django and ReactJS based web-application utilizing the Twitter API to find accounts with similar tweet styles.
- Modern NLP techniques such as neural language modeling, topic modeling, as well as general deep learning techniques. 

## Setup

### Setup virtual environment.
In order for the program to run, we need to following to be set up properly. 

`pip install -r requirements.txt`


### Build Frontend from source

Build the static files from source. This allows it to loaded from the django backend. 
Use the followings commands:  
`cd text_backend/text_frontend`

`npm install`

`npm build`

### Migrate Database 
This ensures that all of the data is where we want it. If the Django model is tweaked at all, 
this must be done before the results can be implemented. 
Use the following commands: 
`cd text_backend`

`python manage.py migrate --run-syncdb`

### Setup Twitter API

There must exist a `twitter_config.yaml` file on the top level with the bearer token for the application.
This is what allows the Twitter API to function. The YAML files should be of format such that 
the bearer token can be accessed via `data[twitter][bearer_token]`.

Additionally, we want to have the top users pre-loaded into the database. 
We can use the following command:

`python text_backend/preload_users.py`

### Train a Model

#### Clean the Data
In order to train a model, we must have data. If using the example book_data, this can be done via 
`clean_book_data.py` script. Otherwise it must be cleaned and put into `.txt` another way. 






...
