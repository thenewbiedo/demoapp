import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import yaml
from flask import Flask

def init_connect_engine():
    # Check if the environment is not 'standard'
    if os.environ.get('GAE_ENV') != 'standard':
        with open("app.yaml", 'r') as file:
            config = yaml.load(file, Loader=yaml.SafeLoader)  # Safely load the YAML file
        env_variables = config.get('env_variables', {})
        
        # Set environment variables
        for var, value in env_variables.items():
            os.environ[var] = value

    # Create the SQLAlchemy engine
    engine = create_engine(
        URL.create(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            host=os.environ.get('MYSQL_HOST'),
            port=3306,  # Default MySQL port
            database=os.environ.get('MYSQL_DB')
        )
    )
    return engine

app = Flask(__name__)
db = init_connect_engine()

from app import routes  # Import routes after initializing the app and database
