import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_clean_data(df: pd.DataFrame):
    """Visualize the cleaned data with various plots."""
    
    # Define categorical and numerical columns
    catg_cols = ['gender', 'type of travel', 'class', 'customer type', 'satisfaction'] # categorical columns
    num_cols = ['age', 'flight distance', 'departure delay in minutes', 'arrival delay in minutes'] # numerical columns

    review_cols = ['inflight wifi service', 'departure/arrival time convenient', 
                'ease of online booking', 'gate location'] # review columns

    review_cols_2 = ['food and drink', 'online boarding', 'seat comfort', 
                    'inflight entertainment', 'on board service'] # additional review columns

    review_cols = ['inflight wifi service', 'departure/arrival time convenient', 'ease of online booking', 'gate location', 'food and drink', 'online boarding', 'seat comfort', 
                 'inflight entertainment', 'on board service', 'leg room service', 'baggage handling', 'checkin service', 'inflight service', 'cleanliness']  # another set of review columns

    # Plot categorical countplots
    """Plot countplots for categorical columns."""
    fig, axes = plt.subplots(len(catg_cols), 3, figsize=(10, 5*len(catg_cols)), constrained_layout=True)
    axes = axes.flatten()

    for ax, col in zip(axes, catg_cols):
        sns.countplot(data=df, x=col, hue=col, ax=ax, palette="viridis", legend=False)
        ax.tick_params(axis='x')

        # Calculate and print percentages for each category
        print(f"\nStatistics for '{col}'")
        col_percentages = df[col].value_counts(normalize=True).mul(100).round(2)
        print(col_percentages)
        print("-" * (25 + len(col)))

    # Hide any unused subplots if the number of plots is not a perfect multiple
    for j in range(len(catg_cols), len(axes)):
        fig.delaxes(axes[j])

    plt.show()
    
    
    # Plot numerical histograms
    """Plot histograms for numerical columns."""
    fig, axes = plt.subplots(len(num_cols), 2, figsize=(10, 5*len(num_cols)), constrained_layout=True)
    axes = axes.flatten()

    for ax, col in zip(axes, num_cols):
        sns.histplot(data=df, x=col, kde=True, ax=ax, color='red')
        
    # Hide any unused subplots if the number of plots is not a perfect multiple
    for j in range(len(num_cols), len(axes)):
        fig.delaxes(axes[j])

    plt.show()

    # Print descriptive statistics for all numerical columns
    print("\nDescriptive Statistics for Numerical Columns")
    print(df[num_cols].describe().round(2))
    print("-" * 50)
    

    # Plot review barplots
    """Plot bar plots for review columns."""
   # Create a single large figure for all service ratings
    # We have 14 review columns, so a 3x5 grid is suitable (3*5=15 plots)
    fig, axes = plt.subplots(3, 5, figsize=(20, 12))
    fig.suptitle('Mean Service Ratings by Class', fontsize=20, y=1.02)
    axes = axes.flatten() # Flatten the 3x5 grid into a 1D array

    # Loop through all review columns and plot them
    for i, col in enumerate(review_cols):
        ax = axes[i] # Select the appropriate subplot
        sns.barplot(data=df, x='class', y=col, hue= 'class', ax=ax, palette="deep", errorbar=None)
        ax.set_title(col, fontsize=11)
        ax.set_xlabel('')
        ax.set_ylabel('Mean Rating')

        # Add mean values on top of bars
        for container in ax.containers:
            ax.bar_label(container, fmt='%.2f', fontsize=10)

    # Hide any unused subplots if the number of plots is not a perfect multiple
    for j in range(len(review_cols), len(axes)):
            fig.delaxes(axes[j])
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
    
    

    # Plot scatter plot for departure and arrival delays
    """Plot a scatter plot to visualize the relationship between departure delay and arrival delay."""
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
    sns.scatterplot(data=df, x='departure delay in minutes', y='arrival delay in minutes',
                    hue='satisfaction', style='satisfaction', ax=ax, palette="magma")

    plt.title("Departure Delay vs Arrival Delay by Satisfaction")
    plt.xlabel("Departure Delay in Minutes")
    plt.ylabel("Arrival Delay in Minutes")
    plt.show()

    # Print correlation and mean delays by satisfaction
    print("\n--- Delay Statistics by Satisfaction ---")
    delay_corr = df[['departure delay in minutes', 'arrival delay in minutes']].corr().iloc[0, 1]
    print(f"Correlation between Departure and Arrival Delay: {delay_corr:.2f}")
    print("\nMean Delays (in minutes):")
    print(df.groupby('satisfaction')[['departure delay in minutes', 'arrival delay in minutes']].mean().round(2))
    print("-" * 50)
    

    # Plot correlation heatmap
    """Plot a correlation heatmap for numerical and review columns."""
    plt.figure(figsize=(12, 8), constrained_layout=True)
    corr = df[num_cols + review_cols].corr()

    sns.heatmap(corr, annot=False, cmap='coolwarm', fmt=".2f", annot_kws={"size": 8}, linewidths=.5, cbar_kws={"shrink": .8})
    plt.title("Correlation Heatmap")
    plt.show()
    
    
    # Plot stacked bar chart for satisfaction by class
    """Plot a stacked bar chart for satisfaction by class."""
    stacked_data = df.groupby('class')['satisfaction'].value_counts(normalize=True).mul(100).round(2).unstack()

    # Create the plot
    ax = stacked_data.plot(kind='bar', stacked=True, figsize=(10, 7), colormap="vlag", edgecolor='black')
    plt.title("Satisfaction by Class (%)", fontsize=16)
    plt.ylabel("Percentage of Passengers")
    plt.xticks(rotation=0)

    # Add percentage labels inside the stacked bars
    for container in ax.containers:
        # The label_type='center' places the text in the middle of the bar segment
        ax.bar_label(container, label_type='center', fmt='%.1f%%', color='white', weight='bold')

    plt.legend(title='Satisfaction', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.85, 1]) # Adjust layout to make space for legend
    plt.show()

    # Print the percentage table
    print("\nSatisfaction Percentage by Class")
    print(stacked_data)
