from fileManager import FileExtractor
from plotManager import PlotMaker

f = FileExtractor("test.txt")
p = PlotMaker("hello world", ["x", "t"], [[[0,1,2,3,4],[5,6,7,8,9]],[[5,6,7,8,9],[0,1,2,3,4]]], ["Alice", "Bob"])
p.plotdot(2)