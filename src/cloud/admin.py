from django.contrib import admin
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	List_display = ["__unicode__", "timestamp", "updated"]
	class Meta:
		Model = SignUp


admin.site.register(SignUp, SignUpAdmin)

