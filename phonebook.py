
<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono');
html{
   display:flex;
   justify-content:center;
   align-items: center;
   width: 100%;
   height: 100%;
   background-image: url('https://source.unsplash.com/collection/327760/1600x900');
   background-size:cover;
}

body{
   width:55%;
   height:60vh;
   border:1px solid lightgray;
   background-color:white;
   border-radius:8px;
   font-family: 'Roboto Mono', monospace;
   box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
   border-top:32px solid #eee;
   overflow-y:scroll;
}

body > div{
  height: calc(100% - 40px);
  overflow-y:auto;
  padding: 20px;
  font-size: 24px;
  white-space: pre;
}

pre{
  margin:inherit;
  font-family: inherit;
}
</style>

#!/usr/bin/python3
print("Content-type: text/html \n")

import magicwand

phonebook_file = open("phone-data.txt")

contacts = {}

for line in phonebook_file:
    newline = line.rstrip()
    c_list = newline.split(",")
    contacts[c_list[0]] = c_list[1]
    
phonebook_file.close()

print("There are a total of", len(contacts.keys()), "contacts in file")
print()

def dirByAlphabet(alphabet):
    a_count = 0 
    for contact in sorted(contacts.items()):
        name, number = contact 
        if name.startswith(alphabet):
            a_count += 1 
            print(a_count, name, ":", number)
    print()
    print("There are", a_count, "contacts starting with", alphabet)
    
def searchByName(query):
    for contact in sorted(contacts.items()):
        name, number = contact 
        if query in name:
            print(name, number)

dirByAlphabet("A")
