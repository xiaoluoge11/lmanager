import os
def disk():
#        grains={}
#        disk = os.popen('vgdisplay  | grep "VG Size" | awk \'{print $3}\'').read()
#        disk = disk.strip('\n')
#        grains['disk']=disk
#        return grains
    grains={}  
    disk = os.statvfs("/")  
    grains['disk'] = (disk.f_bsize * disk.f_blocks)/1024/1024/1024  
    return grains  
if __name__ == '__main__':
    print disk()
