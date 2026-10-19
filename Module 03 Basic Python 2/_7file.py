# .csv -> comma separated
# .txt -> txt file

# write
with open('massage.txt','w') as file:
    file.write('I love Raicha \n')
# append
with open('massage.txt','a') as file:
    file.write('You are my all')
# read
with open('massage.txt','r') as file:
    text=file.read()
    print(text)