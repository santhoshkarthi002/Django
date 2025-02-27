from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class DesignationView(APIView):
    def post(self, request):
        designation_data = designationSerializers(data=request.data)
        if designation_data.is_valid():
            designation_data.save()
            return Response(designation_data.data)
        return Response(designation_data.errors, status=400)

    def get(self, request):
        try:
            get_designation = Designation.objects.all()
            if not get_designation.exists():
                return Response({"error":"No data found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = designationSerializers(get_designation, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error":'Something went wrong',"details" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DesignationDetailViewBYID(APIView):

    def delete(self, request, id):
        designation_data = Designation.objects.get(id=id)
        designation_data.save()
        return Response('Designation deleted successfully')
    
    def get(self, request, id):
        try:
            designation_data = Designation.objects.get(id=id)
            if not designation_data.exists():
                return Response({"error":"No data found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = designationSerializers(designation_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error":'Something went wrong',"details" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

