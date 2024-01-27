import pandas as pd
from faker import Faker
import random
import datetime
from datetime import datetime, timedelta


# Initialize Faker for generating random data
fake = Faker()

# Create an empty DataFrame to store sales data
sales_data = pd.DataFrame(columns=[
    "Product Name", "Generic Name",
    "Date", "Region", "Speciality", "Channel", "Volume", "Sales_Cost"
])

# Product
prdt = pd.read_excel('prdt_list.xlsx')

product_name1 = prdt.Product_Name.tolist()
generic_name1 = prdt.Gnrc_Name.tolist()
# Number of rows to generate (2 million in this case)
num_rows = 3660
# product_name[0]
d = datetime.today() - timedelta(days=3660 + k)
d
# Generate sales data for the specified number of rows
for p in range(0,len(product_name1)):
    for k,_ in enumerate(range(num_rows)):
        product_name = product_name1[p] #fake.random_element(
            # elements=(product_name[0]))
        generic_name = generic_name1[p] # fake.random_element(
            # elements=(generic_name[0]))
        d = datetime.today() - timedelta(days=3660 + k)
        # d.strftime("%d/%m/%Y")
        date = d.strftime("%d/%m/%Y") # fake.date_between(start_date='-3660d', end_date='today')
        region = fake.random_element(elements=('North', 'South', 'East', 'West', 'Central'))
        speciality = fake.random_element(
            elements=('Pain Relief', 'Antibiotics', 'Cardiovascular', 'Respiratory', 'Allergy', 'Gastrointestinal'))
        channel = fake.random_element(elements=('Retail', 'Online', 'Wholesale'))
        volume = random.randint(1, 1000)
        sales_cost = round(random.uniform(10.0, 1000.0), 2)
        print(type(product_name),type(generic_name),type(date),type(region),type(speciality),type(channel),type(volume),type(sales_cost))
        df2 = pd.DataFrame({
                                                            "Product Name": [product_name],
                                                            "Generic Name": [generic_name],
                                                            "Date": [date],
                                                            "Region": [region],
                                                            "Speciality": [speciality],
                                                            "Channel": [channel],
                                                            "Volume": [volume],
                                                            "Sales Cost": [sales_cost]
                                                        })
        sales_data = pd.concat([sales_data,df2])
sales_data.shape
# Save the generated data to a CSV file
sales_data.to_csv("pharma_sales_data_5M_rows.csv", index=False)

print("Pharma sales data generation completed.")
