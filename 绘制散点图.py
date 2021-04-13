#导入pylab库
import pylab

## 绘制该文件中的数据
## 需要引入pylab库，里面用到的函数和MATLAB里的非常类似
def plotData(X, y):
  length = len(y)
  pylab.figure(1)
  pylab.plot(X, y, 'rx')
  pylab.xlabel('Population of City in 10,000s')
  pylab.ylabel('Profit in $10,000s')
  pylab.show()#让绘制的图像在屏幕上显示出来


#调用函数
(X,y) = loadData('ex1data1.txt')
plotData(X,y)
