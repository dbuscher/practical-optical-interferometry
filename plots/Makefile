# Make all the PDF files in this directory
SOURCE=$(shell cat PlotFiles.txt)
PDF_FILES=$(SOURCE:.py=.pdf)
TARGETS=$(PDF_FILES) phase-information.DONE

all : $(TARGETS)

%.pdf : %.py
	python3 $<  $@

# Hack for one python file which produces multiple plots
phase-information.DONE : phase-information.py
	python3 $<  && touch $@ 

clean :
	rm -f *.pdf *.DONE
