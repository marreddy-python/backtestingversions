from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DEBUG = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/flask?user=marreddy&password=BECKNF79"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://mndmusdexwungz:cb4ca1d3f83f4bde9bd9cd8f04af8acb50bddf8583709b63915c739c3bb6c1ef@ec2-174-129-210-249.compute-1.amazonaws.com:5432/d3ebr0n5d6q2mk"

db = SQLAlchemy(app)