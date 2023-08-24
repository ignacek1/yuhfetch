install:
	cp src/main.py /usr/bin/yuhfetch
	chmod +x /usr/bin/yuhfetch
reinstall:
	make install
uninstall:
	rm /usr/bin/yuhfetch
install-termux:
	cp src/main.termux.py /data/data/com.termux/files/usr/bin/yuhfetch 
	chmod +x /usr/bin/yuhfetch
reinstall-termux:
	make install-termux
uninstall-termux:
	rm /data/data/com.termux/files/usr/bin/yuhfetch
