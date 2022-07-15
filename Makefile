ttc: build
	otf2otc simsun.ttf nsimsun.ttf -o simsun.ttc
	otf2otc simsunbd.ttf nsimsunbd.ttf -o simsunbd.ttc
	otf2otc simsunl.ttf nsimsunl.ttf -o simsunl.ttc
	make clean

build:
	python3 build.py

clean:
	rm simsun*.ttf nsimsun*.ttf