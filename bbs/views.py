from django.shortcuts import render, redirect

from django.views import View
from .models import Topic

class BbsView(View):

    def get(self, request, *args, **kwargs):

        data    = Topic.objects.all()
        context = { "data":data }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        posted  = Topic( comment = request.POST["comment"] )
        posted.save()

        return redirect('index')

index   = BbsView.as_view()