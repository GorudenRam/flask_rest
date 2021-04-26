from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from .users import User
from . import db_session


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('password', required=True)


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        return jsonify(
            {
                'user': user.to_dict(only=('id', 'surname', 'name', 'age',
                                           'position', 'speciality', 'address', 'email', 'hashed_password'))
            }
        )

    def put(self, user_id):
        abort_if_user_not_found(user_id)
        args = parser.parse_args()
        session = db_session.create_session()
        user = session.query(User).filter(User.id == user_id).first()
        user.id = args['id']
        user.surname = args['surname']
        user.name = args['name']
        user.age = args['age']
        user.speciality = args['speciality']
        user.address = args['address']
        user.email = args['email']
        user.position = args['position']
        user.set_password(args['password'])
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality',
                  'address', 'email', 'hashed_password')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            id=args['id'],
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            position=args['position']
        )
        user.set_password(args['password'])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})