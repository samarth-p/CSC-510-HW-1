import re
import sys
help = """
CSV : summarized csv file

USAGE: python cli.py [OPTIONS]

OPTIONS:
-e --eg start−up example = nothing
-d --dump on test failure, exit with stack dump = false
-f --file file with csv data = ../data/auto93.csv
-h --help show help = false
-n --nums number of nums to keep = 512
-s --seed random number seed = 10019
-S --Seperator feild seperator = ,""" 


def coerce(s):
    def fun(s1):
        if s1 == "true" or s1 == "True":
            return True
        if s1 == "false" or s1 == "False":
            return False
        return s1
    if s.isdigit():
        return int(s)
    elif re.fullmatch(r'[^\n]+', s):
        return fun(s)
    
the = {}

for k, v in re.findall(r'\n[-][\w]+\s+[-][-]([\w]+)+[^\n]+= ([^\s]+)',help):
    the[k] = coerce(v)


def cli(t):
    for slot, v in t.items():
        v = str(v)
        for i in range(1,len(sys.argv)):
            if sys.argv[i] == "-"+slot[0] or sys.argv[i] == "--"+slot:
                if v == "False":
                    v = "true"
                elif v == "True":
                    v = "false"
                else:
                    v= sys.argv[i+1]
        t[slot] = coerce(v)
    if t['help'] == True:
        print("\n"+help+"\n")
        sys.exit()    
    return t      

# the = cli(the)

# print(the)

