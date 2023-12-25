# Use the official Ubuntu base image
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git

# Copy the CMake project files into the container
RUN git clone --recurse-submodules https://github.com/xR3b0rn/dbcppp.git /app
# Set working directory
WORKDIR /app
RUN git checkout v3.2.6

# Build the CMake project
RUN mkdir build && cd build && cmake .. && make -j && make install && ldconfig

# Cleanup unnecessary packages and files
RUN apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /app

# Set an entrypoint if needed
# ENTRYPOINT ["executable"]

# Set default command if needed
# CMD ["command"]
