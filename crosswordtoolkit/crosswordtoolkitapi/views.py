import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from crosswordtoolkitserver.server import CrosswordToolkitServer

# Create the object instance now so that it's only loaded into memory once. It can then be used each time someone visits the page
crossword_toolkit_server = CrosswordToolkitServer()


def index(requestrequest: HttpRequest):
    return HttpResponse("Hello, world. You're at the Crossword Toolkit API index.")


def anagram(request: HttpRequest, letters: str):
    print(f"Request type: {request.method}")
    return HttpResponse(json.dumps(crossword_toolkit_server.get_anagrams(letters)))


def wordfit(request: HttpRequest, letters: str):
    return HttpResponse(json.dumps(crossword_toolkit_server.get_word_fit(letters)))
