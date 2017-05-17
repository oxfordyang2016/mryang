import MySQLdb
from  colors import red,yellow,green,blue 







#can connect mysql and mariadb
def connectmysql(host1,user1,passwd1,db1):
    db=MySQLdb.connect(host=str(host1), user=str(user1), passwd=str(passwd1),db=str(db1))
    cursor=db.cursor()
    print red(str(db))
    print yellow(str(cursor))
    return [db,cursor]



def execute(cursor,sql):
    print(yellow(sql))
    cursor.execute(sql)


#get row accoring to the above sql
def getrow(db,cursor):
    # commit your changes
    db.commit()
    tabledict={}
    numrows = int(cursor.rowcount)
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    for x in range(0,numrows):
        row = cursor.fetchone()
        #print(row)
        tmpdict={}
        for k in range(0,len(row)):
            #print str(field_names[k])+"                 |---------------------------->"+str(row[k]) 
            tmpdict[str(field_names[k])]=str(row[k])
        tabledict[str(x)]=tmpdict
    return tabledict


#return the qury result of fianl.
def ultimatesql1(host,user,passwd,db,sql):
    
    db=MySQLdb.connect(host, user, passwd,db)
    cursor=db.cursor()
    connectmysql(host,user,passwd,db)
    print(green('i have connect db===='))
    execute(sql)
    result=getrow()
    return result


#debug test
def ultimatesql(host,user,passwd,db,sql):
    
    #db=MySQLdb.connect(host, user, passwd,db)
    #cursor=db.cursor()
    db,cursor=connectmysql(host,user,passwd,db)
    execute(cursor,sql)
    result=getrow(db,cursor)
    print red(str(result))
    return result








