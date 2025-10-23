Usage
=====
Acknowledgements
----------------

LHMP is being developed in collaboration with NASA Langley Research Center and the Hampton University.


Copyright
---------

.. include:: ../LICENSE


Configuring the Raspberry Pi
----------------------------

This section summarizes the steps required to setup the environment needed to run a GigE Vision (i.e., genicam) camera on a Raspberry Pi 4b. Here we use a Pheonix 5.0 Polarization camera (LUCID Vision Labs Inc., 2023) that is built around Sony's IMX250MYR CMOS.

Hardware Requirements
	1) Any GigE vision camera should work however it must be a GenICam compliant machine vision camera/device. 
		a) Power supply.
	
	2) Rasberry Pi 4b running Debian GNU/Linux 12 (bookworm) x64. Prefer remote connection with Raspberry Pi Connect. 
		a) Power supply.
	
	3) Ethernet Cable.

Setup Hardware
	a) Connect camera to Raspberry Pi via ethernet cable.

	b) Power Raspberry Pi.

Install ArenaSDK Software (ArenaSDK_v0.1.78_Linux_ARM64)
	**Note**: Full details in 'README_ARM64.txt'

	a) Set jumbo frames
		$ sudo ip link set enp0s8 mtu 9000

	b) Set receive buffers
		$ sudo ethtool -g enp0s8
		$ sudo ethtool -G enp0s8 rx 4096

	c) Set socket buffer size
		$ sudo sh -c "echo 'net.core.rmem_default=33554432' >> /etc/sysctl.conf"
		$ sudo sh -c "echo 'net.core.rmem_max=33554432' >> /etc/sysctl.conf"
		$ sudo sysctl -p
	d) Reverse path filtering
		$ sudo sh -c "echo 'net.core.rmem_default=33554432' >> /etc/sysctl.conf"
		$ sudo sh -c "echo 'net.core.rmem_max=33554432' >> /etc/sysctl.conf"
		$ sudo sysctl -p

	e) Extract the tarball to your desired location:	
	    $ tar -xvzf ArenaSDK_Linux_ARM64.tar.gz
	    
	f) Run the ArenaSDK_Linux_ARM64.conf file	
	    $ cd ~/Documents/ArenaSDK_v0.1.78_Linux_ARM64/ArenaSDK_Linux_ARM64
	    $ sudo sh Arena_SDK_ARM64.conf

Install ImpactAcquire
	a) Download latest version of ImpactAcquire-arm64-linux-X.X.X.sh from dhttp://static.matrix-vision.com/mvIMPACT_Acquire/
	
	b) Place ImpactAcquire-arm64-linux-X.X.X.sh in '~/.'
	
	c) Install.
		$ cd ~/
		$ ./ImpactAcquire-arm64-linux-X.X.X.sh


Install Harvesters
	a) Setup virtual environment.
		$ python3 -m venv myvirtualenv

	b) Activate virtual environment.
		$ source ~/myvirtualenv/bin/activate

	c) Install Harvesters.
		$ pip install harvesters

	d) Install standard openCV.
		$ pip install opencv-python

Run programs in Harvesters
	a) Activate virtual environment.
		$ source ~/myvirtualenv/bin/activate

	b) Set appropriate directory with python scripts.
		$ cd ~/Documents

	c) Run desired python script.
		$ python3 TestSample.py

Instructions for building sphinx documentation locally
------------------------------------------------------

This section describes howw to build the sphinx documentation locally. 

	a) Setup virtual environment.
		$ python3 -m venv myvirtualenv

	b) Activate virtual environment.
		$ source ~/myvirtualenv/bin/activate

	c) Install Harvesters.
		$ pip install harvesters

	d) Install standard openCV.
		$ pip install opencv-python

	e) Install matplotlib.
		$ pip install matplotlib

	f) Install basic sphinx package.
		$ pip install sphinx

	g) Install html theme for sphinx.
		$ pip install sphinx_rtd_theme

	h) Install pdf builder for sphinx.
		$ pip install sphinx-simplepdf

	i) Build sphinx
		$ sphinx-build -M html source docs	

Test the instrument functionality 
---------------------------------

.. autofunction:: TestSample.Run

Basic function for capturing samples with the LHMP
--------------------------------------------------

.. autofunction:: CaptureSample.Run

