from django import forms
from .models import Course,Topic

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        
        fields = ('__all__')

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        
        fields = ['name','description','course','file']