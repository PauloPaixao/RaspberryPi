# raspberrypi

if you are running http://www.raspbmc.com/ then you must follow the raspbmc instructions

first lets login to your raspberrypi over ssh 

	ssh pi@raspberrypi

then lets make a directory to put your files in, move into it and make our main script 

	mkdir duckdns
	cd duckdns
	vi duck.sh

now copy this text and put it into the file (in vi you hit the i key to insert, ESC then u to undo) you must change your token and domain to be the one you want to update

you can pass a comma separated (no spaces) list of domains
you can if you need to hard code an IP (best not to - leave it blank and we detect your remote ip)
hit **ESC** then use use arrow keys to move the cursor x deletes, i puts you back into insert mode 

	echo url="https://www.duckdns.org/update?domains=exampledomain&token=a7c4d0ad-114e-40ef-ba1d-d217904a50f2&ip=" | curl -k -o ~/duckdns/duck.log -K -

now save the file (in vi hit ESC then :wq! then ENTER)
this script will make a https request and log the output in the file duck.log
now make the duck.sh file executeable 

	chmod 700 duck.sh

next we will be using the cron process to make the script get run every 5 minutes 

	crontab -e

copy this text and paste it at the bottom of the crontab 

	*/5 * * * * ~/duckdns/duck.sh >/dev/null 2>&1

now save the file (CTRL+o then CTRL+x)
lets test the script
 
	./duck.sh

this should simply return to a prompt
 we can also see if the last attempt was successful (OK or bad KO) 

	cat duck.log

if it is KO check your Token and Domain are correct in the duck.sh script
 The final task for Raspbmc is to make the cron autostart on reboot for Raspbian you don't need to do this
 first we simply manualy start the crontab 

	sudo service cron start

Then to automatically start cron on reboot, in Raspmbc you check the option in the Programs Raspbmc menu in XBMC

	http://www.jeffreythompson.org/blog/2014/11/13/installing-ffmpeg-for-raspberry-pi/

Check home video 
http://145.132.122.80:64672/mjpg/video.mjpg


#Rsync 

How to rsync the files.

	rsync -avz -e ssh pssp@paulop-rp2.duckdns.org:/home/pssp/src/images/20160706 /home/paulop/processed/



## Install H264 Support

Run the following commands, one at a time.

	cd /usr/src
	git clone git://git.videolan.org/x264
	cd x264
	./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl
	make
	sudo make install

## Install FFMPEG

Add lines similar to the  `--enable-libx264`  for anything else installed above. This may take a REALLY long time, so be patient.

	cd /usr/src
	git clone https://github.com/FFmpeg/FFmpeg.git
	cd ffmpeg
	sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
	make
	sudo make install