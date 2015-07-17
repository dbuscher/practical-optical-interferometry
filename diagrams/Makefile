# Make all the PDF files in this directory
SOURCE=$(wildcard *.svg)
PDF_FILES=$(SOURCE:.svg=.pdf)
TARGETS=$(PDF_FILES)

all : $(TARGETS)

clean :
	rm -f *.pdf *.DONE

# Need to convert to eps first in order to overcome transparency issues
%.pdf : %.svg
	inkscape --export-area-drawing -f $*.svg --export-eps=$*-tmp.eps
	epstopdf $*-tmp.eps --outfile=$*.pdf
	rm -f $*-tmp.eps
