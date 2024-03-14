from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
import csv

# path = r"C:\Home\ColorGen\products.csv"
def ims(request):

    # with open(path) as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         _, created = Product.objects.get_or_create(
    #         item_code=row[0],
    #         item_name=row[1],
    #         price = 1.0,
    #         tin_size=row[2],
    #         )
    return HttpResponse("Hello world!")