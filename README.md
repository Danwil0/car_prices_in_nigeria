# Nigerian Car Market Analysis 

A data-driven exploration of car prices in Nigeria, scraping real listings from Cars45 and analyzing trends across different brands, locations, and vehicle conditions.

## The Idea

I saw a project idea online about scraping car listings and analyzing price trends, and I thought, why not do this for the Nigerian market? Nigeria has a unique car market with a mix of foreign-used (tokunbo), locally-used, and brand new vehicles. I wanted to understand:

- How quickly do cars depreciate here?
- Does location affect pricing?
- Which brands offer the best value for money?
- What's the real state of the market?

## What I Built

### 1. Web Scraper
Built a Python scraper that collects car listings from Cars45.com, including:
- Basic info (make, model, year, price, location)
- Detailed specs (engine size, mileage, transmission, horsepower)
- Condition and history

### 2. Data Cleaning Pipeline
Raw scraped data is messy. I cleaned:
- Removed currency symbols and formatted prices as numbers
- Standardized location data (split into state and city)
- Calculated car age from manufacturing year
- Handled missing values and outliers
- Dealt with inconsistent formats (like "5-7 seats")

### 3. PostgreSQL Database
Loaded all cleaned data into a PostgreSQL database with:
- Proper data types and constraints
- Indexes for fast queries
- 2,175 car listings with full details

### 4. SQL Analysis
Wrote queries to answer real questions:
- **Depreciation analysis**: How much value do cars lose over time?
- **Location pricing**: Is Lagos really more expensive?
- **Brand comparison**: Which brands hold their value best?
- **Value hunting**: Where are the best deals?

### 5. Jupyter Notebook Visualizations

## 📊 Key Findings

### Price Depreciation
- New cars (1-2 years): Average ₦90M+
- 10-year-old cars: Average ₦25M (72% depreciation!)
- 20-year-old cars: Average ₦5-6M

**Insight**: Cars lose most of their value in the first 10 years.

### Location Matters
- **Edo State**: Highest average prices (surprisingly)
- **Lagos State**: Second highest
- **Ondo State**: Among the lowest

### Brand Depreciation Champions
- **Lexus** depreciates the fastest (unexpected)
- **GAC** holds value better
- Mercedes-Benz surprisingly holds value better than Lexus in the Nigerian market

### Best Value Cars
The sweet spot for value? **Korean brands** (Kia, Hyundai, Nissan):
- Kia Rio 2014: ₦17.35 per km
- Affordable with reasonable mileage
- Good reliability for the price
