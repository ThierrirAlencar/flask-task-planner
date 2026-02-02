from flask_sqlalchemy import SQLAlchemy
from flask import app
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# Modelo Base
BaseModel = declarative_base()
db = SQLAlchemy()