#!/usr/bin/env python
import ConfigParser
cf = ConfigParser.ConfigParser()    
cf.read("/web/CMDB/app/backend/config.ini")
def dbconfig(): 
    db_host = cf.get("db","db_host")
    db_port = cf.get("db","db_port")
    db_user = cf.get("db","db_user")
    db_pass = cf.get("db","db_pass")
    db_name = cf.get("db","db_name") 
    db = {"host":db_host,"port":db_port,"user":db_user,"pass":db_pass,"name":db_name} 
    return db   
if __name__=="__main__":
    xiaoluo = dbconfig()
    print xiaoluo
