import numpy as np
from typing import Union
from model import Model
from database import DataBase

def register_user(login: str, image: Union[str, np.array])-> None:
    model = Model()
    bd = DataBase()
    bd.add_new_face(login, model.get_face_embedding(model.detect_face(image)))

def update_user_info(login: str, image: Union[str, np.array]) -> None:
    model = Model()
    bd = DataBase()
    bd.update_face(login, model.get_face_embedding(model.detect_face(image)))

def delete_user_data(login: str) -> None:
    model= Model()
    bd = DataBase()
    bd.delete_user(login)

def detect_user(image: Union[str, np.array]) -> str:
    model = Model()
    bd = DataBase()
    login = model.recognize_from_db(image, bd)
    return login

def compare_users(image1, image2):
    model = Model()

    face1 = model.detect_face(image1)
    face2 = model.detect_face(image2)

    embedding1 = model.get_face_embedding(face1)
    embedding2 = model.get_face_embedding(face2)

    same = model.compare(embedding1, embedding2)
    return same

def database_stats():
    db = DataBase()
    return db.count()

def database_clear():
    db = DataBase()
    db.clear()