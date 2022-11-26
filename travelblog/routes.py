import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from travelblog import app, db, bcrypt, mail
from travelblog.forms import (RegistrationForm, LoginForm, UpdateAccountForm, 
    PostForm, RequestResetForm, ResetPasswordForm)
from travelblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

# home webpage
