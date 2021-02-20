from django.shortcuts import render

# urls.pyからもらったrequesetオブジェクト
def signupfunc(request):
	if request.method == "POST":
		print("ぽすおだよー")	
	else:
		print("ちがうねー")
	return render(request, 'signup.html', { 'some':100 })