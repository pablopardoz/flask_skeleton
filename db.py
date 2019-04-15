import psycopg2
from clases import *

class dbPostgres:
    usr = ""
    psw = ""
    host = ""
    database=""

    #guardo el objeto db
    db = None

    def __init__(self):
        self.usr = 'xbdqjlgf'
        self.psw = 'ATrpegCtxj_Mzl0026x3QoHkB84PZjfb'
        self.database = "xbdqjlgf"
        self.host = "baasu.db.elephantsql.com"
        self.db = None
        #print self.psw
        #print "creado objeto"

    def dbOpen(self):
        self.db = psycopg2.connect(dbname=self.database, user=self.usr, host=self.host, password=self.psw)
        #print self.db

    def dbClose(self):
        self.db.close()
        #print "cerrada"