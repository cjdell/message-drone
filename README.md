Relay Drone
===========

Source code for entrant in UCLan Drone Hack 19th-20th September 2015

Setup
-----

Getting the code on to the Raspberry Pi:

	cd /home/pi

	git clone git@github.com:cjdell/message-drone.git

Create the DB:

	sqlite3 drone.db < provision.sql

The following bash commands are required to start camera and python services when the Raspberry Pi boots. These can be added to `/etc/rc.local`:

	sudo -u pi cvlc --no-audio v4l2:///dev/video0 --v4l2-width 848 --v4l2-height 480 --v4l2-chroma MJPG --v4l2-hflip 1 --v4l2-vflip 1 --sout '#standard{access=http{mime=multipart/x-mixed-replace;boundary=--7b3cc56e5f51db803f790dad720ed50a},mux=mpjpeg,dst=:8554/}' -I dummy &

	python /home/pi/message-drone/web.py &

