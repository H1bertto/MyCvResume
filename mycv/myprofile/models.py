from django.db import models
from datetime import date


class PortfolioManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) or models.Q(description__icontains=query))


class Portfolio(models.Model):
	title = models.CharField('Title', max_length=150)
	sub_title = models.CharField('Sub Title', max_length=250, blank=True, null=True)
	slug = models.SlugField('Slug', unique=True)
	text = models.TextField('Description')
	categories = models.ManyToManyField('myprofile.Category')
	technologies = models.ManyToManyField('myprofile.Technology')
	cover_image = models.ImageField(verbose_name='Cover', upload_to='portfolio/images')
	image_1 = models.ImageField(verbose_name='Image 1', blank=True, upload_to='portfolio/images')
	legenda_1 = models.CharField('Legenda 1', max_length=250, blank=True)
	image_2 = models.ImageField(verbose_name='Image 2', blank=True, upload_to='portfolio/images')
	legenda_2 = models.CharField('Legenda 2', max_length=250, blank=True)
	image_3 = models.ImageField(verbose_name='Image 3', blank=True, upload_to='portfolio/images')
	legenda_3 = models.CharField('Legenda 3', max_length=250, blank=True)
	url = models.CharField('Url Project', blank=True, null=True, max_length=400)
	url_info = models.CharField('Info Link', blank=True, null=True, max_length=30)
	visible = models.BooleanField('Visible', blank=True, default=True)

	objects = PortfolioManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Portfolio'
		verbose_name_plural = 'Portfolios'
		ordering = ['title']


class Service(models.Model):
	title = models.CharField('Title', max_length=50)
	description = models.TextField(max_length=150)
	icon = models.CharField('Icon', max_length=25)
	date = models.DateField('Date', auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Service'
		verbose_name_plural = 'Services'
		ordering = ['date']


class Category(models.Model):
	name = models.CharField('Name', max_length=80)
	slug = models.SlugField('Slug',)
	description = models.TextField()

	def __str__(self):
		return self.slug

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		ordering = ['name']


class Technology(models.Model):
	name = models.CharField('Name', max_length=50)
	slug = models.SlugField('Slug',)
	knowledge = models.IntegerField('% Knowledge', default=0)
	technical_skill = models.BooleanField('Technical Skill', blank=True, default=False)
	visible = models.BooleanField('Visible', blank=True, default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Technology'
		verbose_name_plural = 'Technologies'
		ordering = ['name']


class Profile(models.Model):
	name = models.CharField('Name', max_length=200)
	profession = models.CharField('Profession', max_length=200)	
	telephone = models.CharField('Telephone', max_length=30)
	adress = models.CharField('Adress', max_length=250)
	email = models.EmailField('Email')
	hire_me = models.TextField('Why Hire Me?')
	about = models.TextField()

	skill_1 = models.CharField('Professional Skill 1', max_length=50)
	value_skill_1 = models.IntegerField('% Of Skill 1', default=0)
	skill_2 = models.CharField('Professional Skill 2', max_length=50)
	value_skill_2 = models.IntegerField('% Of Skill 2', default=0)
	skill_3 = models.CharField('Professional Skill 3', max_length=50)
	value_skill_3 = models.IntegerField('% Of Skill 3', default=0)
	skill_4 = models.CharField('Professional Skill 4', max_length=50)
	value_skill_4 = models.IntegerField('% Of Skill 4', default=0)
	skill_5 = models.CharField('Professional Skill 5', max_length=50)
	value_skill_5 = models.IntegerField('% Of Skill 5', default=0)
	skill_6 = models.CharField('Professional Skill 6', max_length=50)
	value_skill_6 = models.IntegerField('% Of Skill 6', default=0)

	picture = models.ImageField(verbose_name='Your Piture', blank=True, upload_to='profile/images')	
	url_instagram = models.CharField('URL Instagram', max_length=350, blank=True)
	url_facebook = models.CharField('URL Facebook', max_length=350, blank=True)
	url_linkedin = models.CharField('URL LinkeIn', max_length=350, blank=True)
	url_twitter = models.CharField('URL Twitter', max_length=350, blank=True)
	url_github = models.CharField('URL GitHub', max_length=350, blank=True)
	
	url_cv = models.TextField('URL CV')
	url_strengths = models.TextField('URL Strengths', blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Profile'
		verbose_name_plural = 'Profiles'
		ordering = ['name']


class Education(models.Model):
	course = models.CharField('Course', max_length=150)
	institution = models.CharField('Institution', max_length=150)
	url_institution = models.CharField('Link of Institution', max_length=350)
	description = models.TextField()
	start_date = models.DateField('Start Date', default=date.today)
	end_date = models.DateField('End Date', blank=True, default=date.today)
	is_actual = models.BooleanField('Is Actual?', default=False)
	visible = models.BooleanField('Visible', default=True)

	def __str__(self):
		return self.course

	def get_start_year(self):
		return self.start_date.year

	def get_end_year(self):
		if self.is_actual:
			return '%s (Actual)' % self.end_date.year
		else:
			return self.end_date.year

	class Meta:
		verbose_name = 'Education'
		verbose_name_plural = 'Educations'
		ordering = ['-start_date']


class WorkExperience(models.Model):
	profession = models.CharField('Profession', max_length=100)
	company	= models.CharField('Company', max_length=100)
	role_1 = models.CharField('Role 1', max_length=100)
	role_2 = models.CharField('Role 2', max_length=100)	
	url_company	= models.CharField('Link of Company', max_length=350)
	start_date = models.DateField('Start Date', default=date.today)
	end_date = models.DateField('End Date', blank=True, default=date.today)
	is_actual = models.BooleanField('Is Actual?', default=False)
	visible = models.BooleanField('Visible', default=True)

	def __str__(self):
		return self.profession

	def get_start_year(self):
		return self.start_date.year

	def get_end_year(self):
		if self.is_actual:
			return '(Actual)'
		else:
			return self.end_date.year

	class Meta:
		verbose_name = 'Work Experience'
		verbose_name_plural = 'Work Experiences'
		ordering = ['-start_date']


class Review(models.Model):
	name = models.CharField('Name', max_length=100)
	role = models.CharField('Role', max_length=50, null=True)
	company = models.CharField('company', max_length=50)
	testimonial = models.TextField(max_length=125)
	review_picture = models.ImageField(verbose_name='Your Piture', blank=True, upload_to='review/images')	
	visible = models.BooleanField('Visible', default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Review'
		verbose_name_plural = 'Reviews'
		ordering = ['name']


class FeaturedProject(models.Model):
	title = models.CharField('Title', max_length=50)
	sub_title = models.CharField('Sub Title', max_length=100)
	category = models.ForeignKey('myprofile.Category', on_delete=models.deletion.CASCADE)
	description = models.TextField(max_length=400)
	url = models.CharField('Link of Project', max_length=350, blank=True, null=True)
	image = models.ImageField(verbose_name='Project ImageF', blank=True, upload_to='project/images')
	testimonial_name = models.CharField('Testimonial Name', max_length=150, blank=True, null=True)
	testimonial_text = models.TextField(max_length=130, blank=True, null=True)
	testimonial_role = models.CharField('Testimonial Role', max_length=100, blank=True, null=True)
	testimonial_company = models.CharField('Testimonial Company', max_length=50, blank=True, null=True)
	visible = models.BooleanField('Visible', default=True)
	date = models.DateField('Date', auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Featured Project'
		verbose_name_plural = 'Featured Projects'
		ordering = ['-date']