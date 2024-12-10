#import kagglehub
# Download latest version
#path = kagglehub.dataset_download("zeesolver/consumer-behavior-and-shopping-habits-dataset")

#print("Path to dataset files:", path)

import pandas as pd

##Load datasets
data1=pd.read_csv('ShoppingHabits/data/merged_data.csv')
data2=pd.read_csv('ShoppingHabits/data/shopping_behavior_updated.csv')
print(data1.head())
print(data1.describe())
data1 = data1.rename(columns={'Customer ID':'customer_id','Age':'age','Item Purchased':'item_purchased','Purchase Amount (USD)':'purchase_amount','Review Rating':'rating','Subscription Status':'subscription','Payment Method':'payment_method','Shipping Type':'shipping_type','Discount Applied':'discount','Promo Code Used':'promo_code','Previous Purchases':'previous_purchases','Preferred Payment Method':'preferred_pmt_method','Frequency of Purchases':'frq_purchases'})
print(data1.head())
data1.info()
data1['subscription'] = data1['subscription'].map({'Yes':1,'No':0})
data1['discount'] = data1['discount'].map({'Yes':1,'No':0})
data1['promo_code'] = data1['promo_code'].map({'Yes':1,'No':0})
data1['Gender'] = data1['Gender'].map({'Male':1,'Female':0})
print(data1['discount'].unique())
duplicate_rows=data1.duplicated()
print('Number of duplicate rows:', duplicate_rows.sum())
data1.columns = data1.columns.str.strip()
data1['purchase_amount'] = pd.to_numeric(data1['purchase_amount'], errors='coerce')
#Saving clean data to a new file merged_data.csv
data1.to_csv('ShoppingHabits/data/merged_data.csv', index=False)