"""
URL configuration for chaiordjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
#    yha pe path="" ye choda hai kyuki ye chai app k andar ka hai but pura url jo web pe dikhega loca host:8000/chai/ kyuki chai/ hmne main wle me diye tha project folder me
    path('',views.all_chai,name='all_chai'),
    # 2nd path me jo <int:chai_id> ye id mngta hai or sql me id integer me hota hai to aesa likhna hota hai then / kya webpage dikhaan hai is path pe or chai_id hi likhna hai kyuki views.py pe chai_id hi pass kiye the parameter me
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    # path('chai_stores/', views.chai_store_view, name='chai_stores'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
    
    
]
