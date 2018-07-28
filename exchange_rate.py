import pandas as pd
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2 :
    print("[-] All required arguments not given.")

filepath=sys.argv[1]
plotpath=sys.argv[2]

ex_rate_csv=pd.read_csv(filepath)
ex_rate_df=pd.DataFrame(ex_rate_csv).dropna(axis=1)

groupby_loc=ex_rate_df.groupby(ex_rate_df['LOCATION'])
loc_name=[name for name,group in groupby_loc]
print("\n[+] Countries : \n")
for i,c_code in enumerate(loc_name) :
    print(str(i+1)+". " + c_code)

loc=input("[+] Enter the Country code : ")

if loc not in loc_name :
    print("\n[-] Wrong Country code provided ")
    sys.exit(0)
    
get_group=groupby_loc.get_group(loc).reset_index(drop=True)
get_group_value=get_group['Value']
get_group_value_2=get_group_value.iloc[::2]

#visualization

fig,ax=plt.subplots(1,1)
plt.subplots_adjust(top=.95,bottom=.15,right=.98,left=.06)

get_group_value_2.plot(ax=ax,kind='line',xticks=get_group_value_2.index,marker='o',color='r',figsize=(15,10),title=loc)
ax.set_xticklabels(get_group['TIME'][::2],rotation=30)
ax.set_xlabel('TIME',labelpad=10)
ax.set_ylabel('RATE PER USD',labelpad=10)

plt.savefig(plotpath+str('.jpeg'),dpi=450,bbox_inches='tight')
plt.show()



