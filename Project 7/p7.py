import csv
import statistics
import matplotlib.pyplot as plt

def load_data(file_name: str, types: dict) -> dict:
    """Loads the data into a dictionary
    parameter: csv file, dictionary
    returns: the dictionary with data
    """
    with open(file_name, "r") as in_file:
        csv_reader = csv.reader(in_file)
        titles = next(csv_reader) # read and skip column names
        data = {}
        for row in csv_reader:
            index = 0
            for col_name, col_type in types.items():
                if data.get((col_name, col_type)) == None:
                    data[(col_name, col_type)] = []
                else: 
                    data[(col_name, col_type)].append(col_type(row[index]))
                index += 1
    return data

def summarize(data: dict):
    """Calculates and prints a summary of all the data
    parameter: dictionary of data
    returns: printed summary of data
    """
    for key in data:
        if type(key) == int or float:
            summary_num = 'Statistics for {key}: \n min: {min:.1f} \n max: {max:.1f} \n mean: {mean:.1f} \n stdev: {stdev:.1f} \n mode: {mode:.1f}'
        else:
            summary_str = 'Statistics for {key}: \n Number of unique values: {value:.1f} \n Most common value: {common:.1f}'
             

def pearson_corr(x: list, y: list) -> float:
    """Calculates and prints the Pearson correlation coefficient
    parameters: x variable: list, y variable: list
    returns: Pearson corrlation coefficient: float

    > pearson_corr([1, 2, 3], [2, 3, 5])
    0.98

    > pearson_corr([3.5, 6.7, 2.3], [1.7, 6.9, 3.4])
    0.83
    """
    if len(x) != len(y):
        print('Length of x must equal length of y')
    
    x_bar = statistics.mean(x)
    y_bar = statistics.mean(y)
    x_std = statistics.stdev(x)
    y_std = statistics.stdev(y)
    num = 0.0
    for i in range(len(x)):
        num = num + (x[i] - x_bar) * (y[i] - y_bar)
    corr = num / ((len(x) - 1) * x_std * y_std)
    return round(corr, 2)

def survivor_vis(data: dict, col1: tuple, col2: tuple) -> plt.Figure:
    """Creates a scatterplot to visualize the relationship between selected data
    parameters: our dictionary of data, col1 and col2 which represent the specific sets of data we are interested in
    return: a scatterplot
    """
    fig = plt.figure()
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.scatter(data[col1], data[col2], marker = 'o', c = 'red', label = 'Survived')
    plt.legend()
    plt.title('Survivial of Titanic Passengers')
    plt.savefig(f'scatter-{col1[0]}-{col2[0]}.png')
    plt.show(block = False)

# ------ You shouldn't have to modify main --------
def main():
    """Main program driver for Project 7."""

    # 7.1 Load the dataset
    TITANIC_TYPES = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('Titanic-clean.csv', TITANIC_TYPES)

    # 7.2 Print informative summaries
    print("\nPart 7.2")
    summarize(data)

    print("\nPart 7.3")
    # 7.3 Compute correlations between age and survival
    corr_age_survived = pearson_corr(data[('Age', float)],
                                     data[('Survived', int)])
    print(f'Correlation between age and survival is {corr_age_survived:3.2f}')

    # 7.3 Correlation between fare and survival
    corr_fare_survived = pearson_corr(data[('Fare', float)],
                                      data[('Survived', int)])
    print(f'Correlation between fare and survival is {corr_fare_survived:3.2f}')

    # 7.3 Correlation between family size and survival
    corr_fare_survived = pearson_corr(data[('FamilySize', int)],
                                      data[('Survived', int)])
    print(f'Correlation between family size and survival is'
          f' {corr_fare_survived:3.2f}')

    # 7.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    fig = survivor_vis(data, ('Age', float), ('Parch', int))


if __name__ == "__main__":
    main()
