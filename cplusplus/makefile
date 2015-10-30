#file:GNUMakefile

all:foo

foo:foo.o
	g++ foo.o -g -o foo

foo.o: foo.cc foo.h
	g++ -O2 -g -c foo.cc -o foo.o

clean:
	rm -f foo.o
	rm -f foo

#end of file