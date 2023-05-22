from django.shortcuts import  render, redirect
from .models import Contact,Personnel,Projet,Temoignage,Service,Contact_Information
from .forms import NewUserForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import FileResponse
from .models import Contact


def index(request):
	contact_info = Contact_Information.objects.first()
	Services=Service.objects.all()
	Personnels = Personnel.objects.all() 
	Projets = Projet.objects.all()
	Temoignages = Temoignage.objects.all()
	context = {'Personnels':Personnels, 'Projets':Projets,'Temoignages': Temoignages,"Services":Services,'contact_info': contact_info}
	return render(request, 'index.html',context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def submit_message(request):
    if request.method == 'POST':
        objet = request.POST.get('objet')
        message = request.POST.get('message')
        user = request.user

        new_message = Contact(username=user, objet=objet, message=message)
        new_message.save()
        
        return redirect('index')  
    else:
        return render(request, 'index.html')

def download_cv(request, personnel_id):
    # get the Personnel object
    personnel = get_object_or_404(Personnel, id=personnel_id)
    if personnel.fichier_CV:
        # open the file using a file object
        cv_file_content = personnel.fichier_CV.read()
        response = FileResponse(cv_file_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{personnel.fichier_CV}"'
        return response
    else:
        return HttpResponseNotFound("The file does not exist.")
	

def project_details(request, id):
    projet = Projet.objects.get(id=id)
    return render(request, 'project_details.html', {'projet': projet})

def my_projects(request):
    user_projects = Projet.objects.filter(user=request.user)
    context = {'user_projects': user_projects}
    return render(request, 'my_projects.html', context)

def home(request):
   
    return render(request, 'home.html')