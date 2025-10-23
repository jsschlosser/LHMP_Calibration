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
	.. code-block:: console

		$ sudo ip link set enp0s8 mtu 9000

	b) Set receive buffers
	.. code-block:: console

		$ sudo ethtool -g enp0s8
		$ sudo ethtool -G enp0s8 rx 4096

	c) Set socket buffer size
	.. code-block:: console

		$ sudo sh -c "echo 'net.core.rmem_default=33554432' >> /etc/sysctl.conf"
		$ sudo sh -c "echo 'net.core.rmem_max=33554432' >> /etc/sysctl.conf"
		$ sudo sysctl -p
		
	d) Reverse path filtering
	.. code-block:: console

		$ sudo sh -c "echo 'net.core.rmem_default=33554432' >> /etc/sysctl.conf"
		$ sudo sh -c "echo 'net.core.rmem_max=33554432' >> /etc/sysctl.conf"
		$ sudo sysctl -p

	e) Extract the tarball to your desired location:	
	.. code-block:: console

	    $ tar -xvzf ArenaSDK_Linux_ARM64.tar.gz
	    
	f) Run the ArenaSDK_Linux_ARM64.conf file	
	.. code-block:: console

	    $ cd ~/Documents/ArenaSDK_v0.1.78_Linux_ARM64/ArenaSDK_Linux_ARM64
	    $ sudo sh Arena_SDK_ARM64.conf

Install ImpactAcquire
	a) Download latest version of ImpactAcquire-arm64-linux-X.X.X.sh from dhttp://static.matrix-vision.com/mvIMPACT_Acquire/
	
	b) Place ImpactAcquire-arm64-linux-X.X.X.sh in '~/.'
	
	c) Install.
		.. code-block:: console

		$ cd ~/
		$ ./ImpactAcquire-arm64-linux-X.X.X.sh


Install Harvesters
	a) Setup virtual environment.
	.. code-block:: console

		$ python3 -m venv myvirtualenv

	b) Activate virtual environment.
	.. code-block:: console

		$ source ~/myvirtualenv/bin/activate

	c) Install Harvesters.
	.. code-block:: console

		$ pip install harvesters

	d) Install standard openCV.
	.. code-block:: console

		$ pip install opencv-python

Run programs in Harvesters
	a) Activate virtual environment.
	.. code-block:: console

		$ source ~/myvirtualenv/bin/activate

	b) Set appropriate directory with python scripts.
	.. code-block:: console

		$ cd ~/Documents

	c) Run desired python script.
	.. code-block:: console

		$ python3 TestSample.py

Instructions for building sphinx documentation locally
------------------------------------------------------

This section describes howw to build the sphinx documentation locally. 

	a) Setup virtual environment.
	.. code-block:: console

		$ python3 -m venv myvirtualenv

	b) Activate virtual environment.
	.. code-block:: console

		$ source ~/myvirtualenv/bin/activate

	c) Install Harvesters.
	.. code-block:: console

		$ pip install harvesters

	d) Install standard openCV.
	.. code-block:: console

		$ pip install opencv-python

	e) Install matplotlib.
	.. code-block:: console

		$ pip install matplotlib

	f) Install basic sphinx package.
	.. code-block:: console

		$ pip install sphinx

	g) Install html theme for sphinx.
	.. code-block:: console

		$ pip install sphinx_rtd_theme

	h) Install pdf builder for sphinx.
	.. code-block:: console

		$ pip install sphinx-simplepdf

	i) Build sphinx.
	.. code-block:: console

		$ sphinx-build -b html source docs

Test the instrument functionality 
---------------------------------

.. autofunction:: TestSample.Run

Basic function for capturing samples with the LHMP
--------------------------------------------------

.. autofunction:: CaptureSample.Run

