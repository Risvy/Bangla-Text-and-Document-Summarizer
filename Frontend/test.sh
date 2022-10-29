#! /bin/bash

# python /home/risvy/pyscript/testscript/hello.py
touch yes_chole.txt
cd
source ~/virtual_env/venv_with_python3.7/bin/activate
cd BengaliSummarization/Code/AbstractiveSummarizer
touch yes_chole2.txt
chmod +x abstractiveSummarizer.py
python /home/risvy/BengaliSummarization/Code/AbstractiveSummarizer/abstractiveSummarizer.py
google-chrome /home/risvy/BengaliSummarization/Code/AbstractiveSummarizer/DataSet/NCTB/MachineGeneratedSummary/output.txt




