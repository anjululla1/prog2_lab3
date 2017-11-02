#! /user/bin/env python
import re

class GenBank(object):
    def genbankParser(self):
        file = "/Users/anju/Desktop/prog2/hw2_hla.gb.txt"
        my_file = open(file)
        data = my_file.readlines()
        return data

    def Parsedinfo(info, data):
        parsed = []
        string = ''
        for i in data:
            string = i.strip()
            parsed.append(string)

            if string.startswith('ORGANISM'):
                print (string)

            if string.startswith('VERSION'):
                print (string)

            if string.startswith('ACCESSION'):
                print (string)
            
            if string.startswith('exons'):
                continue
            if string.startswith('exon'):
                exon = string
            
            
            if string.startswith('/gene'):
                gene = string

        return parsed
    
    def OriginParsed(info, parsed, string):
        origin = ''
        for k in parsed:
            start = parsed.index('ORIGIN')
            end = parsed.index('//')
        for k in range(start + 1, end):
            for seq in parsed[k]:
                if bool(re.match('[a, g, t, c]', seq)) == True:
                    origin = origin + seq
        origin = origin[1:]
        origin = origin.replace("n", "")
        origin = origin.replace(" ", "")
        origin
        print("ORIGIN")
        print (origin)
        return origin
    def GC(info, origin):
        origin = origin.upper()
        #total = float(len(origin))
        #gcount = origin.count("G")
        #ccount = origin.count("C")
        #gcContent = round((gcount + ccount)*100/total)
        gcContent = ((origin.count("G") + origin.count ("C"))*100/len(origin))
        print ("Percent_GC_content = " "%s"  % gcContent)


obj = GenBank()
file_output = obj.genbankParser()
info_out = obj.Parsedinfo(file_output)
origin = obj.OriginParsed(info_out, file_output)
gc_content= obj.GC(origin)

print ("Name: Anju Lulla")
print ("Email: alulla@uncc.edu")
