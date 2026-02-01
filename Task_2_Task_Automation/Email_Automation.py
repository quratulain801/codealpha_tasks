import re
with open("data.txt","r") as file:
    text=file.read()
emails=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",text)
with open("emails.txt","w") as file:
    for i in emails:
       file.write(i+"\n")
print("emails and extracted and saved succesfully")
