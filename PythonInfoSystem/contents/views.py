from django.shortcuts import get_object_or_404, render
from .forms import LoginForm, UserRegistrationForm
from .models import Topic

def index(request):
    topics_list = Topic.objects.all()
    context = {'topics_list': topics_list}
    return render(request, 'contents/index.html', context)

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'contents/topic_detail.html', {'topic': topic})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})