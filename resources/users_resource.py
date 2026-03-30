from flask import jsonify

from data import db_session
from flask_restful import abort, Resource
from data.user import User

def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify(user.to_dict(only=(
            "id", "surname", "name", "age", "about", "position", "speciality", "address", "email", "hashed_password",
            "modified_date"
        )))

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'ok'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({
            "users": [
                user.to_dict(only=("id", "surname", "name", "age", "about", "position", "speciality", "address",
                                   "email", "hashed_password", "modified_date")) for user in users
            ]
        })