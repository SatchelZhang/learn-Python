def Dayup(df):
    Dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            Dayup = Dayup * (1-0.01)
        else:
            Dayup = Dayup * (1 + df)
    return Dayup
dayfactor = 0.01
while Dayup(dayfactor) < 37.78:
    dayfactor += 0.001
print('工作日的努力参数是：{:.3f}'.format(dayfactor))