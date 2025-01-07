# health_analysis.py - gorkembiyikli
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

def load_data():
    df = pd.read_csv('DSA210 DATA.csv', sep=';', decimal=',')
    
    print("\nOriginal date formats:")
    print(df['Date'].head())
    
    def convert_date(date_str):
        try:
            return pd.to_datetime(date_str, format='%d.%m.%Y')
        except:
            try:
                return pd.to_datetime(date_str, format='%d/%m/%Y')
            except:
                print(f"Problem converting date: {date_str}")
                return None

    df['Date'] = df['Date'].apply(convert_date)
    
    print("\nConverted dates:")
    print(df['Date'].head())
    
    df = df.sort_values('Date')
    
    # Split blood pressure into systolic and diastolic
    df[['Systolic', 'Diastolic']] = df['Blood Pressure (mmHg)'].str.split('/', expand=True).astype(int)
    
    print("\nFull date range:")
    print(df['Date'].sort_values().to_list())
    
    return df

class HealthAnalysis:
    def __init__(self, data):
        self.data = data
        
    def analyze_active_times(self):
        exercise_stats = self.data.groupby('Exercise Type').agg({
            'Step Count': 'mean',
            'Heart Rate (avg bpm)': 'mean',
            'Sleep Quality (%)': 'mean',
            'Calories (kcal)': 'mean',
            'Exercise Duration (min)': 'mean'
        }).round(2)
        
        return exercise_stats
    
    def visualize_trends(self):
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # 1. Daily Steps
        self.data.plot(x='Date', y='Step Count', kind='line', ax=ax1)
        ax1.set_title('Daily Step Count')
        ax1.tick_params(axis='x', rotation=45)
        
        # 2. Exercise Type Distribution
        exercise_counts = self.data['Exercise Type'].value_counts()
        exercise_counts.plot(kind='pie', ax=ax2, autopct='%1.1f%%')
        ax2.set_title('Exercise Type Distribution')
        
        # 3. Sleep Quality vs Exercise Duration
        sns.scatterplot(data=self.data, x='Exercise Duration (min)', 
                       y='Sleep Quality (%)', hue='Exercise Type', ax=ax3)
        ax3.set_title('Sleep Quality vs Exercise Duration')
        
        # 4. Weight Trends with Blood Pressure
        ax4_twin = ax4.twinx()
        self.data.plot(x='Date', y='Weight (kg)', ax=ax4, color='blue', label='Weight')
        self.data.plot(x='Date', y='Systolic', ax=ax4_twin, color='red', label='Systolic BP')
        ax4.set_title('Weight and Blood Pressure Trends')
        ax4.tick_params(axis='x', rotation=45)
        
        # Combine legends
        lines1, labels1 = ax4.get_legend_handles_labels()
        lines2, labels2 = ax4_twin.get_legend_handles_labels()
        ax4_twin.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
        
        plt.tight_layout()
        plt.show()
    
    def generate_health_report(self):
        stats = {
            'Average_Steps': self.data['Step Count'].mean(),
            'Average_Sleep_Quality': self.data['Sleep Quality (%)'].mean(),
            'Most_Common_Exercise': self.data['Exercise Type'].mode()[0],
            'Average_Calorie_Intake': self.data['Calories (kcal)'].mean(),
            'Weight_Change': self.data['Weight (kg)'].iloc[-1] - self.data['Weight (kg)'].iloc[0],
            'Average_Blood_Pressure': f"{self.data['Systolic'].mean():.0f}/{self.data['Diastolic'].mean():.0f}",
            'Average_Water_Intake': self.data['Water Intake (L)'].mean()
        }
        
        # Calculate exercise day vs non-exercise day statistics
        exercise_days = self.data[self.data['Exercise Type'] != 'No Exercise']
        non_exercise_days = self.data[self.data['Exercise Type'] == 'No Exercise']
        
        stats.update({
            'Exercise_Days_Avg_Sleep': exercise_days['Sleep Quality (%)'].mean(),
            'Non_Exercise_Days_Avg_Sleep': non_exercise_days['Sleep Quality (%)'].mean(),
            'Exercise_Days_Avg_HR': exercise_days['Heart Rate (avg bpm)'].mean(),
            'Non_Exercise_Days_Avg_HR': non_exercise_days['Heart Rate (avg bpm)'].mean()
        })
        
        return stats

def main():
    df = load_data()
    
    analysis = HealthAnalysis(df)
    
    exercise_stats = analysis.analyze_active_times()
    print("\nExercise Statistics:")
    print(exercise_stats)
    
    report = analysis.generate_health_report()
    print("\nHealth Report:")
    for key, value in report.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")
    
    analysis.visualize_trends()

if __name__ == "__main__":
    main() 