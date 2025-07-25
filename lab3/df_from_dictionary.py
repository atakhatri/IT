import pandas as pd

print("creation of DataFrame using a Dictionary and proper row index")
info = {'name':['ata','gunjan','anubhav'],
        'div':['A','B','C'],
        'roll':[82,40,8]}

df = pd.DataFrame(info,index=[1,2,3])
print(df)

print("\ncreation of DataFrame using list of dictionaries and proper row index")
lst_dc = [{'runs':489,'avg':55,'sr':145},
          {'runs':377,'avg':47},
          {'runs':719,'avg':89,'sr':151}]
df = pd.DataFrame(lst_dc,index=['rohit','dhoni','kohli'])
print(df)
#if a val for a column is missing it shows NaN(i.e. here sr's val in second dictionary


