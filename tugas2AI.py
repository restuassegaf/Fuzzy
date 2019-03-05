import csv

def fuzzyfikasi(p, h):
    pr, ps, pt = 0, 0, 0
    hr, hs, ht = 0, 0, 0

    if(p <= 0.4):
        pr = 1
    elif (p > 0.4) and (p < 0.9):
        pr = (0.9 - p)/(0.9 - 0.4)
        ps = 1 - pr
    elif (p == 0.9):
        ps = 1
    elif (p > 0.9) and (p < 1.2):
        ps = (1.2 - p)/(1.2 - 0.9)
        pt = 1 - ps
    elif (p >= 1.2):
        pt = 1

    if (h <= 10):
        hr = 1
    elif (h > 10) and (h < 45):
        hr = (45 - h)/(45 - 10)
        hs = 1 - hr
    elif (h == 45):
        hs = 1
    elif (h > 45) and (h < 70):
        hs = (70 - h)/(70 - 30)
        ht = 1 - hs
    elif (h >= 70):
        ht = 1
    return pr, ps, pt, hr, hs, ht

def rule(pr, ps, pt, hr, hs, ht):
    iya = [0, 0, 0]
    tidak = [0, 0, 0, 0, 0, 0]
    if (pr > 0) and (hr > 0):
        tidak[0] = min(pr, hr)
    if (pr > 0) and (hs > 0):
        iya[0] = min(pr, hs)
    if (pr > 0) and (ht > 0):
        iya[1] = min(pr, ht)
    if (ps > 0) and (hr > 0):
        tidak[1] = min(ps, hr)
    if (ps > 0) and (hs > 0):
        tidak[2] = min(ps, hs)
    if (ps > 0) and (ht > 0):
        iya[2] = min(ps, ht)
    if (pt > 0) and (hr > 0):
        tidak[3] = min(pt, hr)
    if (pt > 0) and (hs > 0):
        tidak[4] = min(pt, hs)
    if (pt > 0) and (ht > 0):
        tidak[5] = min (pt, ht)

    return max(iya), max(tidak)

def deffuzyfikasi(iya, tidak):
    return (iya*60 + tidak*40)/(iya+tidak)

with open('DataTugas2.csv') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    with open('TebakanTugas2.csv','w',newline='')as f:
        fieldnames=['orang yang layak','pendapatan','hutang']
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            pr, ps, pt, hr, hs, ht = fuzzyfikasi(float(row[1]), float(row[2]))
            iya, tidak = rule(pr, ps, pt, hr, hs, ht)
            hasil = deffuzyfikasi(iya, tidak)
            if( hasil > 50):
                print('orang yang layak mendapatkan bantuan orang ke-',row[0])
                writer.writerow({'orang yang layak':row[0],'pendapatan':row[1],'hutang':row[2]})
