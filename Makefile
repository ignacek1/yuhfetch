install:
	@cp src/main.py /usr/bin/yuhfetch
	@chmod +x /usr/bin/yuhfetch
	@if [ ! -d /etc/yuhfetch/ ]; then \
		mkdir -p /etc/yuhfetch/; \
	fi
	@cp src/version.txt /etc/yuhfetch/version

reinstall:
	@make install

uninstall:
	@rm /usr/bin/yuhfetch

install-termux:
	@cp src/main.termux.py /data/data/com.termux/files/usr/bin/yuhfetch 
	@chmod +x /data/data/com.termux/files/usr/bin/yuhfetch
	@if [ ! -d /data/data/com.termux/files/etc/yuhfetch/ ]; then \
		mkdir -p /data/data/com.termux/files/etc/yuhfetch/; \
	fi
	@cp src/version.txt /data/data/com.termux/files/etc/yuhfetch/version

reinstall-termux:
	@make install-termux

uninstall-termux:
	@rm /data/data/com.termux/files/usr/bin/yuhfetch
