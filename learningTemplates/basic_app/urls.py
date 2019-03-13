from django.urls import path
from basic_app import views

# template tagging
app_name = 'basic_app'

urlpatterns = [
	path('index/',views.index,name='index'),
	path('relative/',views.relative,name='relative'),
	path('other/',views.other, name='other'),
]