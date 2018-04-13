FROM tensorflow/tensorflow:1.5.0

RUN apt-get update && apt-get install -y \
    python-pip \
    cython \
    git \
    libsm6 \
    libxext6 \
    libxrender-dev \
    wget

RUN cd "/" && \
    wget -nv "https://pjreddie.com/media/files/yolo.weights"

RUN pip install opencv-python

RUN cd "/" && \
    git clone https://github.com/thtrieu/darkflow.git &&\
    cd darkflow && \
    pip install . 
