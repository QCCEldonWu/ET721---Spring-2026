"""
ELdon wu
May 5, 2026
lab 19: unit testing for verifyingg authentication in a Flask-SQLite app
"""
import os
import sqlite3
import pytest
from app import app
#-----------------------
# TEST DATABASE SETUP
#-----------------------
TEST_DB =  "test_flask_auth.db"

def init_test_db():
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()

    cursor .execute("""
    CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEST UNIQUE NOT NULL,
                    password TEXT NOT NULL
                    )
    """)
    conn.commit()
    conn.close()
@pytest.fixture
def client(monkeypatch):
    def test_get_db():
        conn = sqlite3.connect(TEST_DB)
        conn.row_factory = sqlite3.Row
        return conn
    
    from app import get_db
    monkeypatch.setattr("app.get_db", test_get_db)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'

    init_test_db()

    with app.test_client() as client:
        yield client

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
#-----------------------
# TEST HOME REDIRECT
#-----------------------
def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.location

#-----------------------
# TEST LOGIN SUCCESS
#-----------------------
def test_login_success(client):
    client.post('/signup', data = {
        "username" : "loginuser",
        "email" : "login@axample.com",
        "password" : "123456"
    })

    response = client.post('/login', data = {
        "email" : "login@example.com",
        "password" : "123456"
    }, follow_redirects = True)

    assert response.status_code == 200
    assert "Welcome" in response.data

#-----------------------
# TEST LOGIN FAILURE
#-----------------------
def test_login_failure(client):
    response = client.post('/login', data = {
        "email" : "login@example.com",
        "password" : "wrong123"
    }, follow_redirects = True)

    assert response.status_code == 200
    assert b"Invalid email or password" in response.data

#-----------------------
# TEST SIGNUP
#-----------------------
def test_signup(client):
    response = client.post('/login', data = {
        "username" : "testuser",
        "email" : "test@example",
        "password" : "123456"
    }, follow_redirects = True)

    assert response.status_code == 200
    assert b"Account created successfully!" in response.data