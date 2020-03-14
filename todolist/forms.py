from django import forms

from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('todo', 'author')

        widgets = {
            'todo': forms.TextInput(
                attrs={
                    'id': 'inputPassword2',
                    'class': 'form-control',
                    'placeholder': 'Add your todo'
                }
            )
        }

    # def save(self):
    #     new_todo = Todo.objects.create(
    #         todo= self.cleaned_data["todo"],
    #         author= self.request.User,
    #     )
    #     return new_todo
