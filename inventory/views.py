from django.shortcuts import render , redirect
from.forms import ProductUploadForm
from .models import Product

# Create your views here.


# Create your views here.def product_upload_view(request):
def product_upload_view(request):
    if request .method=="POST":
        form =ProductUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ProductUploadForm
              
   
    return render(request,"inventory/product_upload.html",{"form":form})

def products_list(request):
    products=Product.objects.all()
    return render (request,"inventory/product_list.html",{"products":products})
    

def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,"inventory/product_details.html", {"product":product})


def product_update_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
         form = ProductUploadForm(request.POST, instance=product)
         if form.is_valid():
            form.save()
            return redirect("product_detail", id=product.id)
    else:
            form = ProductUploadForm(instance=product)
            return render(request, "inventory/edit_product.html", {'form': form})
    



def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)

    # Perform cart-related logic, such as adding the product to the cart
    # ...

    return redirect('products_list')  # Redirect back to the product list
    