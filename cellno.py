'''
author: Ntsikelelo Sonjica
module: cellno.py

The program generates a random list of 
South African psuedo Cell Phone numbers using 
the following prefix; '074'. It then
outputs the generated cellphone number
'''

from random import randint; #importing randint from random

class CellNo(object):  #class 
        
        def cell_no(self): #function
                
                prefix = ["074"];  #Only 1 Prefix for now; it can be increased if need be
                suffix = [str(randint(1000000,9999999)) for i in range(len(prefix))]; #For loop enhancement in case len(prefix) increase.
                cellno = [];
                for p in prefix:
                        for s in suffix:
                                cellno.append(p+s);

                return cellno[0]; #always print the first generated cellphone number

if __name__ == '__main__':
        cellnobj = CellNo();
        print(cellnobj.cell_no());
