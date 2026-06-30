# Body Fat Analysis

A NumPy-based data analysis project exploring relationships between body measurements and body fat percentage using a real-world dataset.

## What It Does

- Loads a real body fat dataset (252 individuals)
- Calculates body fat statistics (min, max, average)
- Extracts and analyzes age data
- Derives BMI (Body Mass Index) from weight and height measurements
- Formats and displays analysis results

## Features

✅ Real dataset with 252 individuals
✅ 15 measurements including body fat %, age, weight, height, and circumference measurements
✅ Statistical analysis (min, max, average)
✅ BMI calculation and analysis
✅ Clean formatted output

## Data

- **Source**: Body Fat Dataset (standard ML dataset)
- **Rows**: 252 individuals
- **Columns**: 15 (Density, BodyFat, Age, Weight, Height, and body measurements)
- **Target**: Body Fat Percentage

## Usage

```bash
python bodyfat_analysis.py
```

Output will show:
- Minimum and maximum age
- Minimum and maximum body fat percentage
- Average body fat percentage
- All individual BMI values
- Average BMI

## Key Measurements

- Body Fat % — target variable
- Age — in years
- Weight — in lbs
- Height — in inches
- Measurements — Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm, Wrist (in cm)

## What You Learn

- Loading CSV data with NumPy
- Extracting specific columns from arrays
- Calculating basic statistics (min, max, mean)
- Deriving new metrics from raw data (BMI calculation)
- Array slicing and indexing
- Data formatting and display

## Next Steps

This dataset will be used for:
1. Correlation analysis (which measurements predict body fat best?)
2. Visualization with Matplotlib
3. Predictive modeling with Scikit-learn

