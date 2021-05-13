#!/bin/bash
# The path of normal use python environment(From anaconda).
cd /Users/mengxue/Documents/Paper/ChestAuthentication/OtherMaterial/PlayFigure/draw/draw/draw/code
pwd 
/Users/mengxue/opt/anaconda3/envs/MyPy37Env/bin/python Bardirection.py
/Users/mengxue/opt/anaconda3/envs/MyPy37Env/bin/python BarDistance.py
/Users/mengxue/opt/anaconda3/envs/MyPy37Env/bin/python Barnoise.py
/Users/mengxue/opt/anaconda3/envs/MyPy37Env/bin/python Barpose.py
/Users/mengxue/opt/anaconda3/envs/MyPy37Env/bin/python Bardevice.py
/Users/mengxue/opt/anaconda3/envs/MyPy37Env/bin/python CompAverage.py
/Users/mengxue/opt/anaconda3/envs/MyPy37Env/bin/python TrainSizeEer.py

cp ../images/ImpactofHumanPose.eps /Users/mengxue/Documents/Paper/ChestAuthentication/Latex/Ubicomp2021ChestAuth/figures
cp ../images/ImpactofDistance.eps /Users/mengxue/Documents/Paper/ChestAuthentication/Latex/Ubicomp2021ChestAuth/figures
cp ../images/ImpactofDirection.eps /Users/mengxue/Documents/Paper/ChestAuthentication/Latex/Ubicomp2021ChestAuth/figures
cp ../images/ImpactofNoise.eps /Users/mengxue/Documents/Paper/ChestAuthentication/Latex/Ubicomp2021ChestAuth/figures
cp ../images/ImpactofDevice.eps /Users/mengxue/Documents/Paper/ChestAuthentication/Latex/Ubicomp2021ChestAuth/figures
cp ../images/ImpactofMethod.eps /Users/mengxue/Documents/Paper/ChestAuthentication/Latex/Ubicomp2021ChestAuth/figures
cp ../images/TrainSizeEer.eps /Users/mengxue/Documents/Paper/ChestAuthentication/Latex/Ubicomp2021ChestAuth/figures
