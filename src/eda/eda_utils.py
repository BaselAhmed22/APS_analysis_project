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

    review_cols_3 = ['leg room service', 'baggage handling', 'checkin service', 
                    'inflight service', 'cleanliness'] # another set of review columns

    # Plot categorical countplots
    """Plot countplots for categorical columns."""
    fig, axes = plt.subplots(len(catg_cols), 3, figsize=(10, 5*len(catg_cols)), constrained_layout=True)
    axes = axes.flatten()

    for ax, col in zip(axes, catg_cols):
        sns.countplot(data=df, x=col, hue=col, ax=ax, palette="viridis", legend=False)
        ax.tick_params(axis='x')

    for j in range(len(catg_cols), len(axes)):
        fig.delaxes(axes[j])

    plt.show()
    
    
    # Plot numerical histograms
    """Plot histograms for numerical columns."""
    fig, axes = plt.subplots(len(num_cols), 2, figsize=(10, 5*len(num_cols)), constrained_layout=True)
    axes = axes.flatten()

    for ax, col in zip(axes, num_cols):
        sns.histplot(data=df, x=col, kde=True, ax=ax, color='red')
        

    for j in range(len(num_cols), len(axes)):
        fig.delaxes(axes[j])

    plt.show()
    

    # Plot review barplots
    """Plot bar plots for review columns."""
    fig, axes = plt.subplots(1, len(review_cols), figsize=(5*len(review_cols), 10), constrained_layout=True)
    fig.suptitle('Comparison of Service Ratings by Class', fontsize=16)
    axes = axes.flatten()

    for ax, col in zip(axes, review_cols):
        sns.barplot(data=df, x='class', y=col, hue='class', ax=ax, palette="deep", legend=False)
        
        ax.tick_params(axis='x')

    for j in range(len(review_cols), len(axes)):
        fig.delaxes(axes[j])

    plt.show()
    

    # Plot additional review barplots
    """Plot bar plots for additional review columns."""
    fig, axes = plt.subplots(1, len(review_cols_2), figsize=(5*len(review_cols_2), 10), constrained_layout=True)
    fig.suptitle('Comparison of Service Ratings by Class', fontsize=16)
    axes = axes.flatten()

    for ax, col in zip(axes, review_cols_2):
        sns.barplot(data=df, x='class', y=col, hue='class', ax=ax, palette="deep", legend=False)
        
        ax.tick_params(axis='x')

    for j in range(len(review_cols_2), len(axes)):
        fig.delaxes(axes[j])

    plt.show()


    # Plot another set of review barplots
    """Plot bar plots for another set of review columns."""
    fig, axes = plt.subplots(1, len(review_cols_3), figsize=(5*len(review_cols_3), 10), constrained_layout=True)
    fig.suptitle('Comparison of Service Ratings by Class', fontsize=16)
    axes = axes.flatten()

    for ax, col in zip(axes, review_cols_3):
        sns.barplot(data=df, x='class', y=col, hue='class', ax=ax, palette="deep", legend=False)
        
        ax.tick_params(axis='x')

    for j in range(len(review_cols_3), len(axes)):
        fig.delaxes(axes[j])
        
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
    

    # Plot correlation heatmap
    """Plot a correlation heatmap for numerical and review columns."""
    plt.figure(figsize=(12, 8), constrained_layout=True)
    corr = df[num_cols + review_cols + review_cols_2 + review_cols_3].corr()

    sns.heatmap(corr, annot=False, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()
    
    
    # Plot stacked bar chart for satisfaction by class
    """Plot a stacked bar chart for satisfaction by class."""
    stacked_data =df.groupby(['class', 'satisfaction']).size().unstack()
    stacked_data.plot(kind='bar', stacked=True, figsize=(8, 6), colormap="vlag")
    plt.title("Satisfaction by Class")

    plt.tight_layout()
    plt.show()
    
    print("Visualization completed successfully!")
