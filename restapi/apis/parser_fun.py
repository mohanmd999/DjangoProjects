def user_parser(request):
	data={}
	data['username']=request.POST.get('username')
	data['password']=request.POST.get('password')
	data['email']=request.POST.get("email")
	data['phone']=request.POST.get("cell")

	return data

def post_parser(request):
	data={}
	data['post_title']=request.POST.get('post_title')
	data['post_description']=request.POST.get('post_description')
	return data

def create_user_parser(request):
	data={'profile':{
	"city": " ",
	"country": " "
	}}
	data['username']=request.POST.get('username')
	data['password']=request.POST.get('password')
	data['email']=request.POST.get('email')
	# data['username']=request.POST.get('username')

	data['profile']['city']=request.POST.get('city')
	data['profile']['country']=request.POST.get('country')
	return data