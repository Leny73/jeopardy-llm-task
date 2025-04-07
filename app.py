import os
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from datetime import datetime
import re

# Function to remove HTML tags
def remove_html_tags(text):
    return re.sub(r'<.*?>', '', text)

Base = declarative_base()


class JeopardyQuestion(Base):
    __tablename__ = 'jeopardy_questions'
    id = Column(Integer, primary_key=True)
    show_number = Column(Integer)
    air_date = Column(Date)
    round = Column(String)
    category = Column(String)
    value = Column(Integer)
    question = Column(String)
    answer = Column(String)

# Replace 'username', 'password', 'localhost', 'database_name' with your PostgreSQL credentials

engine = create_engine('postgresql://postgres:postgresroot@localhost/jeopardy-llm')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Load the dataset
df = pd.read_csv('JEOPARDY_CSV.csv')

# Replace dollar sign in Value column
df['Value'] = df['Value'].replace({'\$': ''}, regex=True)
# Replace empty strings with NaN
df['Value'] = df['Value'].replace('', pd.NA)
# Replace NaN values with 0
df['Value'] = df['Value'].fillna(0)
# Convert 'Value' column to numeric, coercing errors to NaN
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
# Drop rows with NaN values in 'Value' after conversion
df = df.dropna(subset=['Value'])
# Convert 'Value' to integer
df['Value'] = df['Value'].astype(int)
# Filter the DataFrame to include only rows with a value of 1200 or more
df = df[df['Value'] <= 1200]
# Ensure the 'Value' column is numeric
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
# Drop rows with NaN values in 'Value' after conversion
df = df.dropna(subset=['Value'])


# Remove a tags from dataset
df['Question'] = df['Question'].apply(remove_html_tags)

# Insert filtered rows into the database in batches
BATCH_SIZE = 1000  # Adjust the batch size as needed
rows = []

for index, row in df.iterrows():
    question = JeopardyQuestion(
        show_number=row['Show Number'],
        air_date=datetime.strptime(row['Air Date'], '%Y-%m-%d'),
        round=row['Round'],
        category=row['Category'],
        value=row['Value'],
        question=row['Question'],
        answer=row['Answer']
    )
    rows.append(question)

    # Insert rows in batches
    if len(rows) >= BATCH_SIZE:
        session.bulk_save_objects(rows)
        session.commit()
        rows = []  # Clear the batch

# Insert any remaining rows
if rows:
    session.bulk_save_objects(rows)
    session.commit()

print("Data successfully inserted into the database.")