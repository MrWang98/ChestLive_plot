import os
with open("data/size_result/eer_size_10.txt") as f:
    text = f.read()
    text = text.replace("<tf.Tensor: shape=(), dtype=float32, numpy=", '')
    text = text.replace(">",'')
    text = eval(text)

person={}

result = {}
for size in range(1,21):
    true_dict = {}
    score_dict = {}
    filepath="../data/size_result/eer_size_{}.txt".format(size)
    with open(filepath,'r') as f:
        text = f.read()
        text = text.replace("<tf.Tensor: shape=(), dtype=float32, numpy=",'')
        text = text.replace(">",'')
    text = eval(text)
    for key in text:

        t_count=0
        count=0
        for r_p in text[key]:
            if r_p[0]==0 and r_p[1]<0.5:
                t_count+=1
            elif r_p[0]==1 and r_p[1]>0.5:
                t_count+=1
            count+=1
        if key not in person:
            person[key]=[]
        person[key].append(t_count/count)
print()
