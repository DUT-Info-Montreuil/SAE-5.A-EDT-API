from flask import Flask, jsonify
from flask import Blueprint

from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from contextlib import closing
from config import config

# from services.absent_service import absent_service

absent_app = Blueprint('absent_app', __name__)
