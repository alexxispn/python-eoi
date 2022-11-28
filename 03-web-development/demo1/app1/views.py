from django.shortcuts import render
from django.http import HttpResponse


def hello(req, name = ''):
    return HttpResponse(f"""
    <html>
        <head>
        <title>Hello World</title>
        </head>
        <body>
            <h1> Hello <b>{name}</b></h1>
        </body>
    </html>
    """)


