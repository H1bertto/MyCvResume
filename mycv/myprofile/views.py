from django.shortcuts import render
from .models import Portfolio, Category, Technology, Profile, Education
from .models import WorkExperience, Review, FeaturedProject, Service
from .forms import ContactForm


def home(request):
	profile = Profile.objects.get(id=1)

	featured_projects = FeaturedProject.objects.all()
	work_experiences = WorkExperience.objects.all()
	technologies = Technology.objects.all()
	educations = Education.objects.all()
	portfolios = Portfolio.objects.all()
	categories = Category.objects.all()
	services = Service.objects.all()
	reviews = Review.objects.all()

	technical_skills = technologies.order_by('-knowledge')

	context = {		
		'featured_projects': featured_projects,
		'work_experiences': work_experiences,
		'technical_skills': technical_skills,
		'technologies': technologies,
		'portfolios': portfolios,
		'categories': categories,
		'educations': educations,
		'services': services,
		'reviews': reviews,
		'profile': profile,
		}
	
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail()
			form = ContactForm()
	else:
		form = ContactForm()

	context['form'] = form

	return render(request, 'pages/home.html', context)


def error_404(request):
	return render(request, 'pages/err404.html')