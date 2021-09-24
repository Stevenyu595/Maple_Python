"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from maple import views

app_name = 'maple'
urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu_list, name="menu_list"),
    path('side_menu/<int:side_id>', views.side_detail, name="side_detail"),
    path('chicken_menu/<int:chicken_id>', views.chicken_detail, name="chicken_detail"),
    path('beef_menu/<int:beef_id>', views.beef_detail, name="beef_detail"),
    path('detail_menu/<int:menu_id>', views.menu_detail, name="menu_detail"),
    path('application/', views.accept, name="accept"),
    path('add', views.create_item, name="create_item"),
    path('add_side', views.create_side, name="create_side"),
    path('add_chicken', views.create_chicken, name="create_chicken"),
    path('add_beef', views.create_beef, name='create_beef'),
    path('update/<int:id>', views.update_item, name="update_item"),
    path('side_update/<int:id>', views.update_side, name='update_side'),
    path('chicken_update/<int:id>', views.update_chicken, name='update_chicken'),
    path('beef_update/<int:id>', views.update_beef, name='update_beef'),
    path('delete/<int:id>', views.delete_item, name="delete_item"),
]