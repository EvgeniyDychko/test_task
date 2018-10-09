from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin
from rest_framework.views import APIView
from .models import Notice
from .serializer import NoticeSerializer
from rest_framework.response import Response
from .form import NoticeForm
# Create your views here.

class NoticeList(APIView):

    def get(self,request):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)
    

class NoticeOrderView(FormMixin, ListView):
    context_object_name = 'notices'
    ordering = ['-numbers']
    template_name = 'index.html'
    success_url = '/'
    form_class = NoticeForm
    model = Notice

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

