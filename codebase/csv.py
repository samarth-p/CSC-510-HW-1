from codebase.cli import the
from codebase.cli import coerce
import os

def csv(fname, func):
    script_path = os.path.abspath(__file__) 
    script_dir = os.path.split(script_path)[0] 
    rel_path = fname
    abs_file_path = os.path.join(script_dir, rel_path)
    sep = the["Seperator"]
    with open(abs_file_path, 'r') as f:
        t = []
        for line in f:
            words = line.rstrip('\n').split(sep)
            words_list = []
            for word in words:
                w = coerce(word)
                words_list.append(w)
            t.append(words_list[0:])
        
        func(t)





