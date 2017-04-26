from django.shortcuts import render, redirect
from models import Note
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
def index(request):
	context = {
		'notes': Note.objects.all()
	}
	return render(request, "posts/index.html", context)

def post(request):
	Note.objects.create(text=request.POST['text'])

	context = {
		'notes': Note.objects.all()
	}

	return render(request, "posts/post_index.html", context)

def delete(request, note_id):
	Note.objects.get(id=note_id).delete()

	context = {
		'notes': Note.objects.all()
	}

	return render(request, "posts/post_index.html", context)

def edit(request, note_id):

	context = {
		'notes': Note.objects.all(),
		'note_id': int(note_id),
		'edit': True,
	}

	# print type(context['notes'][0].id)
	# print type(context['note_id'])

	return render(request, "posts/post_index.html", context)

def save(request, note_id):
	# print "Hello!!!"
	Note.objects.filter(id=note_id).update(text=request.POST['text'])

	context = {
		'notes': Note.objects.all(),
	}

	# print type(context['notes'][0].id)
	# print type(context['note_id'])

	return render(request, "posts/post_index.html", context)
