T=int(input())
temp={'01':31, '02':28, '03':31, '04':30, '05':31, '06':30,
      '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
for tc in range(1,T+1):
    s=input()
    YY, MM, DD = s[:4], s[4:6], s[6:]
    if( (MM in list(temp.keys())) and (1 <= int(DD) <= temp[MM]) ):
        print(f"#{tc} {YY}/{MM}/{DD}")       
    else:
        print(f"#{tc} -1")