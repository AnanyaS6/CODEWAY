from tabulate import tabulate
def my_todolist():
    #home page- menu
    print()
    print('\t\tWELCOME TO THE PROGRAM OF \'MY TO-DO LIST\'!')
    print()
    print("-----------------------------------------------------------------------|")
    print('\t\t\t\tMENU-')
    print("-----------------------------------------------------------------------|")
    print('1) Create a new to-do list\n'\
          '2) Display all my to-do lists\n'\
          '3) Add a new task\n'\
          '4) Delete a task\n'\
          '5) Mark a task as \'Done\'\n'\
          '6) Delete a to-do list\n'\
          '7) Return to home page\n'\
          '8) Quit')
    print("-----------------------------------------------------------------------|")
    print()

    disp=[]
    he=[]
    ch='1'
    ch in '12345678' and ch!=''
    while True:
        print('(Enter 7 to return to home page and 8 to exit application)')
        ch=input('Which operation would you like to perform? Enter your choice (1-8): ')
        if ch in '12345678':
            #when choice=1: creating a new to-do list
            if ch=='1':
                dic1={}
                flag=0
                head=input('enter the heading (date/category) : ')
                while head==''or head in '           ':
                    print('Please enter a heading')
                    head=input('enter the heading (date/category) : ')
                    continue
                he.append(head)
                tasnum=int(input('enter how many tasks  ? : '))
                for i in range (1,tasnum+1):
                    tas=input('Enter a new task :')
                    status='   '
                    if tas=='':
                        continue
                    flag+=1
                    dic1[flag]=[status,tas]#    
                disp.append(dic1)
                
                #printing using tabular function
                print('\t\t*****',head,'*****')
                table=[['SNo.','STATUS','TASK-TO-DO']]
                for i in dic1:
                    table.append([i,dic1[i][0],dic1[i][1]])
                print(tabulate(table,headers='firstrow',tablefmt='fancy_grid'))
                print('\nTo-do list created successfully !')
                print('Number of tasks to-do : ',flag)
                print()

            #when choice=2: displaying all the created to-do lists
            elif ch=='2':
                if he==[]:
                    print('No list has been created yet. Create one!')
                    print()
                    continue
                else:
                    print()
                    print('\t\tMY TO-DO LISTS')
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                    #print(disp)
                    for i in range(len(disp)):
                        print('-----------------')
                        print(i+1,'. ',he[i])
                        print('-----------------')
                        table=[['SNo.','STATUS','TASK-TO-DO']]
                        for m in disp[i]:
                            table.append([m,disp[i][m][0],disp[i][m][1]])
                        print(tabulate(table,headers='firstrow',tablefmt='fancy_grid'))
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                print()

            #when choice=3: adding a new task to a to-do list
            elif ch=='3':
                if he==[]:
                    print('No list has been created yet. Create one!')
                    print()
                    continue
                else:
                    d3={}
                    print()
                    print('\t\tMY TO-DO LISTS')
                    print('------------------------------------')
                    for i in range(len(he)):
                        d3[i+1]=he[i]
                        print(i+1,'. ',he[i])
                    print('------------------------------------')
                    print(d3)
                    
                    new=int(input('In which list would you like to add a new task? (enter list number): '))
                    for i in d3:
                        if i==new:
                            new1=input('Enter the task : ')
                            su=list(disp[i-1].keys())
                            #print("su : ", su)
                            disp[i-1][su[-1]+1]=['   ',new1]
                            #print("disp : ",disp)
                            
                            print()
                            print('\t\t*****',d3[i],'*****')
                            table=[['SNo.','STATUS','TASK-TO-DO']]
                            for j in disp[i-1]:
                                table.append([j,disp[i-1][j][0],disp[i-1][j][1]])
                            print(tabulate(table,headers='firstrow',tablefmt='fancy_grid'))

                            print('-------------------------------------------------------|\n')
                            print('new task added to your to-do list successfully!')
                            print('Number of tasks to-do : ',j)
                            print()
                            break
                    else:
                        print('\nSorry, cannot add task, the selected to-do list does not exists\n')
                        continue

            #when choice=4: deleting a task from a to-do list
            elif ch=='4':
                if he==[]:
                    print('No list has been created yet. Create one!')
                    print()
                    continue
                else:
                    d3={}
                    print()
                    print('\t\tMY TO-DO LISTS')
                    print('------------------------------------')
                    for i in range(len(he)):
                        d3[i+1]=he[i]
                        print(i+1,'. ',he[i])
                    print('------------------------------------')
                    
                    old=int(input('From which list would you like to delete a task? (enter list number): '))               
                    if old in d3:
                        print()
                        print('\t\t*****',he[old-1],'- tasks to-do *****')
                        print('------------------------------------')
                        for c in disp[old-1]:
                            print(c,'-',disp[old-1][c][1])
                        print('------------------------------------')

                        delw=int(input('Which task would you like to delete? (Enter task number): '))
                        redisp={}
                        lu=[]
                        if delw in disp[old-1]:
                            del disp[old-1][delw]
                            
                            for n in disp[old-1]:
                                lu.append(disp[old-1][n])
                
                            for u in range(len(lu)):
                                redisp[u+1]=lu[u]
                            print()
                            print('\t\t*****',he[old-1],'*****')
                            table=[['SNo.','STATUS','TASK-TO-DO']]
                            for g in redisp:
                                table.append([g,redisp[g][0],redisp[g][1]])
                            print(tabulate(table,headers='firstrow',tablefmt='fancy_grid'))
                            #print(g,'\t|',redisp[g])
                            print('-------------------------------------------------------|\n')
                            print('task deleted from to-do list successfully!')
                            print('Number of tasks to-do : ',len(lu))
                            print()
                            disp[old-1]=redisp   
                        else:
                            print('\nSorry, cannot delete, the selected task does not exists\n')
                            continue
                    else:
                        print('\nSorry, cannot delete task, the selected to-do list does not exists\n')
                        continue

            #when choice=5: marking a task as 'done'
            elif ch=='5':
                if he==[]:
                    print('No list has been created yet. Create one!')
                    print()
                    continue
                else:
                    d3={}
                    print()
                    print('\t\tMY TO-DO LISTS')
                    table=[['SNo.','TO-DO-LIST']]
                    for i in range(len(he)):
                        d3[i+1]=he[i]
                        table.append([i+1,he[i]])
                    #print(i+1,'. ',he[i])
                    print(tabulate(table,headers='firstrow',tablefmt='fancy_grid'))
                    
                    old=int(input('In which list would you like to mark the task as \'done\'? (enter list number): '))               
                    if old in d3:
                        print()
                        print('\t\t*****',he[old-1],'- tasks to-do *****')
                        table=[['SNo.','STATUS','TASK-TO-DO']]
                        for c in disp[old-1]:
                            table.append([c,disp[old-1][c][0],disp[old-1][c][1]])
                        #print(c,'\t|',disp[old-1][c][1])
                        print(tabulate(table,headers='firstrow',tablefmt='fancy_grid'))

                        delw=int(input('Which task would you like to mark as \'done\'? (Enter task number):'))
                        flag=0
                        if delw in disp[old-1]:
                            disp[old-1][delw][0]+='✓'
                            flag+=1
                            print()
                            print('\t\t*****',he[old-1],'*****')
                            table=[['SNo.','STATUS','TASK-TO-DO']]
                            for g in disp[old-1]:
                                table.append([g,disp[old-1][g][0],disp[old-1][g][1]])
                            print(tabulate(table,headers='firstrow',tablefmt='pretty'))
                            #print(g,'\t|',disp[old-1][g])
                            #print('-------------------------------------------------------|\n')
                            print('task marked as \'done\' successfully!')
                            print('Number of tasks left to-do : ',len(disp[old-1])-flag)
                            print()   
                        else:
                            print('\nSorry, cannot mark as \'done\', the selected task does not exists\n')
                            continue
                    else:
                        print('\nSorry, cannot mark as \'done\', the selected to-do list does not exists\n')
                        continue

            #when choice=6: Deleting a to-do list
            elif ch=='6':
                if he==[]:
                    print('No list has been created yet. Create one!')
                    print()
                    continue
                else:
                    d3={}
                    print()
                    print('\t\tMY TO-DO LISTS')
                    print('------------------------------------')
                    for i in range(len(he)):
                        d3[i+1]=he[i]
                        print(i+1,'. ',he[i])
                    print('------------------------------------')
                    old=int(input('Which list would you like to delete? (enter list number): '))               
                    if old in d3:
                        del he[old-1]
                        del disp[old-1]
                        print()
                        print('To-do list deleted successfully!\n')
                        print('\t\tMY TO-DO LISTS')
                        print('------------------------------------')
                        if any(disp)==True:
                            for i in range(len(he)):
                                d3[i+1]=he[i]
                                print(i+1,'. ',he[i])
                        else:
                            print('No to-do list present!')
                        print('------------------------------------')
                        print()
                        
                    else:
                        print('\nSorry, cannot delete, the selected to-do list does not exists\n')
                        continue
            
            #when choice=7: Displaying home page- MENU
            elif ch=='7':
                print()
                print('\t\tWELCOME TO THE PROGRAM OF \'MY TO-DO LIST\'!!!')
                print()
                print("-----------------------------------------------------------------------|")
                print('\t\t\t\tMENU-')
                print("-----------------------------------------------------------------------|")
                print('1) Create a new to-do list\n'\
                      '2) Display all my to-do lists\n'\
                      '3) Add a new task\n'\
                      '4) Delete a task\n'\
                      '5) Mark a task as \'Done\'\n'\
                      '6) Return to home page\n'\
                      '7) Quit')
                print("-----------------------------------------------------------------------|")
                print()
                continue

            #when choice=8: Quitting program
            elif ch=='8':
                print('Exiting program....')
                break       
        else:
            print('Warning! Please enter the correct choice')
            continue
    import time
    time.sleep(4)
    print()
    print('THANK YOU!')
    print('\n\nCreated by-')
    print('ANANYA SHARMA\n')
my_todolist()
