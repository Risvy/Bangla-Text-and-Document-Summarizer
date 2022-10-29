import wordgraph 
import hClustering as clustering 
import sentTokenizer 
import os 
from bnlm.bnlm import BengaliTokenizer 
from bnlm.bnlm import get_sentence_encoding 
from bnlm.bnlm import get_sentence_similarity 
model_path = 'model'
sp_model = "model/bn_spm.model"

#create folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
def listToString(s):  
    str1 = " "      
    return (str1.join(s)) 

def getSummary(filename): 
    summary = []
    for k in range(n):
        summary_lines = wordgraph.takeinput(filename[k])
        print("summary_lines:",summary_lines)
        if(summary_lines):
            summary.append(summary_lines)
     
    full_summary =[] 
    for x in summary:
        x = x[:-1]
        left_text = x.partition("।")[0]
        left_text = left_text.partition("?")[0]
        left_text = left_text.partition("!")[0]
        full_summary.append(left_text+"।")  
    s = listToString(full_summary)
    return s


# for i in range(1,140):  # for each input.txt file in the folder
for i in range(1,2):
    
    serial_no = str(i)
    # document = open('DataSet/NCTB/Source/'+serial_no+'.txt').read()
    # /home/risvy/Downloads/test.txt
    
    # default input directory is set to downloads folder
    document = open('/home/risvy/Downloads/input.txt').read() 
    #working
    # document = open('DataSet/NCTB/Source/'+'input.txt').read() 
    
    doc = sentTokenizer.sentTokenizing().sentTokenize(document)
    # print('doc',doc)  # commented
    
    # print('\n ekhane jhamela \n') # Solved by modifying hClustering.py file.
    filenamee, n = clustering.startF(doc) 
    # print("\n\nSource:",document)  # commented
    
    summary = getSummary(filenamee)
    print('\n\nSystem Made Summary:',summary)
    
    # save the summary
    createFolder('DataSet/NCTB/MachineGeneratedSummary/')
    fi = open('DataSet/NCTB/MachineGeneratedSummary/'+'output.txt','+w')
    # fi = open('DataSet/NCTB/MachineGeneratedSummary/'+serial_no+'.txt','+w')
    fi.write(summary)


    
    #save the summary in a file named as output.txt
    # createFolder('DataSet/NCTB/Output')
    # file = open('DataSet/NCTB/Output/'+serial_no+'.txt','w')
    # file.write(summary)
    # file.close()

    
    
    # human = open('DataSet/NCTB/Summary/'+serial_no+'.txt').read()
    # print('\n\nHuman Made Summary:',human)
    
    




