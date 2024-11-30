# gorkembiyikli_dsa210_termproject
Dsa210 Health and Exercise Data


# Health and Exercise Data Analysis

## Table of Contents
1. [Motivation](#motivation)
2. [Tools](#tools)
3. [Data Source](#data-source)
4. [Data Processing](#data-processing)
5. [Data Visualizations](#data-visualizations)
6. [Data Analysis](#data-analysis)
   - [Active Times](#active-times)
   - [Exercise Trends](#exercise-trends)
   - [Calorie and Water Consumption Patterns](#calorie-and-water-consumption-patterns)
   - [Trends in Health Metrics](#trends-in-health-metrics)
7. [Findings](#findings)
   - [Daily Activity Patterns](#daily-activity-patterns)
   - [Exercise and Health Relationships](#exercise-and-health-relationships)
   - [Trends in Weight Fluctuations](#trends-in-weight-fluctuations)
8. [Limitations](#limitations)
   - [Data-Sourced Limitations](#data-sourced-limitations)
   - [Personal Limitations](#personal-limitations)
9. [Future Work](#future-work)

---

## Motivation
In this era where personal health is increasingly important, analyzing daily exercise and behaviors offers important insights. This project aims to analyze data over a 2-month period, focusing on sleep quality, heart rate, physical exercise, and other measurements. The main goal is to reveal improved and actionable findings by examining past activities and behaviors for a healthier life.

---

## Tools
- **Python**: Examination and analysis of data in code.  
- **Pandas**: Organizing, filtering, and cleaning the dataset.  
- **Excel**: Initial data processing and organization.  

---

## Data Source
### 1. Personal Health Data:
- Data collected from an Apple health tracking app and Apple Watch from November 2023 to December 2023.  
- Performance indicators include step count, exercise type, exercise duration, heart rate, blood pressure, sleep quality, calorie intake, water intake, and weight.  

### 2. Custom Categories and Insights:
- Exercise types: Walking, Running, Pilates, Football, and No Exercise.  
- Weight dynamically adjusted based on calorie consumption and activity level.  

---

## Data Processing
- Chronologically sorted data from **11.01.2023** to **12.31.2023**.  
- Weight values were adjusted daily according to activity levels and calorie intake.  
- Segregated data into exercise and non-exercise days for comparative analysis.  
- Calculated the daily average of sleep quality, calorie intake, and heart rate.  

---

## Data Visualizations
### 1. Daily and Weekly Trends:
- Bar graphs of step counts and exercise duration, daily.  
- Line graphs showing weekly trends in heart rate and sleep quality.  

### 2. Health Metrics Insights:
- Pie charts for categorizing the time spent on each exercise type.  

### 3. Calorie and Water Intake Patterns:
- Scatter plots that visualize the relationship between calorie consumption and exercise duration.  

---

## Data Analysis
### Active Times
- Peaks were observed in morning and afternoon periods, both between **6 AM - 9 AM** and between **4 PM - 7 PM**, reflecting common exercises.  
- The late night, or from **10 PM to 6 AM**, showed the least activity, which was as expected for rest time.  

### Exercise Trends
- Football is played no more than twice a week, as it is exhausting.  
- Running and walking were the most consistent exercise routines, showing steady durations throughout the week.  

### Calorie and Water Consumption Patterns
- Higher water intake was observed on exercise days compared to non-exercise days.  
- Calorie consumption correlated strongly with exercise intensity, showing spikes on highly active days.  

### Trends in Health Metrics
- Sleep quality improved by an average of 15% on active days compared to non-exercise days.  
- Blood pressure showed better regulation on exercise days, with lower systolic and diastolic averages.  

---

## Findings
### Daily Activity Patterns
- Active days featured higher calorie consumption and water intake, reflecting increased energy expenditure.  
- Non-exercise days were characterized by poorer sleep quality and a slightly higher resting heart rate.  

### Exercise and Health Relationships
- Regular exercise brought consistent improvements in blood pressure and sleep quality measures.  
- Football, while intense, nonetheless elicited moderate caloric expenditure and favorable changes in cardiovascular health.  

### Trends in Weight Fluctuations
- Weight was higher with increased calorie days and on days of less activity.  
- Weight decreased on low-calorie intake days or days with intense physical activity.  

---

## Limitations
### Data-Sourced Limitations
- Limited to two months of data, which may not capture seasonal or long-term trends.  
- Quantitative measures, such as calorie intake, are based partly on manual input, introducing minor inconsistencies.  

### Personal Limitations
- The data concerns the health of one individual and may not generalize to larger populations.  

---

## Future Work
1. **Extended Data Collection**: Include data for at least six months or one year to capture any trends based on seasons.  
2. **Machine Learning Models**: Build predictors for weight variation, quality of sleep, and level of activity.  
3. **Interactive Dashboards**: Use either Power BI or Tableau for dynamic exploration of data in real time.  
4. **Behavioral Recommendations**: Offer personalized suggestions based on the observed trends toward better health metrics.  





