from django.conf.urls import url
from myDBApp import views

app_name = 'myDBApp'

urlpatterns = [
    url(r'^$', views.CollegeList.as_view(), name = 'list'),
    url(r'^register_college/', views.CreateCollege.as_view(), name = 'create_college'),
    url(r'^register_student/', views.CreateStudent.as_view(), name = 'create_student'),
    url(r'^(?P<pk>[-\w]+)/$', views.CollegeDetail.as_view(), name = 'college_details'),
    url(r'^update/(?P<pk>[-\w]+)/$', views.UpdateStudent.as_view(), name = 'update_student'),
    url(r'^delete/(?P<pk>[-\w]+)/$', views.DeleteStudent.as_view(), name = 'delete_student'),

]
