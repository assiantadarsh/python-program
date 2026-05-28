import pandas as pd
import matplotlib.pyplot as plt

# Download Data set -> https://www.kaggle.com/search?q=netflix+dataset
df = pd.read_csv("/content/netflix_titles.csv.zip")

# 1. Data Understanding
print("Rows and Columns ",df.shape)

# 2. Data Inspect
print(df.info())
print(df.isnull().sum())
print("Duplicated Values ",df.duplicated().sum())

# 3. Data cleaning
print(df.dtypes)
df['title'] = df['title'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['director'] = df['director'].fillna('unknown')
df['cast'] = df['cast'].fillna('unknown')
df['country'] = df['country'].fillna('unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df = df.drop_duplicates(subset=['title','type','release_year'])

# 4. Data Transformation
df['year_added'] = df['date_added'].dt.year
df['duration_num'] = df['duration'].str.extract(r'(\d+)').astype(float)
df['duration_unit'] = df['duration'].apply(lambda x: 'Season' if 'Season' in str(x) else 'Minute')
df['primary_genre'] = df['listed_in'].str.split(',').str[0].str.strip()

# 5. EDA summaries
print(df['type'].value_counts())
print(df['country'].value_counts().head(10))
print(df['rating'].value_counts().head(10))
print(df['primary_genre'].value_counts().head(10))

# 6. Basic charts
df['type'].value_counts().plot(kind='bar', title='Content Type Count')
plt.show()
df['country'].value_counts().head(10).plot(kind='bar', title='Top 10 Countries')
plt.show()

