import matplotlib.pyplot as plt
import seaborn as sns 


def get_simple_plot(chart_type, *args, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))

    if chart_type=='bar plot':
        title = "title"
        plt.title(title)
        plt.bar(x, y)

    elif chart_type=='line plot':
        title = "title"
        plt.title(title)
        plt.bar(x, y)
    else:
        title = "title"
        plt.title(title)
        sns.countplot('name', data=data)