from requests import Response
from fixtures.base import BaseClass
from fixtures.constants import ResponseText
from faker import Faker
import random


fake = Faker()
BC = BaseClass()
userUrl = BC.BASE_URL + '/user'


class UserPage:
    POST_USERINFO = "/user_info/{}"
    PUT_USERINFO = "/user_info/{}"
    GET_USERINFO = "/user_info/{}"
    DELETE_USERINFO = "/user_info/{}"

    def add_user_info(self):
        """Generate random user data"""
        userName = fake.user_name()
        userData = {
            "id": random.randint(1000, 9999),
            "username": userName,
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "email": f"{userName}@petstore.com",
            "password": fake.password(),
            "phone": fake.phone_number(),
            "userStatus": 1
        }
        return userData

    def add_user_api(self, payload):
        """Request api for creating a user"""
        headers = {"Content-Type": "application/json"}
        response = BC.request("POST", userUrl, json=payload, headers=headers)
        return response

    def add_user_from_list(self, payload):
        """Request api for creating a user"""
        headers = {"Content-Type": "application/json"}
        response = BC.request("POST", userUrl + '/createWithList', json=payload, headers=headers)
        return response

    def verify_userLogin(self,username,password):
        """Test login of a user"""
        headers = {"Content-Type": "application/json"}
        payload = {"username": "theUser","password": "12345"}
        response = BC.request("GET", userUrl + '/login', json=payload, headers=headers)
        return response

    def verify_userLogout(self):
        """Tets user logout"""
        response = BC.request("GET", userUrl + '/logout')
        return response

    def get_user(self,username):
        """Get user details by name"""
        headers = {"Content-Type": "application/json"}
        response = BC.request('GET', userUrl + '/' +username, headers= headers)
        return response

    def update_user(self,payload):
        """Update User details"""
        username = payload["username"]
        headers = {"Content-Type": "application/json"}
        response = BC.request("PUT", userUrl + '/' + username, json=payload, headers=headers)
        return response

    def delete_user(self,username):
        """Delete user details"""
        headers = {"Content-Type": "application/json"}
        response = BC.request("DELETE", userUrl + '/' + username, headers=headers)
        return response
