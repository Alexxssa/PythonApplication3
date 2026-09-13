import unittest

from auth import authenticate_user

class Test_test_auth(unittest.TestCase):
    def test_missing_credentials(self):
        db = {}
        assert authenticate_user("", "", db) == "Missing credentials"
        assert authenticate_user("", "pass", db) == "Missing credentials"
        assert authenticate_user("user", "", db) == "Missing credentials"

    def test_user_not_found(self):
        db = {}
        assert authenticate_user("user", "pass", db) == "User not found"

    def test_account_locked(self):
        db = {"user": {"password": "pass", "attempts": 3}}
        assert authenticate_user("user", "pass", db) == "Account locked"

    def test_invalid_password(self):
        db = {"user": {"password": "pass", "attempts": 0}}
        assert authenticate_user("user", "wrong", db) == "Invalid password"
        assert db["user"]["attempts"] == 1

    def test_success(self):
        db = {"user": {"password": "pass", "attempts": 1}}
        assert authenticate_user("user", "pass", db) == "Authenticated"
        assert db["user"]["attempts"] == 0
if __name__ == '__main__':
    unittest.main()
