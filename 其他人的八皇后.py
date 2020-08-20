#-*- coding:utf-8 -*-
import random
#冲突检查，在定义state时，采用state来标志每个皇后的位置，其中索引用来表示横坐标，基对应的值表示纵坐标，例如： state[0]=3，表示该皇后位于第1行的第4列上
def conflict(state, nextX):
    nextY = len(state)
#  print(nextY),
    for i in range(nextY):
    #如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，则说明有冲突，需要重新摆放
      if abs(state[i]-nextX) in (0, nextY-i):
#纵坐标减去下一个皇后的横坐标的绝对值 处于 0到下一皇后纵坐标减i则冲突
        return True
    return False
#采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
def queens(num, state=()):
  #num = 8
#  print("%d "%len(state)),
    for pos in range(num):
      if not conflict(state, pos): #如果没有冲突
      #产生当前皇后的位置信息
        if len(state) == num-1:
          yield (pos, ) #生成元组
      #否则，把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
        else:
          for result in queens(num, state+(pos,)):
            yield (pos, ) + result
          #result这个变量代表的是quees返回的元组
#若是最后一行 对于 pos in range(num)调用conflict(state, num) ,
#如果没有冲突,生成元组
#若不是最后一行 对于pos in range(num)调用conflict(state, pos),
#如果没有冲突,state更新,递归调用queens(num, state) state将更新
#为了直观表现棋盘，用X表示每个皇后的位置
def prettyprint(solution):
    def line(pos, length=len(solution)):
      return '. ' * (pos) + 'X ' + '. '*(length-pos-1)
    for pos in solution:
      print(line(pos))
      
if __name__ == "__main__":#来判断是否是在直接运行该.py文件
    prettyprint(random.choice(list(queens(8))))
