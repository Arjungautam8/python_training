

import re
import json
def readEmailFromfile(fileName):
    s = open(fileName , 'r' , encoding = 'utf-8')
    contents = s.read()
    emailList =  re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", contents)
    return emailList



def processEmails(emailList):
    dictionary = {}
    for email in emailList:
        dictionary = addEmailToOutput(email,dictionary)
    saveDictonaryAsJson(dictionary)
        

def findEmailType(email):
    if re.match("[A-Za-z]+\\.[A-Za-z]+@[A-Za-z0-9.-]+",email):
        return"Human"
    else:
        return"Non- Human"


def creatChildJson(occurance, emailType):
    childJson = {}
    childJson['occurance'] = occurance
    childJson['emailType'] = emailType
    return childJson

def addEmailToOutput(email, dictionary):
    if email in dictionary:
        occurance = dictionary.get(email).get('occurance') + 1
        emailType = dictionary.get(email).get('emailType')
        dictionary[email] = creatChildJson(occurance, emailType)
    else:
        occurance = 1
        emailType = findEmailType(email)
        dictionary[email] = creatChildJson(occurance, emailType)
    return dictionary



def  saveDictonaryAsJson(dictionary):
      out_file = open("result.json", "w") 
      json.dump(dictionary, out_file, indent = 6) 
      out_file.close()
    
def main():
    emailList = readEmailFromfile('websiteData.txt')
    processEmails(emailList)
if __name__ == '__main__':
    main()







