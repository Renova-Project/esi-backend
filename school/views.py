from rest_framework.response import Response
from rest_framework.views import APIView

class MyView(APIView):
    def get(self, request):
        data = {'message': 'Hello, world!'}
        return Response(data)


