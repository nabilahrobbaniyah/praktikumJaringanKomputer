tracing dns
1. Flush DNS. ipconfig /flushdns
2. Buka Wireshark
3. Set filter: ip.addr == (IP)
4. start capture
5. Generate traffic. Buka browser: http://www.ietf.org
6. stop capture
7. Cari paket DNS (filter: dns)
![tampilan wireshark](../assets/week4/image4.3.1.png)
![tampilan wireshark](../assets/week4/image4.3.2.png)
![tampilan wireshark](../assets/week4/image4.3.3.png)
![tampilan wireshark](../assets/week4/image4.3.4.png)
![tampilan wireshark](../assets/week4/image4.3.5.png)
![tampilan wireshark](../assets/week4/image4.3.6.png)
![tampilan wireshark](../assets/week4/image4.3.7.png)
![tampilan wireshark](../assets/week4/image4.3.8.png)
![tampilan wireshark](../assets/week4/image4.3.9.png)