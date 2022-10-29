# Bangla Text and Document Summarizer

## Reference
This project implements the works of the following paper: [Unsupervised Abstractive Summarization of Bengali Text Documents](https://www.aclweb.org/anthology/2021.eacl-main.224/) accepted at [EACL 2021](https://2021.eacl.org/). If you use any of the resources or it's relevant to your work, please cite the paper of the original authors. 
### Citation
```
@inproceedings{chowdhury2021eacl,
    title = "Unsupervised Abstractive Summarization of Bengali Text Documents",
    author  = {Radia Rayan Chowdhury and Mir Tafseer Nayeem and Tahsin Tasnim Mim and Md. Saifur Rahman Chowdhury and Taufiqul Jannat},
    booktitle = "Proceedings of the 16th Conference of the {E}uropean Chapter of the Association for Computational Linguistics (EACL)",
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics"
}
```
## Steps to Run the Project
### Step 1: Clone the Project
```
cd
git clone https://github.com/Risvy/Bangla-Text-and-Document-Summarizer.git
```
Go to *Bangla-Text-and-Document-Summarizer* folder. Download *export.pkl* from this [link](https://drive.google.com/drive/folders/11ynzy-mX2zF4JsYruwDftMvXGCY2dTzi?usp=sharing) or [link](https://drive.google.com/file/d/13QLI02RBfxPDMPNEzTzqxrhGdBy-Xs0B/view?usp=share_link) and place it in the `Code/AbstractiveSummarizer/model/` directory.

### Step 2: Create Python Virtual Environment
We need strictly specific version of softwares. So, the preferrable way is to create a virtual environment and run the project there. 

#### Python Virtual Environment Setup:
1. Run the following commands: 
```
pip install pydot
pip install pydotplus

pip install pyqt5
sudo apt install libxcb-xinerama0 
sudo apt-get install graphviz graphviz-dev
pip install pygraphviz
```

2. Install python 3.7 and it’s virtual environment packages.
```
sudo apt-get install python3.7-dev python3.7-venv
```
3. Find out where your python 3.7 is located by this command;
```
which python3.7 
# Should be something like /usr/bin/python3.7
```
4. Go to `Bangla-Text-and-Document-Summarizer/virtual_env` directory. Run these commands:
```
usr/bin/python3.7 -m venv ~/virtual_env/venv_with_python3.7
source ~/virtual_env/venv_with_python3.7/bin/activate
python --version 
```
The python version should be **3.7**, which indicates the above steps are successful. 

### Step 3: 
We used Ubuntu 20.04 and Google Chrome, which are recommended to run this project. Now:
1. Install php in Ubuntu. (Command is not provided, browse google)
2. Go to VS Code > extension, install 2 extensions: **PHP Sever** by brapifra, **PHP Intelephense** by Ben.
3. Go to `Bangla-Text-and-Document-Summarizer` folder and open `Frontend` folder with VS Code.
4. In VS Code, open **index.html** file, and right-click > **PHP Server: Serve Project**.
5. This should open a localhost server in your browser.

#### Step 4: Run and Summarize
Insert the text you want to summarize. Click *SAVE* and the file will be downloaded in your system (default path: /Downloads/input.txt) Then click either *Abstractive* or *Extractive* summarization. The output will be automatically shown in a chrome new tab. Keep in mind that the time it will take depends on the capacity of the host machine. Thus the longer the text, the more time it will take to give results (How about start with a paragraph with 5-6 lines?). Extractive summarization gives faster result than abstractive Summarization.


## Troubleshoot
1. You may need to install specific version of some softwares. Check `Code/AbstractiveSummarizer/Reference_Colab_Implementation.ipynb` for what is installed after which.
2. Some paths could be hard-coded for simplicity. You may need to change some paths to function properly.
3. Start summarizing with documents that have shorter length, as summarization depends on the capacity of your machine.


