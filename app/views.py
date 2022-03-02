from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse, response,Http404, HttpResponseRedirect

from .models import Question,Member
from .forms import MemberForm
from django.utils import timezone

# Create your views here.
#def index(request):
   # return render(request, 'app/index.html')

#liste
def index(request):
    members = Member.objects.all().order_by('id') #Obtenez de la valeur
    return render(request, 'app/members/index.html', {'members':members})
    
#Nouveau et modifier
def edit(request, id=None):
	if id: #Lorsqu'il y a un identifiant (lors de l'édition)
		#Rechercher par identifiant et renvoyer les résultats ou erreur 404
		member = get_object_or_404(Member, pk=id)
	else: #Quand il n'y a pas d'identifiant (quand neuf)
		#Créer un membre
		member = Member()

	#Au POST (lorsque le bouton d'enregistrement est enfoncé, que ce soit nouveau ou modifier)
	if request.method == 'POST':
		#Générer un formulaire
		form = MemberForm(request.POST, instance=member)
		if form.is_valid(): #Enregistrer si la validation est OK
			member = form.save(commit=False)
			member.save()
			return redirect('app:index')
	else: #Au moment de GET (générer un formulaire)
		form = MemberForm(instance=member)
	
	#Afficher un nouvel écran / modifier l'écran
	return render(request, 'app/members/edit.html', dict(form=form, id=id))

#Effacer
def delete(request, id=None):
	# return HttpResponse("Effacer")
	member = get_object_or_404(Member, pk=id)
	member.delete()
	return redirect('app:index')

#Détails (bonus)
def detail(request, id=None):
    member = get_object_or_404(Member, pk=id)
    return render(request, 'app/members/details.html', {'member':member})

