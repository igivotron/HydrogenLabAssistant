class FileExtractor:
    def __init__(self, filename):
        """
        File Extractor extrate data from a .txt file
        :param filename: name of the file of interest
        """
        self.filename = filename
        self.data = self.extract_data()

    def extract_data(self):
        """
        Extract the data from the file as a list with lines by lines separation
        :return: List with the file's data
        """
        with open(self.filename, "r") as f:
            return f.read().split("\n")

    def get_title(self):
        """
        Return the plot's title
        :return: plot's title
        """
        return self.data[0]

    def get_axis(self):
        """
        Return the plot's axis names
        :return: plot's axis names
        """
        return self.data[1].split(" ")

    def get_legend(self):
        """
        Get the plot's legend
        :return: str. Plot's legend
        """
        return self.data[2]

    def get_data(self, line = True):
        """
        Get the data without the plot's name and plot's axis names
        :param line: Boolean. If true return list by line, else return by column
        :return: List. File's data without the plot's name and plot's axis names
        """

        if line :
            l = []
            for i in range(len(self.data[3:])):
                l.append(self.data[i+3].split(" "))
        else:
            c1 = []
            c2 = []
            for i in range(len(self.data[3:])):
                c1.append(self.data[i+3].split(" ")[0])
                c2.append(self.data[i + 3].split(" ")[1])
            l = [c1, c2]
        return l

    def __str__(self):
        return "Plot's name : " + self.get_title() + "\n" + "Plot's axis name : " + str(self.get_axis()) + "\n" + "Legend : " + self.get_legend() + "\n" + "Data by lines : " + str(self.get_data())