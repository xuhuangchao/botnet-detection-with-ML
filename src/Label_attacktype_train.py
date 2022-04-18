import pandas as pd
import numpy as np
data = pd.read_csv('../dataset/ISCX_Botnet-Training.pcap_Flow.csv', low_memory=False,encoding="gbk")
# data = data[0:50000]
print(data.shape)

#replace inf with nan and then drop the rows with nans
print("Null Values in data set: " + str(data.isnull().sum().sum()) )
data = data.replace([np.inf, -np.inf], np.nan).dropna(how="any").reset_index(drop=True)
print("Null Values in data set: " + str(data.isnull().sum().sum()) )

data= data.drop(['Src IP', 'Src Port', 'Dst IP', 'Dst Port', 'Timestamp', 'Protocol'], axis=1)
print(data.shape)

df = data[['Flow ID', 'Label']]
IRC_1 = df['Flow ID'].str.contains('192.168.2.112-131.202.243.84')
IRC_2 = df['Flow ID'].str.contains('192.168.5.122-198.164.30.2')
IRC_3 = df['Flow ID'].str.contains('192.168.2.110-192.168.5.122')
IRC_4 = df['Flow ID'].str.contains('192.168.4.118-192.168.5.122')
IRC_5 = df['Flow ID'].str.contains('192.168.2.113-192.168.5.122')
IRC_6 = df['Flow ID'].str.contains('192.168.1.103-192.168.5.122')
IRC_7 = df['Flow ID'].str.contains('192.168.4.120-192.168.5.122')
IRC_8 = df['Flow ID'].str.contains('192.168.2.112-192.168.2.110')
IRC_9 = df['Flow ID'].str.contains('192.168.2.112-192.168.4.120')
IRC_10 = df['Flow ID'].str.contains('192.168.2.112-192.168.1.103')
IRC_11 = df['Flow ID'].str.contains('192.168.2.112-192.168.2.113')
IRC_12 = df['Flow ID'].str.contains('192.168.2.112-192.168.4.118')
IRC_13 = df['Flow ID'].str.contains('192.168.2.112-192.168.2.109')
IRC_14 = df['Flow ID'].str.contains('192.168.2.112-192.168.2.105')
IRC_15 = df['Flow ID'].str.contains('192.168.1.105-192.168.5.122')


Neris = df['Flow ID'].str.contains('147.32.84.180')
RBot  = df['Flow ID'].str.contains('147.32.84.170')
Menti = df['Flow ID'].str.contains('147.32.84.150')
Sogou = df['Flow ID'].str.contains('147.32.84.140')
Murlo = df['Flow ID'].str.contains('147.32.84.130')
Virut = df['Flow ID'].str.contains('147.32.84.160')
IRCbot_and_black_hole_1 = df['Flow ID'].str.contains('10.0.2.15')
Black_hole_2 = df['Flow ID'].str.contains('192.168.106.141')
Black_hole_3 = df['Flow ID'].str.contains('192.168.106.131')
TBot_1 = df['Flow ID'].str.contains('172.16.253.130')
TBot_2 = df['Flow ID'].str.contains('172.16.253.131')
TBot_3 = df['Flow ID'].str.contains('172.16.253.129')
TBot_4 = df['Flow ID'].str.contains('172.16.253.240')
Weasel_master = df['Flow ID'].str.contains('74.78.117.238')
Weasel_bot = df['Flow ID'].str.contains('158.65.110.24')
Zeus_1  = df['Flow ID'].str.contains('192.168.3.35')
Zeus_2 = df['Flow ID'].str.contains('192.168.3.25')
Zeus_3 = df['Flow ID'].str.contains('192.168.3.65')
bin_Zeus = df['Flow ID'].str.contains('172.29.0.116')
Osx_trojan = df['Flow ID'].str.contains('172.29.0.109')
zero_access_1 = df['Flow ID'].str.contains('172.16.253.132')
zero_access_2 = df['Flow ID'].str.contains('192.168.248.165')
Smoke_bot = df['Flow ID'].str.contains('10.37.130.4')

indx_IRC_1 = [i for i, x in enumerate(IRC_1) if x]
indx_IRC_2 = [i for i, x in enumerate(IRC_2) if x]
indx_IRC_3 = [i for i, x in enumerate(IRC_3) if x]
indx_IRC_4 = [i for i, x in enumerate(IRC_4) if x]
indx_IRC_5 = [i for i, x in enumerate(IRC_5) if x]
indx_IRC_6 = [i for i, x in enumerate(IRC_6) if x]
indx_IRC_7 = [i for i, x in enumerate(IRC_7) if x]
indx_IRC_8 = [i for i, x in enumerate(IRC_8) if x]
indx_IRC_9 = [i for i, x in enumerate(IRC_9) if x]
indx_IRC_10 = [i for i, x in enumerate(IRC_10) if x]
indx_IRC_11 = [i for i, x in enumerate(IRC_11) if x]
indx_IRC_12 = [i for i, x in enumerate(IRC_12) if x]
indx_IRC_13 = [i for i, x in enumerate(IRC_13) if x]
indx_IRC_14 = [i for i, x in enumerate(IRC_14) if x]
indx_IRC_15 = [i for i, x in enumerate(IRC_15) if x]


indx_Neris = [i for i, x in enumerate(Neris) if x]
indx_RBot  = [i for i, x in enumerate(RBot) if x]
indx_Menti = [i for i, x in enumerate(Menti) if x]
indx_Sogou = [i for i, x in enumerate(Sogou) if x]
indx_Murlo = [i for i, x in enumerate(Murlo) if x]
indx_Virut = [i for i, x in enumerate(Virut) if x]
indx_IRCbot_and_black_hole_1 = [i for i, x in enumerate(IRCbot_and_black_hole_1) if x]
indx_Black_hole_2 = [i for i, x in enumerate(Black_hole_2) if x]
indx_Black_hole_3 = [i for i, x in enumerate(Black_hole_3) if x]
indx_TBot_1 = [i for i, x in enumerate(TBot_1) if x]
indx_TBot_2 = [i for i, x in enumerate(TBot_2) if x]
indx_TBot_3 = [i for i, x in enumerate(TBot_3) if x]
indx_TBot_4 = [i for i, x in enumerate(TBot_4) if x]
indx_Weasel_master = [i for i, x in enumerate(Weasel_master) if x]
indx_Weasel_bot = [i for i, x in enumerate(Weasel_bot) if x]
indx_Zeus_1  = [i for i, x in enumerate(Zeus_1) if x]
indx_Zeus_2 = [i for i, x in enumerate(Zeus_2) if x]
indx_Zeus_3 = [i for i, x in enumerate(Zeus_3) if x]
indx_bin_Zeus = [i for i, x in enumerate(bin_Zeus) if x]
indx_Osx_trojan = [i for i, x in enumerate(Osx_trojan) if x]
indx_zero_access_1 = [i for i, x in enumerate(zero_access_1) if x]
indx_zero_access_2 = [i for i, x in enumerate(zero_access_2) if x]
indx_Smoke_bot = [i for i, x in enumerate(Smoke_bot) if x]
indx_zero_access_1 = [i for i, x in enumerate(zero_access_1) if x]
indx_zero_access_2 = [i for i, x in enumerate(zero_access_2) if x]
indx_Smoke_bot = [i for i, x in enumerate(Smoke_bot) if x]


total_instances = df.shape[0]
print("Total Instances:" + str(total_instances))

print("bin_IRC_1_Instances:" + str(len(indx_IRC_1))+ " ---> "+ str(round(len(indx_IRC_1)/total_instances*100, 4)) + " %")
print("bin_IRC_2_Instances:" + str(len(indx_IRC_2))+ " ---> "+ str(round(len(indx_IRC_2)/total_instances*100, 4)) + " %")
print("bin_IRC_3_Instances:" + str(len(indx_IRC_3))+ " ---> "+ str(round(len(indx_IRC_3)/total_instances*100, 4)) + " %")
print("bin_IRC_4_Instances:" + str(len(indx_IRC_4))+ " ---> "+ str(round(len(indx_IRC_4)/total_instances*100, 4)) + " %")
print("bin_IRC_5_Instances:" + str(len(indx_IRC_5))+ " ---> "+ str(round(len(indx_IRC_5)/total_instances*100, 4)) + " %")
print("bin_IRC_6_Instances:" + str(len(indx_IRC_6))+ " ---> "+ str(round(len(indx_IRC_6)/total_instances*100, 4)) + " %")
print("bin_IRC_7_Instances:" + str(len(indx_IRC_7))+ " ---> "+ str(round(len(indx_IRC_7)/total_instances*100, 4)) + " %")
print("bin_IRC_8_Instances:" + str(len(indx_IRC_8))+ " ---> "+ str(round(len(indx_IRC_8)/total_instances*100, 4)) + " %")
print("bin_IRC_9_Instances:" + str(len(indx_IRC_9))+ " ---> "+ str(round(len(indx_IRC_9)/total_instances*100, 4)) + " %")
print("bin_IRC_10_Instances:" + str(len(indx_IRC_10))+ " ---> "+ str(round(len(indx_IRC_10)/total_instances*100, 4)) + " %")
print("bin_IRC_11_Instances:" + str(len(indx_IRC_11))+ " ---> "+ str(round(len(indx_IRC_11)/total_instances*100, 4)) + " %")
print("bin_IRC_12_Instances:" + str(len(indx_IRC_12))+ " ---> "+ str(round(len(indx_IRC_12)/total_instances*100, 4)) + " %")
print("bin_IRC_13_Instances:" + str(len(indx_IRC_13))+ " ---> "+ str(round(len(indx_IRC_13)/total_instances*100, 4)) + " %")
print("bin_IRC_14_Instances:" + str(len(indx_IRC_14))+ " ---> "+ str(round(len(indx_IRC_14)/total_instances*100, 4)) + " %")
print("bin_IRC_15_Instances:" + str(len(indx_IRC_15))+ " ---> "+ str(round(len(indx_IRC_15)/total_instances*100, 4)) + " %")



print("Neris_Instances:" + str(len(indx_Neris)) + " ---> "+ str(round(len(indx_Neris)/total_instances*100, 4)) + " %")
print("RBot_Instances:" + str(len(indx_RBot)) + " ---> "+ str(round(len(indx_RBot)/total_instances*100, 4)) + " %")
print("Menti_Instances:" + str(len(indx_Menti)) + " ---> "+ str(round(len(indx_Menti)/total_instances*100, 4)) + " %")
print("Sogou_Instances:" + str(len(indx_Sogou)) + " ---> "+ str(round(len(indx_Sogou)/total_instances*100, 4)) + " %")
print("Murlo_Instances:" + str(len(indx_Murlo)) + " ---> "+ str(round(len(indx_Murlo)/total_instances*100, 4)) + " %")
print("Virut_Instances:" + str(len(indx_Virut)) + " ---> "+ str(round(len(indx_Virut)/total_instances*100, 4)) + " %")
print("IRCbot_and_black_hole_1_Instances:" + str(len(indx_IRCbot_and_black_hole_1)) + " ---> "+ str(round(len(indx_IRCbot_and_black_hole_1)/total_instances*100, 4)) + " %")
print("Black_hole_2_Instances:" + str(len(indx_Black_hole_2)) + " ---> "+ str(round(len(indx_Black_hole_2)/total_instances*100, 4)) + " %")
print("Black_hole_3_Instances:" + str(len(indx_Black_hole_3)) + " ---> "+ str(round(len(indx_Black_hole_3)/total_instances*100, 4)) + " %")
print("TBot_1_Instances:" + str(len(indx_TBot_1)) + " ---> "+ str(round(len(indx_TBot_1)/total_instances*100, 4)) + " %")
print("TBot_2_Instances:" + str(len(indx_TBot_2)) + " ---> "+ str(round(len(indx_TBot_2)/total_instances*100, 4)) + " %")
print("TBot_3_Instances:" + str(len(indx_TBot_3)) + " ---> "+ str(round(len(indx_TBot_3)/total_instances*100, 4)) + " %")
print("TBot_4_Instances:" + str(len(indx_TBot_4)) + " ---> "+ str(round(len(indx_TBot_4)/total_instances*100, 4)) + " %")
print("Weasel_master_Instances:" + str(len(indx_Weasel_master)) + " ---> "+ str(round(len(indx_Weasel_master)/total_instances*100, 4)) + " %")
print("Weasel_bot_Instances:" + str(len(indx_Weasel_bot)) + " ---> "+ str(round(len(indx_Weasel_bot)/total_instances*100, 4)) + " %")
print("Zeus_1_Instances:" + str(len(indx_Zeus_1)) + " ---> "+ str(round(len(indx_Zeus_1)/total_instances*100, 4)) + " %")
print("Zeus_2_Instances:" + str(len(indx_Zeus_2)) + " ---> "+ str(round(round(len(indx_Zeus_2)/total_instances*100, 4), 2)) + " %")
print("Zeus_3_Instances:" + str(len(indx_Zeus_3)) + " ---> "+ str(round(len(indx_Zeus_3)/total_instances*100, 4)) + " %")
print("bin_Zeus_Instances:" + str(len(indx_Zeus_3)) + " ---> "+ str(round(len(indx_Zeus_3)/total_instances*100, 4)) + " %")
print("Osx_trojan_Instances:" + str(len(indx_Osx_trojan)) + " ---> "+ str(round(len(indx_Osx_trojan)/total_instances*100, 4)) + " %")
print("zero_access_1_Instances:" + str(len(indx_zero_access_1)) + " ---> "+ str(round(len(indx_zero_access_1)/total_instances*100, 4)) + " %")
print("zero_access_2_Instances:" + str(len(indx_zero_access_2)) + " ---> "+ str(round(len(indx_zero_access_2)/total_instances*100, 4)) + " %")
print("Smoke_bot_Instances:" + str(len(indx_Smoke_bot)) + " ---> "+ str(round(len(indx_Smoke_bot)/total_instances*100, 4)) + " %")

data.loc[:, 'Label'] = 0.0

# IRC-1
data.loc[indx_IRC_2, 'Label'] = 1
data.loc[indx_IRC_3, 'Label'] = 1
data.loc[indx_IRC_4, 'Label'] = 1
data.loc[indx_IRC_5, 'Label'] = 1
data.loc[indx_IRC_6, 'Label'] = 1
data.loc[indx_IRC_7, 'Label'] = 1
data.loc[indx_IRC_11, 'Label'] = 1
data.loc[indx_IRC_15, 'Label'] = 1

# Neris-2
data.loc[indx_Neris, 'Label'] = 2

# Rbot-3
data.loc[indx_RBot, 'Label'] = 3

# Virut-4
data.loc[indx_Virut, 'Label'] = 4

# Zeus-5
data.loc[indx_Zeus_2, 'Label'] = 5

data.to_csv('../dataset/training_label_attacktype.csv',encoding='utf-8')