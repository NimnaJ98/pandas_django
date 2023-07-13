from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd

# Create your views here.

def chart_select_view(request):
    error_message = None
    df=None

    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())

    if purchase_df.shape[0] > 0:
        product_df['product_id'] = product_df['id']
        df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'date_y'], axis=1).rename({'id_x':'id', 'date_x':'date'}, axis=1)
        if request.method == 'POST':
            chart_type = request.POST.get('sales')
            date_from = request.POST['date_from']
            date_to = request.POST['date_to'] 

            df['date'] = df['date'].apply[lambda x: x.strftime('%Y-%m-%d')]
            df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')

            if chart_type != "":
                if date_from != "" and date_to != "":
                    df = df[(df['date']>date_from) & (df['date']<date_to)]
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    #function to get a graph
                    
            else:
                error_message = "Please select a chart type to continue"
    else:
        error_message = "No records found"

    context = {
        'error_message': error_message,
    }
    return render(request, 'products/main.html', context)