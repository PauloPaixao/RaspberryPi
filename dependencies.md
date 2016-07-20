# Camera Project


## Linux File-watcher

Checking the files with Filewatcher.
In Ubuntu inotifywait is provided by the inotify-tools package.


	inotifywait -m /camera -e create -e moved_to |
		while read path action file; do
			echo "The file '$file' appeared in directory '$path' via '$action'"
			# do something with the file
		done

## Camera Stream

The video steam can be found in the URL.
 
	http://145.132.122.80:64672/mjpg/video.mjpg

Download the stream to MP4

	ffmpeg -y -i http://pssp:xptoxpto@145.132.122.80:64672/mjpg/video.mjpg  paulo.mp4

	ffmpeg -y -i http://pssp:xptoxpto@145.132.122.80:64672/mjpg/video.mjpg -vframe 1 img%03d.jpg 


Converting stream to images (jpg) every 2 seconds.

	ffmpeg -y -i http://pssp:xptoxpto@145.132.122.80:64672/mjpg/video.mjpg -vf fps=1/2 img%03d.jpg


## Examples

How to execute ffmpeg.

	ffmpeg  \
		-y \
		-timeout 5000000 \
		-map 0:0 \
		-an \
		-sn \
		-f md5 - \
		-headers "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36" \
		-headers "X-Forwarded-For: 13.14.15.66" \
		-i "http://127.0.0.1:8080/some_video_file.mp4" \
		-v trace

Repeat command every second.

	while sleep 1; do echo "Hi"; done

Repeat last 10 files every second.

	while sleep 1; clear; do ls -1t | head -10; done


## Image Magick 

Threshold

	convert -density 150 -threshold 10% img006.jpg th006a.jpg

IP Address show in Linux 

	ip addr show


## Linux apt-get dependencies 

Linux dependencies can be installing running the following commands.

Watcher for folder

	sudo apt-get install inotify-tools


## FFMPEG ##

How to process videos

	sudo apt-get install ffmpeg 

Installing FFMpeg on Raspbian. Installing H264 Support
Run the following commands, one at a time.

	cd /usr/src
	git clone https://github.com/FFmpeg/FFmpeg.git
	cd ffmpeg
	sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
	make
	sudo make install

Install FFMPEG. Add lines similar to the `--enable-libx264`  for anything else installed above. This may take a REALLY long time, so be patient.

	cd /usr/src
	git clone https://github.com/FFmpeg/FFmpeg.git
	cd ffmpeg
	sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
	make
	sudo make install

## Image Magick##

	sudo apt-get install imagemagick

Python and Python pip

	sudo apt-get install python-pip

Python libraries 

	pip install imutils
	pip install numpy

Detailed instructions for Raspberry Pi.

- http://robertcastle.com/2014/02/installing-opencv-on-a-raspberry-pi/
- [http://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/](http://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/ "http://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/")



Install OpenCV

	cd $HOME
	mkdir opencv_src
	cd opencv_src/
	git clone https://github.com/Itseez/opencv.git
	cd opencv/
	mkdir release
	cd release/
	cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
	make
	sudo make install



