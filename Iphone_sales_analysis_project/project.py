# ==========================================
# iPhone Sales Data Analysis Project
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("/content/archive (2).zip")


# ==========================================
# 1. Data Understanding
# ==========================================

print("Rows and Columns:", df.shape)
print("\nData Types:")
print(df.dtypes)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())


# ==========================================
# 2. Data Inspection
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ==========================================
# 3. Data Cleaning
# ==========================================

# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Remove extra spaces from product name
df['product_name'] = df['product_name'].str.strip()

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Column Names:")
print(df.columns)

print("\nDataset Shape After Cleaning:")
print(df.shape)


# ==========================================
# 4. Data Transformation
# ==========================================

# Discount amount
df['discount_amount'] = df['mrp'] - df['sale_price']

# Price category
def price_category(price):
    if price < 40000:
        return 'Low'
    elif price < 70000:
        return 'Medium'
    elif price < 100000:
        return 'High'
    else:
        return 'Premium'

df['price_category'] = df['sale_price'].apply(price_category)

# Review-to-rating ratio
df['review_to_rating_ratio'] = df['number_of_reviews'] / df['star_rating'].replace(0, pd.NA)

# Extract iPhone model from product name
df['iphone_model'] = df['product_name'].str.extract(
    r'(iPhone\s+(?:SE|XR|XS|X|\d+\s*(?:Pro Max|Pro|Plus|Mini)?))',
    expand=False
)

# RAM number extraction
df['ram_num'] = df['ram'].str.extract(r'(\d+)').astype(float)

# RAM based phone category
def ram_category(ram):
    if ram <= 2:
        return 'Basic'
    elif ram <= 4:
        return 'Standard'
    elif ram <= 6:
        return 'High Performance'
    else:
        return 'Premium'

df['phone_category'] = df['ram_num'].apply(ram_category)

print("\nTransformed Dataset Preview:")
print(df[['product_name', 'iphone_model', 'sale_price', 'mrp',
          'discount_amount', 'price_category', 'ram',
          'phone_category', 'review_to_rating_ratio']].head())


# ==========================================
# 5. EDA Questions
# ==========================================

# 1. Top 10 most expensive iPhones
top_expensive = df.sort_values(by='sale_price', ascending=False).head(10)

print("\n1. Top 10 Most Expensive iPhones:")
print(top_expensive[['iphone_model', 'product_name', 'sale_price', 'price_category']])


# 2. Top 10 cheapest iPhones
top_cheapest = df.sort_values(by='sale_price', ascending=True).head(10)

print("\n2. Top 10 Cheapest iPhones:")
print(top_cheapest[['iphone_model', 'product_name', 'sale_price', 'price_category']])


# 3. Highest rated iPhone
highest_rated = df.sort_values(by='star_rating', ascending=False).head(1)

print("\n3. Highest Rated iPhone:")
print(highest_rated[['iphone_model', 'product_name', 'star_rating']])


# 4. Most reviewed iPhone
most_reviewed = df.sort_values(by='number_of_reviews', ascending=False).head(1)

print("\n4. Most Reviewed iPhone:")
print(most_reviewed[['iphone_model', 'product_name', 'number_of_reviews']])


# 5. Highest discount iPhone
highest_discount = df.sort_values(by='discount_percentage', ascending=False).head(1)

print("\n5. Highest Discount iPhone:")
print(highest_discount[['iphone_model', 'product_name', 'discount_percentage', 'discount_amount']])


# 6. Average sale price
avg_sale_price = df['sale_price'].mean()

print("\n6. Average Sale Price:")
print(round(avg_sale_price, 2))


# 7. Average MRP
avg_mrp = df['mrp'].mean()

print("\n7. Average MRP:")
print(round(avg_mrp, 2))


# 8. Average discount percentage
avg_discount_percentage = df['discount_percentage'].mean()

print("\n8. Average Discount Percentage:")
print(round(avg_discount_percentage, 2))


# 9. RAM category count
ram_category_count = df['phone_category'].value_counts()

print("\n9. RAM Category Count:")
print(ram_category_count)


# 10. Price category count
price_category_count = df['price_category'].value_counts()

print("\n10. Price Category Count:")
print(price_category_count)


# ==========================================
# 6. Analysis Questions
# ==========================================

# 1. Do high-price iPhones get more ratings?
price_rating_corr = df['sale_price'].corr(df['number_of_ratings'])

print("\nAnalysis 1. Sale Price vs Number of Ratings Correlation:")
print(price_rating_corr)

if price_rating_corr > 0:
    print("High-price iPhones have a positive relation with number of ratings.")
elif price_rating_corr < 0:
    print("High-price iPhones do not get more ratings. The relation is negative.")
else:
    print("There is no relation between price and number of ratings.")


# 2. Does higher discount increase reviews or rating?
discount_review_corr = df['discount_percentage'].corr(df['number_of_reviews'])
discount_rating_corr = df['discount_percentage'].corr(df['star_rating'])

print("\nAnalysis 2. Discount vs Reviews Correlation:")
print(discount_review_corr)

print("\nDiscount vs Star Rating Correlation:")
print(discount_rating_corr)

if discount_review_corr > 0:
    print("Higher discount has a positive relation with number of reviews.")
else:
    print("Higher discount does not have a strong positive relation with reviews.")

if discount_rating_corr > 0:
    print("Higher discount has a positive relation with star rating.")
else:
    print("Higher discount does not have a strong positive relation with rating.")


# 3. Do expensive iPhones have better ratings?
avg_rating_by_price = df.groupby('price_category')['star_rating'].mean().sort_values(ascending=False)

print("\nAnalysis 3. Average Rating by Price Category:")
print(avg_rating_by_price)


# 4. Which iPhone looks value-for-money?
df['value_score'] = (
    df['star_rating'] * 0.5 +
    df['discount_percentage'] * 0.3 +
    (df['number_of_reviews'] / df['number_of_reviews'].max()) * 0.2
)

value_for_money = df.sort_values(by='value_score', ascending=False).head(10)

print("\nAnalysis 4. Top 10 Value-for-Money iPhones:")
print(value_for_money[['iphone_model', 'product_name', 'sale_price',
                       'star_rating', 'discount_percentage',
                       'number_of_reviews', 'value_score']])


# 5. Sale price and MRP difference
print("\nAnalysis 5. Sale Price and MRP Difference:")
print(df[['iphone_model', 'product_name', 'mrp', 'sale_price', 'discount_amount']].head(10))

avg_discount_amount = df['discount_amount'].mean()

print("\nAverage Discount Amount:")
print(round(avg_discount_amount, 2))


# 6. Premium category iPhones
premium_iphones = df[df['price_category'] == 'Premium']

print("\nAnalysis 6. Premium Category iPhones:")
print(premium_iphones[['iphone_model', 'product_name', 'sale_price', 'price_category']])


# 7. High discount + high rating iPhones
avg_discount = df['discount_percentage'].mean()
avg_rating = df['star_rating'].mean()

high_discount_high_rating = df[
    (df['discount_percentage'] >= avg_discount) &
    (df['star_rating'] >= avg_rating)
]

print("\nAnalysis 7. High Discount + High Rating iPhones:")
print(high_discount_high_rating[['iphone_model', 'product_name', 'sale_price',
                                 'discount_percentage', 'star_rating']])


# ==========================================
# 7. Data Visualization
# ==========================================

# 1. Top 10 expensive iPhones bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_expensive['iphone_model'], top_expensive['sale_price'])
plt.title("Top 10 Most Expensive iPhones")
plt.xlabel("iPhone Model")
plt.ylabel("Sale Price")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()


# 2. Top 10 cheapest iPhones bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_cheapest['iphone_model'], top_cheapest['sale_price'])
plt.title("Top 10 Cheapest iPhones")
plt.xlabel("iPhone Model")
plt.ylabel("Sale Price")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()


# 3. Sale price distribution histogram
plt.figure(figsize=(10, 5))
plt.hist(df['sale_price'], bins=10)
plt.title("Sale Price Distribution")
plt.xlabel("Sale Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# 4. Rating distribution histogram
plt.figure(figsize=(10, 5))
plt.hist(df['star_rating'], bins=10)
plt.title("Rating Distribution")
plt.xlabel("Star Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# 5. Discount percentage distribution histogram
plt.figure(figsize=(10, 5))
plt.hist(df['discount_percentage'], bins=10)
plt.title("Discount Percentage Distribution")
plt.xlabel("Discount Percentage")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# 6. Sale price vs number of ratings scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(df['sale_price'], df['number_of_ratings'])
plt.title("Sale Price vs Number of Ratings")
plt.xlabel("Sale Price")
plt.ylabel("Number of Ratings")
plt.tight_layout()
plt.show()


# 7. Discount percentage vs number of ratings scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(df['discount_percentage'], df['number_of_ratings'])
plt.title("Discount Percentage vs Number of Ratings")
plt.xlabel("Discount Percentage")
plt.ylabel("Number of Ratings")
plt.tight_layout()
plt.show()


# 8. Price category count bar chart
plt.figure(figsize=(8, 5))
plt.bar(price_category_count.index, price_category_count.values)
plt.title("Price Category Count")
plt.xlabel("Price Category")
plt.ylabel("Number of iPhones")
plt.tight_layout()
plt.show()


# 9. RAM category count bar chart
plt.figure(figsize=(8, 5))
plt.bar(ram_category_count.index, ram_category_count.values)
plt.title("RAM Category Count")
plt.xlabel("RAM Category")
plt.ylabel("Number of iPhones")
plt.tight_layout()
plt.show()


# 10. Top 10 highest reviewed iPhones bar chart
top_reviewed = df.sort_values(by='number_of_reviews', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_reviewed['iphone_model'], top_reviewed['number_of_reviews'])
plt.title("Top 10 Highest Reviewed iPhones")
plt.xlabel("iPhone Model")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()


# 11. Correlation heatmap
corr_data = df[['sale_price', 'mrp', 'discount_percentage',
                'star_rating', 'number_of_ratings',
                'number_of_reviews', 'discount_amount']].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr_data, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# 12. Seaborn countplot for price category
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='price_category')
plt.title("Price Category Count using Seaborn")
plt.xlabel("Price Category")
plt.ylabel("Number of iPhones")
plt.tight_layout()
plt.show()


# 13. Seaborn scatter plot: Sale price vs ratings
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='sale_price', y='number_of_ratings', hue='price_category')
plt.title("Sale Price vs Number of Ratings by Price Category")
plt.xlabel("Sale Price")
plt.ylabel("Number of Ratings")
plt.tight_layout()
plt.show()


# ==========================================
# 8. Final Insights
# ==========================================

print("\nFinal Insights:")
print("1. The dataset contains", df.shape[0], "iPhone product records and", df.shape[1], "columns after transformation.")
print("2. There are no missing values and no duplicate rows in the original inspection.")
print("3. The average sale price is:", round(avg_sale_price, 2))
print("4. The average MRP is:", round(avg_mrp, 2))
print("5. The average discount percentage is:", round(avg_discount_percentage, 2))
print("6. The average discount amount is:", round(avg_discount_amount, 2))
print("7. Sale price and number of ratings correlation is:", round(price_rating_corr, 3))
print("8. Discount and number of reviews correlation is:", round(discount_review_corr, 3))
print("9. Discount and star rating correlation is:", round(discount_rating_corr, 3))
print("10. Premium category iPhones have an average rating of:", round(avg_rating_by_price.get('Premium', 0), 2))
print("11. High discount and high rating phones can be considered good deal options.")
print("12. Value-for-money score helps identify phones with good rating, discount, and reviews.")
