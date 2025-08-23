from django.shortcuts import render, get_object_or_404
from .models import ChaiVarity, Store
from .forms import ChaiVarityForm   # ✅ corrected import

# Create your views here.
def home(request):
    return render(request, 'chaiapp/home.html')

def hello(request):
    return render(request, 'chaiapp/hello.html')

def index(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chaiapp/index.html', {'chais': chais})

def layout(request):
    return render(request, 'chaiapp/layout.html')

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chaiapp/chai_detail.html', {'chai': chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_variety)  # ✅ corrected Store
    else:
        form = ChaiVarityForm()

    return render(
        request,
        'chaiapp/chai_stores.html',
        {
            'stores': stores,
            'form': form   # ✅ corrected context
        }
    )
