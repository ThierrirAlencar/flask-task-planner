from flask_sqlalchemy import SQLAlchemy
from flask import app
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()