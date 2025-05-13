from models import UserModel, db
from flask_restful import Resource, fields, reqparse, request, marshal

user_fields = {
    "id": fields.Integer,
    "firstName": fields.String,
    "lastName": fields.String,
    "userName": fields.String,
    "email": fields.String,
    "phoneNumber": fields.Integer,
    "password": fields.String,
    "verified": fields.Boolean
}

class User(Resource):
    user_parser = reqparse.RequestParser()
    user_parser.add_argument('firstName', required=True, help="Enter your first name!")
    user_parser.add_argument('lastName', required=True, help="Enter your last name!")
    user_parser.add_argument('userName', required=True, help="Enter your username!")
    user_parser.add_argument('email', required=True, help="Enter your email address!")
    user_parser.add_argument('phoneNumber', required=True, help="Enter your phone number!")
    user_parser.add_argument('password', required=True, help="Enter your password!")

    def get(self, id=None):
        if id:
            user = UserModel.query.filter_by(id=id).first()
            if user:
                return marshal(user, user_fields), 200
            else:
                return {"message": "User not found"}, 404
        else:
            users = UserModel.query.all()
            return [marshal(user, user_fields) for user in users], 200

    
    def post(self):
        data = request.get_json()
        user = UserModel(**data)

        try:
            db.session.add(user)
            db.session.commit()

            return {"message": "User created successfully", "status": "success"}
        except Exception as e:
            return {"message": "Unable to create user", "status": "fail"}, 400
    
    