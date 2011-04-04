# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.views.generic.simple import direct_to_template
from django.template import RequestContext

# Templates in Django need a "Context" to parse with, so we'll borrow this.
# "Context"'s are really nothing more than a generic dict wrapped up in a
# neat little function call.
from django.template import Context

from agenda.models import Person, Group
#from agenda.forms import RegistrationForm

def index(request):
        
        peopleList = Person.objects.order_by('name')
        
        data = {
            'agenda': peopleList,
        }
        
        return render_to_response('index.html', data, context_instance=RequestContext(request))
        
def detail(request, id, slug):
        
        person = get_object_or_404(Person, id=id)
        
        data = {
            'person': person,
        }
        
        return render_to_response('people/detail.html', data, context_instance=RequestContext(request))