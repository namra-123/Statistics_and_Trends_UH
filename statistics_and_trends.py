"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    """
    The function `plot_relational_plot` creates a scatter 
    plot comparing the PetalLengthCm and
    PetalWidthCm columns of a DataFrame and saves the plot as a PNG file.
    
    :return: The function `plot_relational_plot(df)` returns a
    scatter plot of the columns 'PetalLengthCm' and 'PetalWidthCm' from the 
    input DataFrame `df`. The plot is saved as'relational_plot.png'.
    """
    
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.scatterplot(x=df['PetalLengthCm'], y=df['PetalWidthCm'], alpha=.8)
    plt.gca().spines[['top', 'right',]].set_visible(False)
    ax.set_title('PetalLengthCm vs PetalWidthCm', fontsize=16)
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    """
    The function `plot_categorical_plot` creates a histogram plot for 
    the 'SepalWidthCm' column in a DataFrame and saves the plot as an
    image file.

    :return: The function `plot_categorical_plot` is returning nothing 
    explicitly. It is generating a histogram plot of the 'SepalWidthCm' column
    from the input DataFrame `df`, customizing the plot
    appearance, saving the plot as 'categorical_plot.png', and then returning.
    """

    fig, ax = plt.subplots(figsize=(7, 7))
    sns.histplot(x=df['SepalWidthCm'], bins=20)
    plt.gca().spines[['top', 'right',]].set_visible(False)
    ax.set_title('SepalWidthCm', fontsize=16)
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    """
    The function `plot_statistical_plot` generates a heatmap of the 
    correlation matrix for numerical columns in a DataFrame and saves it as an
    image file.
    
    :return: The function `plot_statistical_plot(df)` returns a heatmap plot 
    of the correlation matrix of numerical columns in the input DataFrame `df`.
    The plot is saved as an image file named 'statistical_plot.png'.
    """
    
    fig, ax = plt.subplots(figsize=(7, 7))
    df_numeric = df.select_dtypes(include=["number"])
    sns.color_palette("rocket", as_cmap=True)
    sns.heatmap(df_numeric.corr(), annot=True, linewidths=0.2)
    ax.set_title("HeatMap of Iris ", fontsize=16)
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    """
    The function `statistical_analysis` calculates the mean, standard 
    deviation, skewness, and excess kurtosis of a specified column in a 
    DataFrame.
    """
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col].dropna())
    excess_kurtosis = ss.kurtosis(df[col].dropna())
    return mean, stddev, skew, excess_kurtosis

def preprocessing(df):
    """
    The `preprocessing` function drops missing values, selects numerical 
    columns, and displays data summary, sample data, and correlation matrix 
    before returning the processed DataFrame.
    
    :return: The function `preprocessing` returns a DataFrame `df_num` after
    dropping any rows with missing values, selecting only numerical columns, 
    printing the data summary using `describe`, displaying a sample of the 
    data using `head`, and showing the correlation matrix of the numerical
    data using `corr`.
    """
    # You should preprocess your data in this function and
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    df.dropna(inplace=True)
    df_num = df.select_dtypes(include=["number"])
    print("Data Summary:\n", df_num.describe())
    print("\nSample Data:\n", df_num.head(10))
    print("\nCorrelation Matrix:\n", df_num.corr())
    return df_num


def writing(moments, col):
    """
    The function "writing" calculates and displays descriptive statistics for 
    a given attribute, including mean, standard deviation, skewness, and
    excess kurtosis, and determines whether the data is skewed and the type 
    of kurtosis.
    
    :return: The function `writing` is returning nothing explicitly. It is
    simply printing out the calculated statistics and characteristics of the
    data for the specified attribute `col`.
    """
    
    mean, stddev, skew, excess_kurtosis = moments
    print(f'\nFor the attribute {col}:')
    print(f'Mean = {mean:.2f},'
          f'Standard Deviation = {stddev:.2f}, '
          f'Skewness={skew:.2f}, and '
          f'Excess Kurtosis = {excess_kurtosis:.2f}.')
    # Delete the following options as appropriate for your data.
    # Not skewed and mesokurtic can be defined with asymmetries <-2 or >2.
    
    skewness_type = "not skewed" if abs(skew) < 0.5 else "right-skewed" if skew > 0 else "left-skewed"
    kurtosis_type = "mesokurtic" if -0.5 <= excess_kurtosis <= 0.5 else "leptokurtic" if excess_kurtosis > 0.5 else "platykurtic"
    print(f'The data was {skewness_type} and {kurtosis_type}.')
    return

def main():
    """
    The main function reads a CSV file, preprocesses the data, plots relational, statistical, and
    categorical plots, performs statistical analysis on a specific column, and writes the results to a
    file.
    :return: The `main()` function is returning nothing explicitly. It is executing a series of steps
    such as reading a CSV file, preprocessing the data, plotting relational, statistical, and
    categorical plots, performing statistical analysis on a specific column, and writing the results to
    a file. The function does not have a specific return value.
    """
    
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'SepalLengthCm'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    
    return


if __name__ == '__main__':
    main()
