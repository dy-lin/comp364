from collections import namedtuple
class MyCSV:
    def __init__(self, delimiter=",", header=True):
        self.delimiter = delimiter
        self.header = header
    def parse(self,path):
        data = MyData()
        lines = []
        #encoding since not all characters are utf-8
        with open(path,"r",encoding="ISO-8859-1") as f:
            lines = list(f)
        for i in range(len(lines)):
            lines[i] = lines[i].strip('\n')
        for index, line in enumerate(lines):
            lines[index] = line.split(self.delimiter)
        #now this is a 2D list
        #lines[row#][column#]
        
        #strips each entry of double quotes that are sometimes present in csv fields
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                lines[i][j] = lines[i][j].strip('"')

        if self.header == True:
            if lines[0][0] == '':
                lines[0][0] = "number"
            data.columns = lines[0]
            for index,column in enumerate(data.columns):
                vals = []
                #if header == True, means first line is a header, does not count as data
                for i in range(1,len(lines)):
                    vals.append(lines[i][index])
                setattr(data,column,vals)
        else:
            for i in range(len(lines[0])):
                data.columns.append("col_" + str(i))
            for index,column in enumerate(data.columns):
                vals = []
                #if header == False, means first line is already data
                for i in range(len(lines)):
                    vals.append(lines[i][index])
                setattr(data,column,vals)
        return data
class MyData:
    #has attributes: list of column names, and attribute to each column that contains its values.
    def iterrows(self):
        iterable = []
        allrows = []
        Row = namedtuple("Row", self.columns)
        for column in self.columns:
            rows = getattr(self, column)
            allrows.append(rows)
        zipped = zip(*allrows)
        for tuple in zipped:
            row = Row(*tuple)
            iterable.append(row)
        return iter(iterable)



