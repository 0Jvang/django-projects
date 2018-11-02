from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        '''UserCreationForm 的 Meta 内部类下的 model 属性对应的是 auth.User 模型。
        而 RegisterForm 通过覆写父类 model 属性的值，将其改为 users.User。'''
        model = User
        fields = ('username', 'email')