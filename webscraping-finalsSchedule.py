from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv
url='https://registrar.web.baylor.edu/exams-grading/fall-2023-final-exam-schedule'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url,headers=headers)

webpage= urlopen(req).read()

soup  = BeautifulSoup(webpage,'html.parser')

print(soup.title.text)

tables=soup.findAll('table')       #just trying to find first hit, not iterating
finals_table=tables[1]

infile = open('myclasses.csv','r')
csv_file=csv.reader(infile)

tr=finals_table.findAll('tr')

for rec in csv_file:
    myclass=rec[0]
    mytime=rec[1]

    for row in tr:
        td=row.findAll('td')
        if td:
            sch_class=td[0].text
            sch_time=td[1].text
            exam_day=td[2].text
            exam_time=td[3].text

            if sch_class==myclass and sch_time==mytime:
                print(myclass,mytime,exam_day,exam_time)

