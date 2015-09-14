#!/bin/bash
####install epel_yum######
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
####yum install client#####
yum install salt-minion -y
####change master ###
sed -i "s/#id:/id: $1/g" /etc/salt/minion
sed -i "s/#master: salt/master: $2/g" /etc/salt/minion
####start client####
/etc/init.d/salt-minion restart 
