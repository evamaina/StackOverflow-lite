def jwt_required(func):
   
    @wraps(f)
    def decorator(*args, **kwargs):
        '''fetches token from header and decodes it'''
        auth_header = request.headers.get('Authorization')
        auth_token = auth_header.split("Bearer ")[1]
        if auth_token:
            user_id = User.decode_token(auth_token)
            if not isinstance(user_id, str):
                user_id = user_id
            else:
                response = {
                    'message' : user_id
                }
                return jsonify(response), 401
        else:
            return False
        return func(user_id=user_id, *args, **kwargs)
    return decorator