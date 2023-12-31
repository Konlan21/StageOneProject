from django.shortcuts import render
from django.http import JsonResponse

from datetime import datetime
from django.utils import timezone


def endpoint(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track') 

    current_day = datetime.now().strftime('%A')

    utc_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file = 'https://github.com/Konlan21/StageOneProject/blob/main/stageoneapp/views.py'
    github_repository = 'https://github.com/Konlan21/StageOneProject.git'


    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file,
        'github_repo_url': github_repository,
        'status_code': 200 
    }

    return JsonResponse(response)