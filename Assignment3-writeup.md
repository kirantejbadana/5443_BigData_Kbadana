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
