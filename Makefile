ttc: build
	otf2otc simsun.ttf nsimsun.ttf -o simsun.ttc
	otf2otc simsunbd.ttf nsimsunbd.ttf -o simsunbd.ttc
	rm simsun*.ttf nsimsun*.ttf

build:
	python3 build.py