## 从.txt文件中读取数据
def loadData(flieName):
  inFile = open(idkp1-10, 'r')#以只读方式打开某fileName文件
  #定义两个空list，用来存放文件中的数据
  X = []
  y = []
  for line in inFile:
    trainingSet = line.split(',') #对于每一行，按','把数据分开，这里是分成两部分
    X.append(trainingSet[0]) #第一部分，即文件中的第一列数据逐一添加到list X 中
    y.append(trainingSet[1]) #第二部分，即文件中的第二列数据逐一添加到list y 中
   return (X, y)  # X,y组成一个元组，这样可以通过函数一次性返回
