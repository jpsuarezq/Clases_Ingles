sudo nano /etc/resolv.conf


nameserver 1.1.1.1
nameserver 8.8.8.8

sudo resolvectl flush-caches
ping opencode.ai
