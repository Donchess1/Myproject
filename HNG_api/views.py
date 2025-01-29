from django.shortcuts import render
from datetime import datetime, timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(["GET"])
def my_Hng_api(request):
    return Response({
        "slack_email": "stepabod@yahoo.com",
        "current_datetime": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "github_url": "https://github.com/Donchess1/Myproject.git"
    }, status=status.HTTP_200_OK)