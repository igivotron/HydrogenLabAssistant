import matplotlib.pyplot as plt
import numpy
import numpy as np
class PlotMaker():
    def __init__(self, name, axis, data, legend):
        """
        Permet de plot un graphique selon les paramètres fournis
        :param name: str. Plot's name
        :param axis: str. Plot's axis names
        :param data: list. Data to plot [[[0, 1, 2], [3, 4, 5]], [[0, 1, 2], [3, 4, 5]]]
        :param legend: list. Plot's legend
        """
        self.name = name
        self.axis_name = axis
        self.data = data
        self.legend = legend

    def test(self):
        print(self.legend)

    def number_of_data_error(self, number_of_data):
        if number_of_data > len(self.data):
            raise ValueError("You don't have enough data")
        if number_of_data > len(self.legend):
            raise ValueError("You don't have enough legends")

    def plot_description(self):
        plt.title(self.name)
        plt.xlabel(self.axis_name[0])
        plt.ylabel(self.axis_name[1])

    def plotline(self, number_of_data=1, save = False):
        """
        Plot a basic graphic representation
        :param number_of_data: int. How many data to plot
        :param save: Boolean. If true save the plot as a png
        :return:
        """
        self.number_of_data_error(number_of_data)
        for i in range(number_of_data):
            plt.plot(self.data[i][0], self.data[i][1])
            plt.legend(self.legend[:number_of_data])
        self.plot_description()
        if save:
            plt.savefig(self.name, format='png')
        plt.show()

    def plotdot(self, number_of_data=1, save= False, dot="o", extrapolate = False):
        """
        Plot a basic dots representation
        :param number_of_data: How many data to plot
        :param save: Boolean. If true save the plot as a png
        :param dot: str. Type of dot. if - before dot (-x), draw a line
        """
        self.number_of_data_error(number_of_data)
        for i in range(number_of_data):
            plt.plot(self.data[i][0], self.data[i][1], dot)
            plt.legend(self.legend[:number_of_data])
        self.plot_description()
        if save:
            plt.savefig(self.name, format='png')
        plt.show()

#\TODO Extrapolation



