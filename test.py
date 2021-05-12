import os
root='.'
filelist=os.listdir(root)
for file in filelist:
    if ("1.200000e-01" in file)|("3.500000e-01" in file):
        path=os.path.join(root,file)
        with open(path) as f:
            text=f.readlines()
            for n in text:
                x = n.replace('\n','')
                s="HeySiri{}.mat".format(x)
                errorpath=os.path.join(root,s)
                if(os.path.exists(errorpath)):
                    print(errorpath)
                    os.remove(errorpath)
