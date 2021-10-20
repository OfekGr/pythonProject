dic={'rami':70, 'dani':60, 'neta':80,'bibi':69, 'yaniv':90}
name_dic=list(dic.keys())
grade_dic=list(dic.values())
failed=''
for i in range(len(name_dic)):
    if grade_dic[i] < 70:
        failed+=name_dic[i]+' '

print(failed)