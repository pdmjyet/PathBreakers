import os

for line in open('/home/pady/Downloads/pathbreakers.csv'):
    row = line.split(',')
    if row[1].strip() == "Id" or row[1].strip() == "":
        for idx, value in enumerate(row):
            if value == "Id":
                pp = idx
            if value == "Name":
                name = idx
            if value == "Course":
                degree= idx
            if value == "Year of Graduation":
                yog = idx
            if value == "Profession":
                profession = idx
            if value == "Tag":
                tag = idx
            if value == "Link":
                link = idx
        continue
    cmd = " --profilepic '"+row[pp]+"'"
    cmd += " --name '"+ row[name]+"'"
    cmd += " --degree '"+row[degree]+"'"
    cmd += " --yog "+row[yog]
    cmd += " --profession '"+row[profession]+"'"
    cmd += " --tag '"+row[tag]+"'"
    cmd += " --link '"+row[link]+"'"
    print(cmd)
    #os.system("../manage.py populate_db "+ cmd, shell=True)