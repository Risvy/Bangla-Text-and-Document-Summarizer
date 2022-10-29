import wordgraph
import hClustering as clustering
import sentTokenizer
import os
from bnlm.bnlm import BengaliTokenizer
from bnlm.bnlm import get_sentence_encoding
from bnlm.bnlm import get_sentence_similarity

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
def listToString(s):  
    str1 = " "      
    return (str1.join(s)) 

def getSummary(filename, n):
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

def summarize(text):
    out_file = 'output'
    doc = sentTokenizer.sentTokenizing().sentTokenize(text)
    #print('doc',doc)
    filenamee, n = clustering.startF(doc)
    #print("\n\nSource:",document)
    
    summary = getSummary(filenamee, n)
    createFolder('Dataset/NCTB/MachineGeneratedSummary/')
    fi = open('Dataset/NCTB/MachineGeneratedSummary/'+out_file+'.txt','+w')
    fi.write(summary)
    return summary

print(summarize('১৯ সালের ৬ অক্টোবর সম্রাট ও তাঁর সহযোগী তৎকালীন যুবলীগ নেতা এনামুল হক ওরফে আরমানকে কুমিল্লা থেকে গ্রেপ্তার করে র‍্যাব। তখন র‍্যাব জানায়, গ্রেপ্তারের সময় সম্রাট ও আরমান মদ্যপ ছিলেন। তাঁদের কাছে বিদেশি মদ ছিল। এ কারণে ভ্রাম্যমাণ আদালত তাঁদের ছয় মাস করে কারাদণ্ড দেন। গ্রেপ্তারের পর সম্রাট ও আরমানকে কুমিল্লা থেকে ঢাকায় আনা হয়। বন্য প্রাণীর চামড়া রাখায় ভ্রাম্যমাণ আদালত সম্রাটকে ছয় মাসের কারাদণ্ড দেন।'))