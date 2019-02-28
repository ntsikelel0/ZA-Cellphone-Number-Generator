'''
author: Maze
module: cellno.py

Here I am making use of OOP.The program
generates a random list of South African
Cell Phone numbers using the following
prefixes '073', '074' and '079'. It then
outputs the first generated cellphone numb
'''

from random import randint;

class CellNo(object):
        def cell_no(self):
                prefix = ["073","074","079"];
                suffix = [str(randint(1000000,9999999))];
                cell = [];
                for p in prefix:
                        for s in suffix:
                                cell.append(p+s);

                print(cell[0]);

cellnobj = CellNo();
cellnobj.cell_no();
