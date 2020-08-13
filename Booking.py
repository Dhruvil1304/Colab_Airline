
from Airdb import *
from Flidb import *
from Custdb import *


op=1
while op==1:
    print('Please select ur choice:')
    print('\t\t 1.Airport')
    print('\t\t 2.Flights')
    print('\t\t 3.Customer')
    print('\t\t 4.exit')
    choice=int(input('Enter ur choice:'))

    if choice==1:
        op1=1
        while op1 !=5:
            print('\t1 for entry')
            print('\t2 for view')
            print('\t3 for search')
            print('\t4 for view flights')
            print('\t5 for main menu')
            op1=int(input('Enter ur choice:'))

            if op1==1:
                add='y'
                while add=='y':
                    print('-------Entry--------')
                    a1=Airport()
                    a1.setairid(int(input('Enter Airport id:')))
                    a1.setaircity(input('Enter Airport city:'))
                    a1.setairname(input('Enter Airport name:'))
                    a1.setairtype(input('Enter Airport type:'))

                    if insertair(a1):
                        print("You have added airport properly.")
                    else:
                        print("Error in adding data of airport.. ")
                    add=input('Do u want to add another airport?(y/n)')

            elif op1==2:
                print('---------View----------')
                print('CITY \t ID \t NAME \t TYPE ')
                for row in viewair():
                    print(row[0],'\t',row[1],'\t',row[2],'\t',row[3])
                    print('------------------------------------------')


            elif op1==3:
                print('--------Search--------')
                search=int(input('Enter id for get details:'))
                print('CITY \t ID \t NAME \t TYPE ')
                for row in findair(search):
                    print(row[0], '\t', row[1], '\t', row[2], '\t', row[3])
                    print('------------------------------------------')



            elif op1==4:
                print('--------Available FLights---------')
                print('\tID \t SOURCE \t DESTINATION \t DATE \t TAKEOFF \t CLASS \t AIRLINE \t VIA \t LANDING ')
                source=int(input('Enter source id of airport where u want to check flights:'))
                for row in avialable(source):
                    print('\t',row[0], '\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4], '\t', row[5], '\t', row[6],'\t', row[7],' \t',row[8])
                    print('--------------------------------------------------------------------------------------------------------------------------')





    elif choice==2:
        op5=1
        while op5 != 4:
            print('\t1 for entry')
            print('\t2 for view')
            print('\t3 for search')
            print('\t4 for main menu')
            op5 = int(input('Enter ur choice:'))


            if op5 == 1:
                    print('-------Entry--------')
                    f1=Flight()
                    print('CITY \t ID \t NAME \t TYPE ')
                    for row in viewair():
                        print(row[0], '\t', row[1], '\t', row[2], '\t', row[3])
                    f1.setsource(input('Enter source:'))
                    f1.setdesti(input('Enter destination:'))
                    f1.setid(int(input('Enter flight id:')))
                    f1.setairline(input('Enter flight airline:'))
                    f1.setclasss(input('Enter flight class:'))
                    f1.setdate(input('Enter flying date:'))
                    f1.settakeoff(input('Enter takeoff timing:'))
                    f1.setlanding(input('Enter landing timing:'))
                    f1.setvia(input('Enter via airport:'))
                    if insertfli(f1):
                        print("You have added flight properly.")
                    else:
                        print("Error in adding data of flight.. ")

            elif op5 == 2:

                    print('-------View--------')
                    print('\tID \t SOURCE \t DESTINATION \t DATE \t TAKEOFF \t CLASS \t AIRLINE \t  VIA \t LANDING ')
                    for row in viewfli():
                        print('\t',row[0],'\t',row[1],'\t \t',row[2],'\t \t',row[3],' \t',row[4],' \t\t',row[5],' \t',row[6],' \t',row[7],' \t',row[8])
                        print('--------------------------------------------------------------------------------------------------------------------------')





            elif op5==3:
                    searchf=int(input('Enter flight id :'))
                    print('\tID \t SOURCE \t DESTINATION \t DATE \t TAKEOFF \t CLASS \t AIRLINE \t VIA \t LANDING ')
                    for row in findfli(searchf):
                        print('\t',row[0], '\t', row[1], '\t \t', row[2], '\t \t', row[3], ' \t', row[4], ' \t\t', row[5], ' \t',row[6], ' \t', row[7],' \t',row[8])
                        print('--------------------------------------------------------------------------------------------------------------------------')




    elif choice==3:
        op8 = 1
        while op8 != 4:
            print('\t1 for entry')
            print('\t2 for view')
            print('\t3 for search')
            print('\t4 for main menu')
            op8 = int(input('Enter ur choice:'))

            if op8==1:
                print('-------Entry------')
                c1=Customer()
                c1.setcname(input('Enter customer name: '))
                c1.setcid(int(input('Enter customer id:')))
                c1.setcmob(int(input('Enter customer mobile no:')))

                i='yes'
                while i=='yes':
                    print('Select source id and destination id')
                    print('CITY \t ID \t NAME \t TYPE ')
                    for row in viewair():
                        print('\t',row[0], '\t', row[1], '\t', row[2], '\t', row[3])
                        print('-----------------------------------------------------')

                    sid = input("Enter Scource  Airport city from list :")
                    did = input("Enter Destination Ariport city from list :")

                    print('======Available flights======')
                    print('\tID \t SOURCE \t DESTINATION \t DATE \t TAKEOFF \t CLASS \t AIRLINE \t VIA \t LANDING ')
                    for row in avail(sid,did):
                        print('\t',row[0], '\t', row[1], ' \t\t', row[2], '\t \t', row[3], ' \t', row[4], ' \t\t', row[5], ' \t',row[6], ' \t', row[7],' \t',row[8])
                        print('--------------------------------------------------------------------------------------------------------------------------')


                    select=int(input('Please select ur flight'))
                    c1.setbookings(select)
                    i=input('Do u want to do another booking?..yes/no')
                if insertcust(c1):
                    print("Booking confirmed.")
                else:
                    print("Error in flight booking.. ")





            elif op8==2:
                print('--------Customers--------')


                for row in viewcust():
                    print('\tC_NAME \t C_ID \t C_MOB \t C_BOOKINGS')
                    print('\t',row[0],'\t',row[1],'\t',row[2],'\t',row[3])
                    print('-----------------------------------------------')
                    x=input('Flight details?y/n')
                    if x.lower()=='y':
                        for r in row[3]:
                            print('\tID \t SOURCE \t DESTINATION \t DATE \t TAKEOFF \t CLASS \t AIRLINE \t VIA \t LANDING ')
                            for row in findfli(r):
                                print('\t', row[0], '\t', row[1], '\t \t', row[2], '\t \t', row[3], ' \t', row[4],' \t\t', row[5], ' \t', row[6], ' \t', row[7], ' \t', row[8])
                                print('--------------------------------------------------------------------------------------------------------------------------')





            elif op8==3:

                find=int(input('Enter customer id: '))
                print('\tC_NAME \t C_ID \t C_MOB \t C_BOOKINGS')
                for row in findcust(find):
                    print('\t',row[0], '\t', row[1], '\t', row[2], '\t', row[3])
                    print('-----------------------------------------------------')
                    x = input('Flight details?y/n')
                    if x.lower() == 'y':
                        for r in row[3]:
                            print('\tID \t SOURCE \t DESTINATION \t DATE \t TAKEOFF \t CLASS \t AIRLINE \t VIA \t LANDING ')
                            for row in findfli(r):
                                print('\t', row[0], '\t', row[1], '\t \t', row[2], '\t \t', row[3], ' \t', row[4],' \t\t', row[5], ' \t', row[6], ' \t', row[7], ' \t', row[8])
                                print('--------------------------------------------------------------------------------------------------------------------------')




    elif choice==4:
        print('You are exited')











