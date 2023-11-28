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

    def get_data(self, line = True):
        """
        Get the data without the plot's name and plot's axis names
        :param line: Boolean. If true return list by lines, else return by columns
        :return: List. File's data without the plot's name and plot's axis names
        """

        if line :
            l = []
            for i in range(len(self.data[2:])):
                l.append(self.data[i+2].split(" "))
        else:
            c1 = []
            c2 = []
            for i in range(len(self.data[2:])):
                c1.append(self.data[i+2].split(" ")[0])
                c2.append(self.data[i + 2].split(" ")[1])
            l = [c1, c2]
        return l

    def __str__(self):
        return "Plot's name : " + self.get_title() + "\n" + "Plot's axis name : " + str(self.get_axis()) + "\n" + "Data by lines : " + str(self.get_data())