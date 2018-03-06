from django.shortcuts import render

from helloworld.forms import HelloForm


def hello_user_name(request):
    """ Gets user name and returns to the template """

    template_name = 'helloworld/index.html'
    form = HelloForm()
    context = {'form': form}

    if request.method == 'GET':
        return render(request, template_name, context=context, status=200)

    elif request.method == 'POST':
        name = request.POST['name']
        context['name'] = name

        return render(request, template_name, context=context, status=200)
