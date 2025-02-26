from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class UserInfoView(APIView):

    def post(self, request):
        serializer = userInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        new_user.save()
        return Response('User created successfully')

    def get(self, request):
        user_data = UserInfo.objects.all()
        get_users_data = userInfoSerializer(user_data, many=True).data
        print(get_users_data)
        return Response(get_users_data)


class UserInfoDetailViewBYID(APIView):

    def get(self, request, id):
        user_data = UserInfo.objects.get(id=id)
        user_details = userInfoSerializer(user_data, many=False).data
        return Response(user_details)

    def patch(self, request, id):
        user_data = UserInfo.objects.get(id=id)
        user_details = userInfoSerializer(user_data, data=request.data, partial=True)

        if user_details.is_valid():
             user_details.save()
             return Response("User updated successfully")
        return Response(user_details.errors, status=400)

    def delete(self, request, id):
        user_details = userInfo.objects.delete(id=id)
        user_details.save()
        return Response('User deleted successfully')
