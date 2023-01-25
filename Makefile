VER=$(shell grep __version__ phdseeker/constants.py|cut -d= -f2|tr -d '\" ')

.ONESHELL:

ver:
	@echo phdseeker ver. $(VER)

setup: ver
	python setup.py sdist
	python setup.py bdist_wheel

lins: ver
	python setup.py install

pins: ver
	pip install phdseeker==$(VER)

upypi: setup
	twine upload "dist/phdseeker-$(VER).tar.gz"

utest: setup
	twine upload -r testpypi "dist/phdseeker-$(VER).tar.gz"

upload: setup upypi utest

clean: ver
	@rm phdseeker.egg-info/ -rfv
	@rm build/ -rfv
	@rm dist/ -rfv
	@rm phdseeker*.spec -rfv
	@rm PhD_Positions_*csv PhD_Positions_*xlsx -rfv
