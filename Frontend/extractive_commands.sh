#! /bin/bash


touch extractive_chole.txt
cd
source ~/virtual_env/venv_with_python3.7/bin/activate
cd BengaliSummarization/Code/ExtractiveSummarizer
python ExtractiveSummarization1.py
google-chrome /home/risvy/BengaliSummarization/Code/ExtractiveSummarizer/output.txt
