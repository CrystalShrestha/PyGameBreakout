from pymongo import MongoClient
from pymongo import DESCENDING
from datetime import datetime


def connect_db():
    uri = "mongodb+srv://crystal:Winning11@cluster0.usgz7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    my_db_cli = MongoClient(uri)
    db = my_db_cli.joran1
    my_scores = db.scores  # creating a score table
    allscores = (list(my_scores.find().sort("score", DESCENDING)))
    return allscores


def fetch_scores():

    my_scores = connect_db()
    # get a list of high scores (from best to worst)
    return my_scores


def write_score(name, score):
    #my_scores = connect_db()
    uri = "mongodb+srv://crystal:Winning11@cluster0.usgz7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    my_db_cli = MongoClient(uri)
    db = my_db_cli.joran1
    my_scores = db.scores
    now = datetime.now().strftime("%d/%m/%Y")

    # add a new score
    my_scores.insert({"user_name": name,
                      "score": score, "time": now})
    # get a list of high scores (from best to worst)
    allscores = (list(my_scores.find().sort("score", DESCENDING)))
    return allscores


def fetch_high_score():
    my_scores = connect_db()
    max_score = max(my_scores, key=lambda x: x['score'])
    return max_score


def fetch_low_score():
    my_scores = connect_db()
    min_score = min(my_scores, key=lambda x: x['score'])
    return min_score

    # If you need to add a user manually to the DB
    # my_scores.insert({"user_name": "Raj Kumar",
    #                   "score": "77", "time": "08/22/2021"})
    # my_scores.insert({"user_name": "Shyam", "score": "33",
    #                   "time": "02/23/2021"})
