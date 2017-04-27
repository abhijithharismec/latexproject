from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^processimg',views.preprocess,name='preprocess'),
	#url(r'^tesscall',views.call,name='call'),
	#url(r'^gencode',views.codegen,name='codegen'),
]