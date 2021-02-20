from django.shortcuts import render

# urls.pyからもらったrequesetオブジェクト
def signupfunc(request):
	return render(request, 'signup.html', { 'some':100 })