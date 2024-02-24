.PHONY: install uninstall build upload-test upload


install: ssmi.py
	@echo Installing ssmi ...
	@install -d /usr/bin
	@install -m 755 ssmi.py /usr/bin/ssmi
	@install -d /usr/share/man/man1
	@install -m 644 ssmi.1 /usr/share/man/man1/
	@echo Successfuly installed

uninstall:
	@echo Uninstalling ssmi ...
	@rm -f /usr/bin/ssmi
	@rm -f /usr/share/man/man1/ssmi.1
	@echo Successfuly uninstalled

build:
	python setup.py sdist bdist_wheel

upload-test:
	python -m twine upload --repository testpypi dist/* --verbose

upload:
	python -m twine upload dist/*
