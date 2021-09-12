import pandas as pd
import os

mypath = "census\Work\Districts\\"

def economic_activity():

    with open(mypath + "Binder1.txt") as file_in:    

        index = 1
        #df = pd.DataFrame()
        data = []
        district = ''
        for line in file_in:
            #print (line)
            index = index + 1
            
            if 'DISTRICT' in line.strip():
                district = line.strip()
                print (district)
             
            if 'RURAL' in line.strip() and len(line.strip().strip('-').strip()) == 5:
                ruralComplete = False                        
                
                for line in file_in:                         
                    if ruralComplete == True:
                        break
                    if 'FEMALE' in line:
                        for line in file_in:
                            # for literacy
                            if '10 & ABOVE' in line or \
                            '10 -  14'  in line  or '15 -  19' in line or  \
                            '20 - 24'  in line or '25 - 29'  in line  or \
                            '30 - 34' in line  or	'35 - 39' in line  or \
                            '40 - 44'  in line or '45 - 49' in line  or \
                            '50 - 54' in line  or '55 - 59' in line  or \
                            '60 - 64' in line  or '65 - 69' in line  or \
                            '70 - 74'  in line or '75 & ABOVE' in line :
                                data.append(data_compile(District = district, Tehsil="", line=line, Gender='Female', Locality='Rural'))
                            if '75 & ABOVE' in line:
                                break
                    if 'MALE' in line:
                        for line in file_in:
                            # for literacy
                            if '10 & ABOVE' in line or \
                            '10 -  14'  in line  or '15 -  19' in line or  \
                            '20 - 24'  in line or '25 - 29'  in line  or \
                            '30 - 34' in line  or	'35 - 39' in line  or \
                            '40 - 44'  in line or '45 - 49' in line  or \
                            '50 - 54' in line  or '55 - 59' in line  or \
                            '60 - 64' in line  or '65 - 69' in line  or \
                            '70 - 74'  in line or '75 & ABOVE' in line :
                                data.append(data_compile(District = district, Tehsil="", line=line, Gender='Male', Locality='Rural'))
                            if '75 & ABOVE' in line:
                                break
                    
                    if 'TRANSGENDER' in line:
                        for line in file_in:
                            # for literacy
                            if '10 & ABOVE' in line or \
                            '10 -  14'  in line  or '15 -  19' in line or  \
                            '20 - 24'  in line or '25 - 29'  in line  or \
                            '30 - 34' in line  or	'35 - 39' in line  or \
                            '40 - 44'  in line or '45 - 49' in line  or \
                            '50 - 54' in line  or '55 - 59' in line  or \
                            '60 - 64' in line  or '65 - 69' in line  or \
                            '70 - 74'  in line or '75 & ABOVE' in line :
                                data.append(data_compile(District = district, Tehsil="", line=line, Gender='Transgender', Locality='Rural'))
                            if '75 & ABOVE' in line:
                                ruralComplete = True
                                break                                            
            elif 'URBAN'  in line.strip() and len(line.strip()) == 5:
                                    
                urbanComplete = False
                                        
                for line in file_in:   
                                            
                    if urbanComplete == True:
                        break
                    
                    if 'FEMALE' in line:
                        for line in file_in:
                            if '10 & ABOVE' in line or \
                            '10 -  14'  in line  or '15 -  19' in line or  \
                            '20 - 24'  in line or '25 - 29'  in line  or \
                            '30 - 34' in line  or	'35 - 39' in line  or \
                            '40 - 44'  in line or '45 - 49' in line  or \
                            '50 - 54' in line  or '55 - 59' in line  or \
                            '60 - 64' in line  or '65 - 69' in line  or \
                            '70 - 74'  in line or '75 & ABOVE' in line :
                                data.append(data_compile(District = district, Tehsil="", line=line, Gender='Female', Locality='Urban'))
                            if '75 & ABOVE' in line:
                                break
                            
                    if 'MALE' in line:
                        for line in file_in:
                            if '10 & ABOVE' in line or \
                            '10 -  14'  in line  or '15 -  19' in line or  \
                            '20 - 24'  in line or '25 - 29'  in line  or \
                            '30 - 34' in line  or	'35 - 39' in line  or \
                            '40 - 44'  in line or '45 - 49' in line  or \
                            '50 - 54' in line  or '55 - 59' in line  or \
                            '60 - 64' in line  or '65 - 69' in line  or \
                            '70 - 74'  in line or '75 & ABOVE' in line :
                                data.append(data_compile(District = district, Tehsil="", line=line, Gender='Male', Locality='Urban'))
                            if '75 & ABOVE' in line:
                                break
                            
                    if 'TRANSGENDER' in line:
                        for line in file_in:
                            if '10 & ABOVE' in line or \
                            '10 -  14'  in line  or '15 -  19' in line or  \
                            '20 - 24'  in line or '25 - 29'  in line  or \
                            '30 - 34' in line  or	'35 - 39' in line  or \
                            '40 - 44'  in line or '45 - 49' in line  or \
                            '50 - 54' in line  or '55 - 59' in line  or \
                            '60 - 64' in line  or '65 - 69' in line  or \
                            '70 - 74'  in line or '75 & ABOVE' in line :
                                data.append(data_compile(District = district, Tehsil="", line=line,\
                                    Gender='Transgender', Locality='Urban'))
                            if '75 & ABOVE' in line  or  \
                                (district == 'KASUR DISTRICT' and '70 - 74'):
                                urbanComplete = True
                                tehsilComplete = True
                                #df = pd.DataFrame(data)
                                #df.to_csv("test.csv", mode='a', header=False)
                                break        
            

   
def data_compile(District = '', Tehsil = '', line=[], Gender = '', Locality = ''):
    
    age_groups =  ['10 AND ABOVE'  , '10-14',  '15-19' ,  '20-24' , 
                   '25-29' , '30-34' 	,'35-39' ,	'40-44',  '45-49' ,
                   '50-54'  ,'55-59' , '60-64',  '65-69' , '70-74',  '75 AND ABOVE']
    
    # for literacy    
    degrees = ['Total', 'Worked', 'Seeking Work', 'Student', 'House Keeping', \
        'Others']

    mark = [(District, Gender, Locality, line[0:14].strip(), degrees[index], i) for i, index in \
        zip(list(filter(None, line.strip()[14:].split(' '))), range(0,len(degrees)))]

    data = []
    for i in mark:  
        data.append(i)

    df = pd.DataFrame(data)
    
    # for literacy
    df.to_csv(mypath + District + ".csv", mode='a', header=False)

    return data

    
if __name__ == "__main__":
        
    economic_activity()