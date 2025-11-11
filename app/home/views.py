from django.http import HttpResponse
import os
import socket

def index(request):
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "Unable to determin IP address"
    imp = os.environ.get("IMP_Text","Not Set Yet")
    return HttpResponse(f"<h1> Hello IT Security Nepal <h1> new line check blah blah <br> Hostname: {hostname} <br> IP Address: {ip_address} <br> <br> Important text is {imp}")
