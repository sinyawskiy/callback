# coding=utf-8
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from questions.forms import CallbackForm


class CallbackView(FormView):
    form_class = CallbackForm
    template_name = 'callback_form.html'
    #success_url = ''#reverse('questions:callback')

    def form_valid(self, form):
        form.save()
        return super(CallbackView, self).form_valid(form)

    def __init__(self, *args, **kwargs):
        self.success_url = reverse('questions:callback')
        return super(CallbackView, self).__init__(*args, **kwargs)


