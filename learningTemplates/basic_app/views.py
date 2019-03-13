from django.shortcuts import render

# Create your views here.

def index(request):
	context_dict = {'text':'hello world','number':100}
	return render(request,"basic_app/index.html", context=context_dict)
def other(Request):
	return render(Request, "basic_app/other.html")
def relative(Request):
	return render(Request, "basic_app/relative_templates.html")
