import cPickle as p

u'''load user data,if it is null ,indicates it first use'''
def load():
    accountsFile='account.data'
    f = file(accountsFile)
    accountlist=[]
    try:
        accountlist=p.load(f)
    except Exception , e :
        print 'firstuser'
    return accountlist
def IsFirstUse():
    if  len(load())==0:
        return True
    else :
        return False
def writein(list):
    accountsFile='account.data'
    f = file(accountsFile, 'w')
    p.dump(list, f)
    f.close()
def clear():
    accountsFile='account.data'
    f = file(accountsFile, 'w')
    accountlist=[]
    p.dump(accountlist, f)
