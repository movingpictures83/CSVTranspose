import sys
import numpy
import random


class CSVTransposePlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line.split(','))

      self.m = len(lines)
      self.samples = []
      self.rows = self.firstline.split(',')
      self.rows.remove(self.rows[0]) # Buffer entry
      self.n = len(self.rows)
      for i in range(0, self.n):
         self.rows[i] = '\"' + self.rows[i].strip() + '\"'
      
      self.cols = []
      for line in lines:
         self.cols.append(line[0])

      self.ADJ = []
      i = 0
      # This time, n X m
      for i in range(self.n):
            self.ADJ.append([])
            for j in range(self.m):
               self.ADJ[i].append(0)

      
      for i in range(self.m):
         for j in range(1, self.n+1):
            self.ADJ[j-1][i] = lines[i][j]
 
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write("\"\",")
      for i in range(self.m):
         filestuff2.write(self.cols[i])
         if (i == self.m-1):
            filestuff2.write("\n")
         else:
            filestuff2.write(",")

      for i in range(self.n):
         #filestuff2.write(self.bacteria[i]+',')
         filestuff2.write(self.rows[i]+',')
         for j in range(self.m):
            filestuff2.write(str(self.ADJ[i][j]).strip())
            if (j < self.m-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



