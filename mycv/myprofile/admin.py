from django.contrib import admin
from .models import Portfolio, Category, Technology, Profile, Education
from .models import WorkExperience, Review, FeaturedProject, Service


class PortfolioAdmin(admin.ModelAdmin):
	list_display = ['title', 'sub_title']
	search_fields = ['title', 'sub_title', 'category', 'technologies']
	prepopulated_fields = {'slug': ('title',)}

class ServiceAdmin(admin.ModelAdmin):
	list_display = ['title', 'date']
	search_fields = ['title', 'date']	


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	search_fields = ['name']


class TechnologyAdmin(admin.ModelAdmin):
	list_display = ['name', 'visible', 'technical_skill']
	prepopulated_fields = {'slug': ('name',)}
	search_fields = ['name', 'visible', 'technical_skill']


class EducationAdmin(admin.ModelAdmin):
	list_display = ['course', 'start_date', 'end_date', 'is_actual', 'visible']
	search_fields = ['course', 'start_date', 'end_date', 'is_actual', 'visible']


class WorkExperienceAdmin(admin.ModelAdmin):
	list_display = ['profession', 'company', 'start_date', 'end_date', 'is_actual', 'visible']
	search_fields = ['profession', 'company', 'start_date', 'end_date', 'is_actual', 'visible']


class ReviewAdmin(admin.ModelAdmin):
	list_display = ['name', 'role', 'company', 'visible']
	search_fields = ['name', 'role', 'company', 'visible']

class FeaturedProjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'sub_title', 'category', 'testimonial_name', 'visible']
	search_fields = ['title', 'sub_title', 'category']


admin.site.register(FeaturedProject, FeaturedProjectAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Profile)
