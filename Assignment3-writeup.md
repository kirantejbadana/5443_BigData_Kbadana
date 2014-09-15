![Command prompt](http://198.199.95.27/Hadoop.png)

1. How do you add nodes to your Hadoop cluster?
<br>Ans. Firstly all the systems needs to be present in the network. <br>
To know the status of the clusters connected to the system "JPS" must be typed<br>
<br>
Go to the network interfaces by typing in the below command. <br>
sudo vi /etc/network/interfaces <br>
Type in the password as asked. <br>
<br>
update the below line as mentioned <br>
```
iface eth0 inet static 
address <ip address>
netmask
network
broadcast
gateway
dns-search
dns-nameserver
```

Go to the host name file present in /etc/hostname
<br>
```
vi /etc/hostname
```
Give the name as Slave01
Re-start the machine by typint the command
```
Sudo shutdown -r now
```
Go to the master system and edit the host file by typing the below commands

```
Sudo vi /etc/hosts
```
<IP Address> Slave01

Copying ssh key to the slave

```
ssh-copy-id -i ~/.ssh/id_rsa.pub hduser@Slave01
```


2. Can everyone in class add the remaining members of the class to thier cluster?

Yes every one in the class can add every other person in the class as a cluster by following the above steps by acting as a master. And every other person in the class must act as slave.

3. Can everyone simultaneously run thier own Hadoop cluster, AND be a slave (worker) in another Hadoop cluster?

Yes, every one can simulataniously run the zhadoop cluster but while acting as slave and if one of the slave is asked to do a job which uses all the mapreduce then it the next job in the queue is kept waiting.



