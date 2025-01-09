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

    def format_water_intake(value):
        try:
            # Convert to string and take first two digits plus one decimal
            str_val = str(value).replace('.', '')  # Remove all dots
            formatted = float(str_val[:2] + '.' + str_val[2])  # Format as X.X
            return formatted
        except:
            return None

    df['Date'] = df['Date'].apply(convert_date)
    
    print("\nConverted dates:")
    print(df['Date'].head())
    
    df = df.sort_values('Date')
    
    # Apply water intake formatting
    df['Water Intake (L)'] = df['Water Intake (L)'].apply(format_water_intake)
    
    # Split blood pressure into systolic and diastolic
    # First fill NaN values with a default value (e.g., '0/0')
    df['Blood Pressure (mmHg)'] = df['Blood Pressure (mmHg)'].fillna('0/0')
    df[['Systolic', 'Diastolic']] = df['Blood Pressure (mmHg)'].str.split('/', expand=True).astype(int)
    
    # Remove rows where blood pressure is 0/0 if you don't want to include them in analysis
    df = df[~((df['Systolic'] == 0) & (df['Diastolic'] == 0))]
    
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
        # Create a figure with multiple subplots
        fig = plt.figure(figsize=(20, 15))
        gs = plt.GridSpec(3, 3, figure=fig)
        
        # Convert dates to ordinal numbers for regression
        date_ordinal = [pd.Timestamp(d).toordinal() for d in self.data['Date']]
        
        # 1. Daily Steps with trend line (top left)
        ax1 = fig.add_subplot(gs[0, 0])
        sns.regplot(x=date_ordinal, y=self.data['Step Count'], ax=ax1, scatter_kws={'alpha':0.5})
        # Convert ordinal ticks back to dates
        tick_positions = ax1.get_xticks()
        tick_labels = [pd.Timestamp.fromordinal(int(tick)).strftime('%Y-%m-%d') for tick in tick_positions]
        ax1.set_xticklabels(tick_labels)
        ax1.set_title('Daily Steps Trend')
        ax1.tick_params(axis='x', rotation=45)
        
        # 2. Exercise Type Distribution (top middle)
        ax2 = fig.add_subplot(gs[0, 1])
        exercise_counts = self.data['Exercise Type'].value_counts()
        exercise_counts.plot(kind='pie', ax=ax2, autopct='%1.1f%%')
        ax2.set_title('Exercise Type Distribution')
        
        # 3. Sleep Quality Distribution by Exercise Type (top right)
        ax3 = fig.add_subplot(gs[0, 2])
        sns.violinplot(data=self.data, x='Exercise Type', y='Sleep Quality (%)', ax=ax3)
        ax3.set_title('Sleep Quality by Exercise Type')
        ax3.tick_params(axis='x', rotation=45)
        
        # 4. Heart Rate vs Exercise Duration Scatter (middle left)
        ax4 = fig.add_subplot(gs[1, 0])
        sns.scatterplot(data=self.data, x='Exercise Duration (min)', 
                       y='Heart Rate (avg bpm)', hue='Exercise Type', ax=ax4)
        ax4.set_title('Heart Rate vs Exercise Duration')
        
        # 5. Weight Trend with Confidence Interval (middle middle)
        ax5 = fig.add_subplot(gs[1, 1])
        sns.regplot(x=date_ordinal, y=self.data['Weight (kg)'], ax=ax5)
        # Convert ordinal ticks back to dates
        tick_positions = ax5.get_xticks()
        tick_labels = [pd.Timestamp.fromordinal(int(tick)).strftime('%Y-%m-%d') for tick in tick_positions]
        ax5.set_xticklabels(tick_labels)
        ax5.set_title('Weight Trend Over Time')
        ax5.tick_params(axis='x', rotation=45)
        
        # 6. Blood Pressure Distribution (middle right)
        ax6 = fig.add_subplot(gs[1, 2])
        sns.boxplot(data=self.data[['Systolic', 'Diastolic']], ax=ax6)
        ax6.set_title('Blood Pressure Distribution')
        
        # 7. Correlation Heatmap (bottom left)
        ax7 = fig.add_subplot(gs[2, 0])
        numeric_cols = ['Step Count', 'Heart Rate (avg bpm)', 'Sleep Quality (%)', 
                       'Calories (kcal)', 'Water Intake (L)', 'Weight (kg)', 
                       'Exercise Duration (min)', 'Systolic', 'Diastolic']
        correlation = self.data[numeric_cols].corr()
        sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', ax=ax7)
        ax7.set_title('Correlation Matrix')
        ax7.tick_params(axis='x', rotation=45)
        
        # 8. Exercise Duration Distribution (bottom middle)
        ax8 = fig.add_subplot(gs[2, 1])
        sns.boxplot(data=self.data, x='Exercise Type', y='Exercise Duration (min)', ax=ax8)
        ax8.set_title('Exercise Duration by Type')
        ax8.tick_params(axis='x', rotation=45)
        
        # 9. Sleep Quality vs Heart Rate (bottom right)
        ax9 = fig.add_subplot(gs[2, 2])
        sns.scatterplot(data=self.data, x='Heart Rate (avg bpm)', 
                       y='Sleep Quality (%)', hue='Exercise Type', ax=ax9)
        ax9.set_title('Sleep Quality vs Heart Rate')
        
        plt.tight_layout()
        plt.show()
        
        # Additional Time Series Plots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Time Series Analysis', fontsize=16)
        
        # Steps and Heart Rate
        ax1 = axes[0, 0]
        sns.lineplot(data=self.data, x='Date', y='Step Count', ax=ax1)
        ax1_twin = ax1.twinx()
        sns.lineplot(data=self.data, x='Date', y='Heart Rate (avg bpm)', 
                    ax=ax1_twin, color='red')
        ax1.set_title('Steps and Heart Rate Over Time')
        ax1.tick_params(axis='x', rotation=45)
        
        # Sleep Quality and Water Intake
        ax2 = axes[0, 1]
        sns.lineplot(data=self.data, x='Date', y='Sleep Quality (%)', ax=ax2)
        ax2_twin = ax2.twinx()
        sns.lineplot(data=self.data, x='Date', y='Water Intake (L)', 
                    ax=ax2_twin, color='green')
        ax2.set_title('Sleep Quality and Water Intake Over Time')
        ax2.tick_params(axis='x', rotation=45)
        
        # Blood Pressure Over Time
        ax3 = axes[1, 0]
        sns.lineplot(data=self.data, x='Date', y='Systolic', label='Systolic', ax=ax3)
        sns.lineplot(data=self.data, x='Date', y='Diastolic', label='Diastolic', ax=ax3)
        ax3.set_title('Blood Pressure Over Time')
        ax3.tick_params(axis='x', rotation=45)
        
        # Exercise Duration and Calories
        ax4 = axes[1, 1]
        sns.scatterplot(data=self.data, x='Exercise Duration (min)', 
                       y='Calories (kcal)', hue='Exercise Type', ax=ax4)
        ax4.set_title('Calories vs Exercise Duration')
        
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