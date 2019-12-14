from configparser import ConfigParser
c=ConfigParser()
c["settings"]={
    'debug':"true",
    'security_key':"jsfjk",
'log_path':"D://dkkfmvk"}
c["DB"]={
    'db_name':"mysql",
    'db_type':"RDBms"
}
f=open("G:\SOFTWARES\sample.ini","w")
c.write(f)
f.close()