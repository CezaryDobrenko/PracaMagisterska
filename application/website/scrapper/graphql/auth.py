from scrapper.models.api_key import ApiKey

from functools import wraps

def get_user_from_api_token(api_token):
    key = ApiKey.objects.filter(key=api_token).first()
    if key:
        if key.is_active:
            return key.user
        else:
            raise Exception("Api key is inactive!")
    else:
        raise Exception("Invalid api key!")
    

def authenticate_required():
    def decorator(func):
        @wraps(func)
        def wrapper(root, info, *args, **kwargs):
            authorization = info.context.environ["HTTP_AUTHORIZATION"]
            api_token = "".join(authorization.split())[6:]
            kwargs["api_token"] = api_token
            kwargs["current_user"] = get_user_from_api_token(api_token)
            return func(root, info, *args, **kwargs)

        return wrapper

    return decorator