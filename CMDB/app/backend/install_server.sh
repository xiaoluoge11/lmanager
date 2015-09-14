#!/bin/bash
####install epel_yum######
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
####yum install client#####
yum install salt-master -y
#####change config####
cp -rf /web/CMDB/app/backend/master /etc/salt/master
#####start master####
/etc/init.d/salt-master start
