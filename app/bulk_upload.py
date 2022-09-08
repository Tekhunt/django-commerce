import pandas as pd

from .models.product_model import Product

def create(self, validated_data):

    df = pd.read_csv('/', sep='delimiter')
    products = []
    for i in range(len(df)):
        products.append(
            Product(
            name=df.iloc[i][0],
            description=df.iloc[i][1],
            price=df.iloc[i][2]
            )
        )
    instance = Product.objects.bulk_create(products)
    instance.save
    return instance