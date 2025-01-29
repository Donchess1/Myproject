from django.http import JsonResponse
from datetime import datetime, timezone
def my_Hng_api(request):
    return JsonResponse({
        "email": "stepabod@yahoo.com",
        "current_datetime": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "github_url": "<https://github.com/Donchess1/Myproject>"
    })