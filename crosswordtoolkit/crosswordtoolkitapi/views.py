import json
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Crossword Toolkit API index.")


def anagram(request, letters):
    return HttpResponse(
        f"Iya. You're now at the Crossword Toolkit Anagram API page, for input letters: {letters}!"
    )


def wordfit(request, letters):
    """Placeholder function to find the words, with some test json output"""
    words = []
    for l in letters:
        words.append(l)
    return HttpResponse(f"{json.dumps(words)}")
