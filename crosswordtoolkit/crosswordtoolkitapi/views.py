import json
from django.shortcuts import render
from django.http import HttpResponse
from crosswordtoolkitserver.server import CrosswordToolkitServer

# Create the object instance now so that it's only loaded into memory once. It can then be used each time someone visits the page
crossword_toolkit_server = CrosswordToolkitServer()


def index(request):
    return HttpResponse("Hello, world. You're at the Crossword Toolkit API index.")


def anagram(request, letters):
    return HttpResponse(json.dumps(crossword_toolkit_server.get_anagrams(letters)))


def wordfit(request, letters):
    return HttpResponse(json.dumps(crossword_toolkit_server.get_word_fit(letters)))
