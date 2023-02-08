from django.shortcuts import render
from rest_framework.views import APIView
from uuid import uuid4
# Create your views here.
# class UploadProfileImage(APIView):
#     def post(self, request):

#         # 일단 파일 불러와
#         file = request.FILES['file']
#         email = request.data.get('email')

#         uuid_name = uuid4().hex
#         save_path = os.path.join(MEDIA_ROOT, uuid_name)

#         with open(save_path, 'wb+') as destination:
#             for chunk in file.chunks():
#                 destination.write(chunk)

#         profile_image = uuid_name

#         user = User.objects.filter(email=email).first()

#         user.profile_image = profile_image
#         user.save()

#         return Response(status=200)