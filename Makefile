PWD := $(shell pwd)

all:
	gcc -lzmq server.c -o server
	gcc -lzmq client.c -o client
clean:
	rm client server
