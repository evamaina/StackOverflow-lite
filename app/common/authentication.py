from functools import wraps
from flask import request, jsonify
from app.models.users import User
def jwt_required(f):
   
    @wraps(f)
    def decorator(*args, **kwargs):
        '''fetches token from header and decodes it'''
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return jsonify({'message':'provide token please'})
        auth_token = auth_header.split("Bearer ")[1]
        if auth_token:
            user_id = User.decodetoken(auth_token)
            if not isinstance(user_id, str):
                user_id = user_id
            else:
                response = {
                    'message' : user_id
                }
                return jsonify(response), 401
        else:
            return False
        return f(user_id)
    return decorator