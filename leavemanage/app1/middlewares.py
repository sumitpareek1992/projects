from django.shortcuts import render
class RequestTracker:
	def __init__(self, view):
		self.view=view

	def __call__(self, request):
		#print("before sending to view")
		resp = self.view(request)
		if resp.status_code==500:
			return render(request,"app1/500.html")
		elif resp.status_code==404:
			return render(request,"app1/404.html")
		#print("code before response")
		return resp

