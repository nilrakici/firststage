def extractRecord():
    name = []
    age = []
    address = []
    phone = []
    mail = []

    infile = open("latest-customers.txt", "r")
    Lines = infile.readlines()

    for l in Lines:
        l = l.replace(", ", " ")
        l = l.strip("\n")

        name.append(l.split(",")[0])
        age.append(l.split(",")[1])
        address.append(l.split(",")[2])
        phone.append(l.split(",")[3])
        mail.append(l.split(",")[4])
        infile.close()
    return (name, age, address, phone, mail)


record = extractRecord()
a = len(record[1])
outfile = open("MyFile.txt", "w")

for x in range(1, a):
    if (int(record[1][x]) > 40):
        if (int(record[1][x]) < 59):
            outfile.writelines(record[0][x] + "," + record[3][x] + "," + record[4][x] + "\n")

outfile.close()
