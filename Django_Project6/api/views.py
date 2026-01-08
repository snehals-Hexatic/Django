from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .models import Student
from .serializers import StudentSerializer


@csrf_exempt
def student_api(request):

    # ---------- GET ----------
    if request.method == 'GET':
        id = request.GET.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return HttpResponse(
                JSONRenderer().render(serializer.data),
                content_type='application/json'
            )

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return HttpResponse(
            JSONRenderer().render(serializer.data),
            content_type='application/json'
        )

    # ---------- POST ----------
    if request.method == 'POST':
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(
                JSONRenderer().render({'msg': 'Data Created'}),
                content_type='application/json'
            )

        return HttpResponse(
            JSONRenderer().render(serializer.errors),
            content_type='application/json'
        )

    # ---------- PUT ----------
    if request.method == 'PUT':
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        id = data.get('id')
        stu = Student.objects.get(id=id)

        serializer = StudentSerializer(stu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(
                JSONRenderer().render({'msg': 'Data Updated'}),
                content_type='application/json'
            )

        return HttpResponse(
            JSONRenderer().render(serializer.errors),
            content_type='application/json'
        )
     
     #-----------Delete-----------------   

    if request.method == 'DELETE':
     id = request.GET.get('id')

    if id is None:
        return JsonResponse({'error': 'ID is required'}, status=400)

    stu = Student.objects.get(id=id)
    stu.delete()

    return JsonResponse({'msg': 'Data Deleted'})

       
       

