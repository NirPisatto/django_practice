# import base64
# from storage_api.models import File
# from storage_api.serializer import FileSerializer, UploadedFileSerializer
# from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework import status, generics
# from django.http import HttpResponse, JsonResponse
# from django.core.files.base import ContentFile


# # Create your views here.

# @api_view(['GET'])
# def get_all_files(request):
#     files = File.objects.filter(deleted=False)
#     files_serailzer = FileSerializer(files, many=True)
#     return Response(files_serailzer.data)

# @api_view(['GET','PUT', 'DELETE'])
# def handle_file(request, file_id):
#     if request.method == 'GET':
#         return get_file(request, file_id)
#     elif request.method == 'DELETE':
#         return delete_file(request, file_id)
#     elif request.method == 'PUT':
#         return update_file(request, file_id)
#     else:
#         return Response({"message": "Method not allowed"}, status=405)

# # @api_view(['POST'])
# # def upload_file(request):
# #     serailizer = FileSerializer(data=request.data)
# #     serailizer.is_valid(raise_exception=True)
# #     serailizer.save()
# #     return Response(serailizer.data, status=201)

# def get_file(request, file_id):
#     try:
#         file = File.objects.get(id=file_id)
#     except File.DoesNotExist:
#         return Response({"message": "Resource not found"}, status=404)
#     file_serailzer = FileSerializer(file)
#     return Response(file_serailzer.data)

# def delete_file(request, file_id):
#     file = File.objects.get(id=file_id)
#     file.delete()
#     return Response({"message": "Resource deleted successfully"}, status=204)

# def update_file(request, file_id):
#     file = File.objects.get(id=file_id)
#     serailizer = FileSerializer(file, data=request.data)
#     serailizer.is_valid(raise_exception=True)
#     serailizer.save()
#     return Response(serailizer.data, status=201)

# class FileUploadAPIView(generics.CreateAPIView):
#     queryset = File.objects.all()
#     serializer_class = UploadedFileSerializer
#     parser_classes = (MultiPartParser, FormParser, JSONParser)

#     def post(self, request, *args, **kwargs):
#         try:
#             if 'file' in request.data and isinstance(request.data['file'], str):
#                 # If 'file' is a string, assume it's a base64-encoded file and decode it
#                 file_content = base64.b64decode(request.data['file'])
#                 request.data['file'] = ContentFile(file_content, name=request.data['name'])
#         except Exception as e:
#             return Response({"message": "Invalid file"}, status=400)

#         return super().post(request, *args, **kwargs)

#     def perform_create(self, serializer):
#         serializer.save()

import base64
from storage_api.models import File
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from storage_api.serializer import  UploadedFileSerializer
from storage_api.models import File
from django.http import HttpResponse, JsonResponse
from django.core.files.base import ContentFile


class FileList(APIView):
    def get(self, request):
        try:
            files = File.objects.filter(deleted=False)
        except Exception as e:
            return Response({"message": "Resource not found"}, status=404)
        file_serailzer = UploadedFileSerializer(files, many=True)
        return Response(file_serailzer.data)
    

class FileCreate(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = UploadedFileSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, *args, **kwargs):
        try:
            if 'file' in request.data and isinstance(request.data['file'], str):
                # If 'file' is a string, assume it's a base64-encoded file and decode it
                file_content = base64.b64decode(request.data['file'])
                request.data['file'] = ContentFile(file_content, name=request.data['name'])
        except Exception as e:
            return Response({"message": "Invalid file"}, status=400)

        return super().post(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save()

class File(APIView):
    def get(self, request, file_id):
        try:
            file = File.objects.get(id=file_id)
        except Exception as e:
            return Response({"message": "Resource not found"}, status=404)
        file_serailzer = UploadedFileSerializer(file)
        return Response(file_serailzer.data)
    
    def delete(self, request, file_id):
        try:
            file = File.objects.get(id=file_id)
        except Exception as e:
            return Response({"message": "Resource not found"}, status=404)
        file.delete()
        return Response({"message": "Resource deleted successfully"}, status=204)

    # def delete(self, request, file_id):
    #     file = File.objects.get(id=file_id)
    #     file.delete()
    #     return Response({"message": "Resource deleted successfully"}, status=204)

    # def put(self, request, file_id):
    #     file = File.objects.get(id=file_id)
    #     serailizer = UploadedFileSerializer(file, data=request.data)
    #     serailizer.is_valid(raise_exception=True)
    #     serailizer.save()
    #     return Response(serailizer.data, status=201