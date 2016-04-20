from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

from base.forms import TextForm
from base.models import Text

def index(request):
    """
    Serves home page
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = TextForm()
        return render(request, 'base/index.html', {'form': form})
    elif request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['test_text_input']
            save_text = Text.objects.create(text=text)
            pk = save_text.id
            return redirect('/text-display/' + str(pk) + '/')
        else:
            return render(request, 'base/index.html', {'form': form})
    else:
        return HttpResponseNotAllowed(['POST', 'GET'])

def text_display(request, text_id):
    """
    Serves test display page
    :param request: HTTP request
    :param text_id: text pk
    :return:
    """
    if request.method == 'GET':
        text = Text.objects.get(pk=text_id)
        return render(
            request,
            'base/text_display.html',
            {'text': text.text}
        )

    else:
        return HttpResponseNotAllowed(['GET'])
