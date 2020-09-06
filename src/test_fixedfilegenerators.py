import unittest
import json


from fixedwidthgenerators.src import fixedfilegenerator

JSON= 'test.json'
dict = fixedfilegenerator.readJSON(JSON)



class TestFixedfilegenerator(unittest.TestCase):
    def test_readJSON(self):


        self.assertEqual(dict['ColumnNames'][0],'A',"Shoud be A")
        self.assertEqual(dict['Offsets'][0], '5', "Shoud be 5")
        self.assertEqual(dict['Offsets'][1], '10', "Shoud be 10")
        self.assertEqual(dict['FixedWidthEncoding'], 'windows-1252', "Shoud be windows-1252")
        self.assertEqual(dict['DelimitedEncoding'], 'utf-8', "Shoud be utf-8")

    def test_getfixedcolumnoffsets(self):
        columnwidths=[2,2,2]
        columnheaders=['A','B','C']
        resultstr=fixedfilegenerator.getfixedcolumnoffsets(columnwidths,columnheaders)
        self.assertEqual(resultstr,' A B C')

    def test_generatefixedwidthfile(self):
        columnwidths=dict['Offsets']
        columnheaders=dict['ColumnNames']

        flag=fixedfilegenerator.generatefixedwidthfile(columnwidths, columnheaders,200,encoding=dict['FixedWidthEncoding'])
        self.assertEqual(flag,True,"Should be True")
        fxdlenfile =open('fixed.txt','r')
        self.assertNotEqual(fxdlenfile,None,"fixed.txt file should be created with 100 lines by default")
        self.assertEqual(fxdlenfile.encoding,'cp1252',"Shuold be windows-1252(cp1252)")
        strlen =len(fxdlenfile.readline())
        self.assertEqual(strlen,42,"The length of the string in the file should be 42 including new line character")
        nooflines= len(fxdlenfile.readlines())
        self.assertEqual(nooflines,200,"The number of lines should be 200 excluding header")
        fxdlenfile.close()

    def test_generatecsvfile(self):
        columnwidths = dict['Offsets']
        fxdlenfile=None
        fxdlenfile = open('fixed.txt', 'r')
        self.assertNotEqual(fxdlenfile,None,"Fixed file to be generated before CSV file generation")
        self.assertEqual(fxdlenfile.encoding, 'cp1252', "Shuold be windows-1252(cp1252)")
        fxdlenfile.close()
        flag=fixedfilegenerator.generatecsvfile(columnwidths,encoding=dict['DelimitedEncoding'])
        self.assertEqual(flag,True,"Should be True as the snake.csv file gets generated with a default delimiter")
        csvfile=None
        csvfile=open('snake.csv','r',encoding='utf-8')
        self.assertNotEqual(csvfile,None,"CSV file to be generated with content")
        self.assertEqual(csvfile.encoding, 'utf-8', "Should be utf-8")
        header=csvfile.readline()
        self.assertEqual(header[5],',',"Offset value is 5 and comma is expected after 5th character of the record")
        nooflines=len(csvfile.readlines())
        self.assertEqual(nooflines, 200, "The number of lines should be 200 excluding header")
        csvfile.close()





if(__name__=='__main__'):
    unittest.main()
