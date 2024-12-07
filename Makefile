ttc: apply_gsub otf2ttf build
	otf2otc simsun.ttf nsimsun.ttf -o simsun.ttc
	otf2otc simsunbd.ttf nsimsunbd.ttf -o simsunbd.ttc
	otf2otc simsunl.ttf nsimsunl.ttf -o simsunl.ttc
	make clean

apply_gsub:
	python3 apply_gsub.py

otf2ttf:
	otf2ttf SourceHanSerifSC-Regular.otf -o SourceHanSerifSC-Regular.ttf
	otf2ttf SourceHanSerifSC-Light.otf -o SourceHanSerifSC-Light.ttf
	otf2ttf SourceHanSerifSC-Bold.otf -o SourceHanSerifSC-Bold.ttf
	otf2ttf SourceHanSerifHWSC-Regular.otf -o SourceHanSerifHWSC-Regular.ttf
	otf2ttf SourceHanSerifHWSC-Light.otf -o SourceHanSerifHWSC-Light.ttf
	otf2ttf SourceHanSerifHWSC-Bold.otf -o SourceHanSerifHWSC-Bold.ttf

build:
	python3 build.py

clean:
	rm simsun*.ttf nsimsun*.ttf