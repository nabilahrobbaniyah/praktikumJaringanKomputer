# Identifikasi slow start dan congestion avoidance
a. Slow start selalu dimulai setelah koneksi TCP established (3-way handshake selesai)
Saat congestion window (cwnd) masih kecil (biasanya 1 MSS)
Di grafik, ditandai dengan kenaikan eksponensial (kurva melengkung ke atas)
Sequence number naik semakin cepat setiap RTT
b. Berakhir saat cwnd mencapai ssthresh (slow start threshold)
Setelah itu pertumbuhan berubah dari eksponensial → linear
Di grafik, transisi dari kurva melengkung → garis hampir lurus
c. congestion avoidance mulai langsung setelah slow start berakhir, pertumbuhan menjadi linear (additive increase)
cwnd bertambah sekitar 1 MSS per RTT
Di grafik, sequence number naik dengan slope konstan
