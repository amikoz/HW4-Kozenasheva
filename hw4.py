import os, re

def mystem_():
    inp = 'D:\input.txt'
    outp = 'D:\output.txt'
    os.system('D:\mystem.exe ' + inp + ' ' + outp + ' -nid')


def table():
    f = open('D:\output.txt', 'r', encoding = 'utf - 8')
    fr = f.readlines()
    f.close()
    scripttables = open('D:\script.sql', 'a', encoding = 'utf - 8')
    scripttables.write('CREATE TABLE Table1 (id INTEGER PRIMARY KEY, wordform VARCHAR (100), lemma VARCHAR (100));\n')
    i = 0
    for line in fr:
        w = re.search('(.*?)[{?]', line)
        wordform = w.group(1)
        wordform = wordform.lower()
        l = re.search('{(.*?)[=?]', line)
        lemma = l.group(1)
        scripttables.write('INSERT INTO Table1 (id, wordform, lemma) VALUES ("' + str(i) + '", ' + '"' + wordform + '", ' + '"' + lemma +'");\n')
        i +=1
    scripttables.close()
    return scripttables

    
if __name__ == '__main__':
    mystem_()
    table()
