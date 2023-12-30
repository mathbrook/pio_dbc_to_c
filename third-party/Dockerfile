# Use the official Ubuntu base image
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    make \
    git

# Copy the CMake project files into the container
RUN git clone https://github.com/howerj/dbcc.git /app
# Set working directory
WORKDIR /app

# Build the CMake project
RUN make
# RUN cmake --build build --config release
# Cleanup unnecessary packages and files
RUN apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set an entrypoint if needed
# ENTRYPOINT ["executable"]
RUN mkdir -p /out/lib && chmod -R 777 /out/lib
RUN chown -R 1000:1000 /out/lib

VOLUME /out

# Set default command if needed
# CMD ["command"]
