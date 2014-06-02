PROJECT=yundong
TAR=tar -cjf

TARNAME=$(PROJECT)-`date "+%Y.%m.%d"`.tar.bz2

CLEANFILES +=     \
	mainwindow.py

all: mainwindow.ui
	pyside-uic mainwindow.ui -o mainwindow.py

clean:
	rm -f $(CLEANFILES)
	rm -rf __pycache__
	find . -name "*.pyc" -delete

dist: clean
	cd .. && $(TAR) /tmp/$(TARNAME) $(PROJECT)
	mv /tmp/$(TARNAME) .
