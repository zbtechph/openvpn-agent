# openvpn-agent

this script sends a json data to your api to monitor active connections and bandwidth.
data includes trusted_ip, bytes_received, bytes_sent, common_name, and script type (client-connect or client-disconnect)
https://openvpn.net/community-resources/reference-manual-for-openvpn-2-4/#environmental-variables

first, clone or download this repository then edit agent.py

change endpoint value to your api endpoint.

add this line to your openvpn server config. usually, `/etc/openvpn/server.conf`
```
client-connect ./openvpn-agent/agent.py
client-disconnect ./openvpn-agent/agent.py
```
then restart openvpn
```
systemctl restart openvpn
```

note: bytes_sent and bytes_received will only return a value on client-disconnect script.
