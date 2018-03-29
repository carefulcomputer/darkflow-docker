FROM tensorflow/tensorflow
RUN apt-get update && apt-get install -y \
	python-pip \
	cython \
	git \
	libsm6 \
	libxext6 \
	libxrender-dev \
	wget
RUN pip install opencv-python

RUN cd "/" && \
	git clone https://github.com/thtrieu/darkflow.git &&\
	cd darkflow && \
	pip uninstall --yes tensorflow && \
	pip install tensorflow==1.5 && \
	pip install . && \
	cd "/" && \
	rm -rf darkflow
