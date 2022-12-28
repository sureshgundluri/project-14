from django.urls import path
from app1.views import *
app_name='something1'

urlpatterns=[
    path('suresh/',suresh,name='suresh'),
    path('naresh/',naresh,name="naresh"),
]