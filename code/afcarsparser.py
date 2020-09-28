import subprocess as s, pyautogui as p, os, datetime as dt, time, shutil as sh

def afcarsfcparse(text, typ_):
    '''Parses a text file into predetermined column sizes for a Foster Care file and a Adoption file.'''
    start = 0 #initialize the beginning value for the parse.
    #The lengths of columns for FC and AD depending on which gile is being parsed.
    fcwidths = [2,6,5,12,8,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,2,8,8,8,8,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,4,8,8,1,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,8,1,1,1,1,1,1,1,1,5]
    adwidths = [2,6,12,1,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,4,1,8,8,8,1,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5]
    newtext = ''
    if typ_ == 'ad':
        for width in adwidths:
            end = start + width
            newtext += text[start:end]+','
            start = end
    elif typ_ == 'fc':
        for width in fcwidths:
            end = start + width
            newtext += text[start:end]+','
            start = end
    
    return(newtext)

def fcrpts(file_):
    '''Run the AFCARS reports for Foster Care'''
    date = dt.datetime.now()
    path = os.path.dirname(file_) + '\\'
    report = (r'FCreport' + str(date.month) + '.' + str(date.day) + '.' +str(date.year) + '.txt')
    freq =  (r'FCfreqreport' + str(date.month) + '.' + str(date.day) + '.' +str(date.year) + '.txt')

    #Move source file into folder with exe
    base = os.path.basename(file_)
    des = r'U:\DFS\DFS Data Unit\AFCARS\AFCARS Checkit\{}'.format(base)
    sh.copy(file_,des)

    os.chdir('U:\DFS\DFS Data Unit\AFCARS\AFCARS Checkit')
    s.Popen('chkdat3.exe')

    p.sleep(.3); p.write(base); p.press('enter')
    p.sleep(.3); p.write(report); p.press('enter')
    p.sleep(.3); p.write(r's'); p.press('enter')
    p.sleep(.3); p.write(r'10'); p.press('enter')

    #Move new file to original folder with source file
    desdir = os.path.dirname(des) + '\\'
    src = desdir + report
    des = path + report
    sh.copy(src, des)

    #Move to next folder with exe
    des = r'U:\DFS\DFS Data Unit\AFCARS\AFCARS Checkit\Freq\{}'.format(base)
    sh.copy(file_,des)

    os.chdir('U:\DFS\DFS Data Unit\AFCARS\AFCARS Checkit\Freq')
    s.Popen('xfreq_n.exe')

    p.sleep(.3); p.write(base); p.press('enter')
    p.sleep(.3); p.write(freq); p.press('enter')
    p.sleep(.3); p.write(r's'); p.press('enter')

    #Move freq report to original folder with source
    desdir = os.path.dirname(des) + '\\'
    src = desdir + freq
    des = path + freq
    sh.copy(src, des)

def adrpts(file_):
    '''Run the AFCARS reports for Adoption'''
    date = dt.datetime.now()
    path = os.path.dirname(file_) + '\\'
    month = date.month
    day = date.day
    year = date.year
    report = r'ADreport{}.{}.{}.txt'.format(month,day,year) #For some reason another name for the report can't be used???????
    freq =  r'ADfreqreport{}.{}.{}.txt'.format(month,day,year)

    #Move source file into foler with exe
    base = os.path.basename(file_)
    des = r'U:\DFS\DFS Data Unit\AFCARS\AFCARS Checkit\{}'.format(base)
    sh.copy(file_,des)

    os.chdir('U:\DFS\DFS Data Unit\AFCARS\AFCARS Checkit')
    s.Popen('chkdat3.exe')

    p.sleep(.3); p.write(base); p.press('enter')
    p.sleep(.3); p.write(r's'); p.press('enter')
    p.sleep(.3); p.write(report); p.press('enter')
    p.sleep(.3); p.write(r'10'); p.press('enter')
    time.sleep(1)

    #Move new file to original folder with source file
    desdir = os.path.dirname(des) + '\\'
    src = desdir + report
    des = path + report
    sh.copy(src, des)

    #Move to next folder with exe
    des = r'U:\DFS\DFS Data Unit\AFCARS\AFCARS Checkit\Freq\{}'.format(base)
    sh.copy(file_,des)

    os.chdir('U:\DFS\DFS Data Unit\AFCARS\AFCARS Checkit\Freq')
    s.Popen('xfreq_n.exe')

    p.sleep(.3); p.write(base); p.press('enter')
    p.sleep(.3); p.write(r's'); p.press('enter')
    p.sleep(.3); p.write(freq); p.press('enter')

    #Move freq report to original folder with source
    desdir = os.path.dirname(des) + '\\'
    src = desdir + freq
    des = path + freq
    sh.copy(src, des)


#The headers for the Foster Care and Adoption parsed files.
adheaders = "1-State FIPS Code,2-Report Month-Year End,3-Record Number (PID),4-State Involvement,5-Child DOB,6-Sex,7a-Race-AI,7b-Race-AS,7c-Race-BL,7d-Race-HI,7e-Race-CA,7f-Race-UD,8-Hispanic Origin,9-Special Needs,10-Primary Special Needs,11-Mental Retardation,12-Visual-Hearing Impairment,13-Physically Disabled,14-Emotionally Disturbed,15-Other Medical Condition,16-BIO Mother YOB,17-BIO Father YOB,18-Mother Married at child's birth,19-BIO Mother TPR Date,20-BIO Father TPR Date,21-Adoption Finalization Date,22-Adoptive Parents Family Structure,23-Adoptive Mother YOB,24-Adoptive Father YOB,25a-Adoptive Mother's Race - AI,25b-Adoptive Mother's Race - AS,25c-Adoptive Mother's Race - BL,25d-Adoptive Mother's Race - PA,25e-Adoptive Mother's Race - CA,25f-Adoptive Mother's Race - OT,26-Adoptive Mother/s Hispanic Origin,27a-Adoptive Father's Race - AI,27b-Adoptive Father's Race - AS,27c-Adoptive Father's Race - BL,27d-Adoptive Father's Race - PA,27e-Adoptive Father's Race - CA,27f-Adoptive Father's Race - OT,28- Adoptive Mother/s Hispanic Origin,29-Adoptive Step Parent relationship to Child,30-Adoptive Other Relative relationship to child,31-Adoptive Foster Parent Relationship to Child,32-Adoptive Other Non-relative Relationship to child,33-Child Placed in,34-Child Placed byReceiving Monthly Subsidy,35- Receiving a Monthly Subsidy,36-Monthly Amount"
fcheaders = "1StateFIPS,2RptPerEndtxt,3LocalFIPS,4RecNum,5LastRevtxt,6ChDOBtxt,7ChSex,8aChRcNat,8bChRcAsn,8cChRcBl,8dChRcPac,8eChRcWh,8fChRcUnab,9ChHispLat,10ChDiag,11ChRetard,12ChVisual,13ChPhys,14ChEmotnl,15ChMedicl,16AdoptInd,17AdoptAge,18FirstRmvtxt,19TtlRmv,20PrDschrgtxt,21CurrRmvtxt,22RmvTranstxt,23CurrPlmttxt,24TtlPlmt,25TypRmv,26PhysAb,27SexAb,28Neg,29ParAlc,30ParDrg,31ChAlc,32ChDrg,33ChDisab,34ChBehav,35ParDeath,36ParJail,37ParCope,38Abandon,39Relinq,40Housing,41CurrPlmtSet,42PlmtOutState,43Goal,44FamStr,45Par1BirthYr,46Par2BirthYr,47MomTPRtxt,48DadTPRtxt,49FCStrct,50PrimBirthYr,51SecdBirthYr,52aPrimRcNat,52bPrimRcAsn,52cPrimRcBl,52dPrimRcPac,52ePrimRcWh,52fPrimRcUnab,53PrimHispLat,54aSecdRcNat,54bSecdRcAsn,54cSecdRcBl,54dSecdRcPac,54eSecdRcWh,54fSecdRcUnab,55SecdHispLat,56FCDschrgtxt,57DschrgTranstxt,58DschrgReas,59FC-IVE,60Adpt-IVE,61TitleIVA,62TitleIVD,63TitleXIX,64SSI,65None,66MthRate"

#PROGRAM BEGINS

typ = (input('Enter "FC" for a Foster Care file, "AD" for an Adoption file, or "B" for both.\n')).lower()

if typ == 'fc':
    
    file = input('Enter the text file full path that needs to be parsed:\n')
    if not file.endswith('.txt'):
        file += '.txt'

    newfile = os.path.splitext(os.path.basename(file))[0]
    newfile = os.path.dirname(file) + '\\' + newfile + '.csv'


    xtra = (input('Do you want the extra reports as well? (y/n)\n')).lower()

    with open(file) as txt, open(newfile,'w')as output:
        content = txt.readlines()
        print(fcheaders, file = output)    
        for line in content:
            if not line.startswith('10'):           #Skip any dummy records 
                continue
            if len(line) < 198:                     #Total length of the whole row should be 198. If any more columns are added, then this will increase.
                spaces = 198 - (len(line))
                line = line + (' ' * spaces)
            newline = afcarsfcparse(line, typ)
            print(newline, file = output)

        if xtra == 'y':                             #Run the reports.
            fcrpts(file)
        
elif typ == 'ad':

    file = input('Enter the text file full path that needs to be parsed:\n')
    if not file.endswith('.txt'):
        file += '.txt'

    newfile = os.path.splitext(os.path.basename(file))[0]
    newfile = os.path.dirname(file) + '\\' + newfile + '.csv'


    xtra = (input('Do you want the extra reports as well? (y/n)\n')).lower()

    with open(file) as txt, open(newfile,'w')as output:
        content = txt.readlines()
        print(adheaders, file = output)    
        for line in content:
            if not line.startswith('10'):
                continue
            if len(line) < 111:                     #Total length is similiar to Foster Care, but the length shoukld be 111.
                spaces = 111 - (len(line))
                line = line + (' ' * spaces)
            newline = afcarsfcparse(line, typ)
            print(newline, file = output)

        if xtra == 'y':
            adrpts(file)

elif typ == 'b':
    
    fcfile = input('Enter the FC text file full path that needs to be parsed:\n')
    if not fcfile.endswith('.txt'):
        fcfile += '.txt'

    fcnewfile = os.path.splitext(os.path.basename(fcfile))[0]
    fcnewfile = os.path.dirname(fcfile) + '\\' + fcnewfile + '.csv'
    
    adfile = input('Enter the AD text file full path that needs to be parsed:\n')
    if not adfile.endswith('.txt'):
        adfile += '.txt'

    adnewfile = os.path.splitext(os.path.basename(adfile))[0]
    adnewfile = os.path.dirname(adfile) + '\\' + adnewfile + '.csv'

    xtra = (input('Do you want the extra reports as well? (y/n)\n')).lower()

    with open(fcfile) as txt, open(fcnewfile,'w')as output:
        content = txt.readlines()
        print(fcheaders, file = output)    
        for line in content:
            if not line.startswith('10'):
                continue
            if len(line) < 198:
                spaces = 198 - (len(line))
                line = line + (' ' * spaces)
            newline = afcarsfcparse(line, 'fc')
            print(newline, file = output)
            
    with open(adfile) as txt, open(adnewfile,'w')as output:
        content = txt.readlines()
        print(adheaders, file = output)    
        for line in content:
            if not line.startswith('10'):
                continue
            if len(line) < 111:
                spaces = 111 - (len(line))
                line = line + (' ' * spaces)
            newline = afcarsfcparse(line, 'ad')
            print(newline, file = output)
    if xtra == 'y':
        fcrpts(fcfile)
        adrpts(adfile)        

else:
    print('You did not enter FC or AD. Please run the program again!')
