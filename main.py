import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Data.csv')

#Data Cleaning

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df= df.drop_duplicates()

#Numerical Columns Cleaning
df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(',', '').astype(float)

#Categorical data cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True , 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()
df = df.drop_duplicates()

# print(df)

#Question 1 : Which is the costliest flat in the dataset?
#Solution:-
costliest_flat = df.loc[df['price'].idxmax()]
print("Answer 1 :-",f"The costliest flat in the dataset is a {costliest_flat['bhk_count']} BHK {costliest_flat['flat_type']} located in {costliest_flat['locality']}, priced at {costliest_flat['price']/10000000} crores. It is built by {costliest_flat['builder_name']} and has a rate per sqft of {costliest_flat['rate_per_sqft']}. The flat is currently {costliest_flat['status']} and RERA approval status is {costliest_flat['rera_approval']}.")

#Question 2 :- Which locality has the highest average price?
#Solution:-
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print("Answer 2 :-",f"The locality with the highest average price is {highest_avg_price_locality}.")

#Question 3 :- Which locality has the highest rate per square foot?
#Solution :- 
highest_avg_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print("Answer 3 :-",f"The locality with the highest average rate per square foot is {highest_avg_rate_locality}.")

#Question 4 :- Do ready-to-move properties cost more than under-construction properties?
#Solution :-
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status']== 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print("Answer 4 :-", f"Yes, ready-to-move properties cost more  than under-construction properties.")
else:
    print("Answer 4 :-", f"No, under-construction properties cost more  than ready-to-move properties.")


# Question 5 :- Do RERA-approved properties command a price premium?
# Solution :-
rera_approved_avg_price = df[df['rera_approval']== True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval']== False]['price'].mean()

if rera_approved_avg_price > rera_not_approved_avg_price:
    print("Answer 5 :-", f"Yes, RERA-approved properties command a price premium.")
else:
    print("Answer 5 :-", f"No, RERA-approved properties do not command a price premium.")

# Question 6 :- How does area (sqft) impact property price?
#Solution :- 
# sns.scatterplot(data=df, x='area', y='price')
# plt.show()

#Question 7 :-Which BHK configuration is the most expensive on average?
#SOlution :-
most_expensive_bhk = df.groupby('bhk_count')['price'].mean().idxmax()
print("Answer 7 :-", f"The most expensive BHK configuration on average is {most_expensive_bhk} BHK.")

#Question 8 :-Which property type (Apartment, Floor, Plot) is the costliest based on rate per square foot?
#SOlution :-
costliest_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print("Answer 8 :-", f"The costliest property type on average is {costliest_property_type}.")
#Question 9 :-Do certain builders or companies consistently price higher?
#SOlution :-
most_expensive_builder = df.groupby("builder_name")['price'].mean().idxmax()
print("Answer 9 :-",f"The builder with the most expensive properties on average is {most_expensive_builder}.")
#Question 10 :-Are larger homes always more expensive per square foot?
#SOlution :-
sns.scatterplot(data=df, x='area', y = 'rate_per_sqft')
plt.show()