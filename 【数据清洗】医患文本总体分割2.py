import pandas as pd

txtdata_df = pd.read_table(r'C:\Users\Administrator\Desktop\Patient Flow Online\2018.txt',
	names = ['total'],encoding = 'UTF-8',engine='python')

text_patient = []
text_doctor = []
for i in txtdata_df.index:
	text_patient.append([])
	text_doctor.append([])
for j in txtdata_df.index:
	txtdata_df_row = txtdata_df.iloc[j,0].split('|||')
	for k in txtdata_df_row:
		if k[0:2] == 'p:':
			text_patient[j].append(k)
		else:
			text_doctor[j].append(k)

for l1 in range(len(text_patient)):
	text_patient[l1] = '|'.join(text_patient[l1])
for l2 in range(len(text_doctor)):
	text_doctor[l2] = '|'.join(text_doctor[l2])							

txtdata_df['patient'] = text_patient
txtdata_df['doctor'] = text_doctor

txtdata_df.to_excel(r'C:\Users\Administrator\Desktop\2018.xlsx')