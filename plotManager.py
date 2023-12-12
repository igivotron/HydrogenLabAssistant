import matplotlib.pyplot as plt
import numpy as np
class PlotMaker():
    def __init__(self, name, axis, data, legend, grid=True, square=True):
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
        if grid:
            plt.grid()

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

    def show(self):
        plt.show()

    def save(self):
        plt.savefig(self.name, format='png')

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

    def plotdot(self, number_of_data=1, save= False, dot="o"):
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

    def plotderivline(self, number_of_data=1, m ="derivative"):
        for i in range(number_of_data):
            lx = len(self.data[i][0])
            ly = len(self.data[i][1])
            A = np.zeros(lx-1)
            for j in range(lx-1):
                A[j] = (self.data[i][0][j+1]-self.data[i][0][j]) / (self.data[i][1][j+1]-self.data[i][1][j])
            plt.plot(self.data[i][0][1:], A)

    def plotderivdot(self, number_of_data=1, m ="derivative", dot="o"):
        for i in range(number_of_data):
            lx = len(self.data[i][0])
            ly = len(self.data[i][1])
            A = np.zeros(lx-1)
            for j in range(lx-1):
                A[j] = (self.data[i][0][j+1]-self.data[i][0][j]) / (self.data[i][1][j+1]-self.data[i][1][j])
            plt.plot(self.data[i][0][1:], A, dot)


