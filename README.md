# Gurgaon-Real-Estate-Market-Analysis

📌 Project Overview
A comprehensive exploratory data analysis (EDA) project built using Python to analyze real estate property listings. This project processes raw housing data, standardizes and cleans the dataset, and extracts actionable insights regarding property pricing trends, locality rates, builder positioning, and regulatory impacts (RERA approval).

🛠️ Tech Stack & Libraries
Language: Python

Data Manipulation & Analysis: Pandas

Data Visualization: Matplotlib, Seaborn

⚙️ Data Cleaning & Preprocessing Pipeline
To ensure data integrity before analysis, the dataset underwent rigorous preprocessing:

Column Standardization: Normalized column headers to lowercase, stripped whitespaces, and replaced spaces with underscores (_).

Duplicate Removal: Filtered out duplicate records to prevent skewed analytical results.

Type Casting & Formatting: Cleaned numerical fields (price, rate_per_sqft) by removing commas and converting them to floating-point data types.

Categorical Normalization: Standardized text fields like status and flat_type, and mapped RERA approval statuses to boolean indicators for streamlined querying.

📊 Key Analytical Questions Addressed
The analysis answers several critical market research queries:

Cost Identification: Determines the absolute costliest flat in the dataset along with its complete configuration details (BHK, locality, builder, price in crores, and square-foot rate).

Locality Benchmarking: Identifies premium localities commanding the highest average property prices and highest average rates per square foot.

Property Status Trends: Compares pricing dynamics between ready-to-move and under-construction properties.

Regulatory Impact: Evaluates whether RERA-approved properties command a measurable price premium.

Configuration & Type Valuation: Analyzes which BHK configurations and property types (Apartment, Floor, Plot) lead the market in average cost.

Builder Positioning: Examines builder pricing strategies to identify developers with consistently higher property price averages.

Visual Correlations: Utilizes Seaborn scatter plots to visualize the relationship between area (sqft) versus total price and rate per square foot.
