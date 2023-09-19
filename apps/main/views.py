from django.shortcuts import render
from django.views.generic import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from .models import Matches, Favourite, User


class MainView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'index.html'
        videos: QuerySet[Matches] = Matches.objects.all()
        userr = User.objects.first()
        f_videos: QuerySet[Favourite] = Favourite.objects.filter(user=userr)
        return render(
            request=request,
            template_name=template_name,
            context={
                'videos': videos,
                'f_videos': f_videos
            }
        )