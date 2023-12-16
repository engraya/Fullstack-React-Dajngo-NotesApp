from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

# Create your views here.

# API OVERVIEW VIEWS
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Notes List' : '/notesList',
        'Notes Detail' : '/noteDetail/<str:pk>/',
        'Notes Create' : '/noteCreate/',
        'Notes Updtae' : '/notesUpdate/<str:pk>/',
        'Notes Delete' : '/notesDelete/<str:pk>/'
    }
    return Response(api_urls)


#Getting all Notes List
@api_view(['GET'])
def notesList(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    apiResponse = serializer.data
    return Response(apiResponse)
\


#Getting Single Note Detail
@api_view(['GET'])
def noteDetail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    apiResponse = serializer.data
    return Response(apiResponse)


#Create A nEW nOTE
@api_view(['POST'])
def noteCreate(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    apiResponse = serializer.data
    return jResponse(apiResponse)   


#Update a Note
@api_view(['POST'])
def noteUpdate(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    apiResponse = serializer.data
    return Response(apiResponse)    

#Note Delete
@api_view(['DELETE'])
def noteDelete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note Successfully Deleted!')
