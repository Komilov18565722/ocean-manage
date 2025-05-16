from django.http import JsonResponse

from accounts.models import User

class StateCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        auth = request.headers.get('Authorization', None)
        
        # if request.META['REMOTE_ADDR'] == '192.168.23.165':
        #     return JsonResponse({"Ukam": "Uzur so`ra"}, status=502)
        
        if auth:

            token = auth.split()

            if len(token) > 1:
                token = token[1]

                import jwt
                from environs import Env
                env = Env()
                env.read_env()
                secret_key = env.str("SECRET_KEY")

                try:
                    decoded_data = jwt.decode(token, secret_key, algorithms=["HS256"])
                    user = User.objects.filter(id = decoded_data['user_id']).first()
                    if user and user.status == 0:
                        return JsonResponse({"error": "Unauthorized"}, status=401)

                except jwt.InvalidTokenError:
                    print("Invalid Token")


        response = self.get_response(request)
        
        return response

    