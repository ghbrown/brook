
#package specific stuff
PACKNAME=taylor
TESTDIR=tests

#useful general variables
VENV=test_venv
ACTIVATE=$(VENV)/bin/activate
VENVPIP=$(VENV)/bin/pip
SANDBOX=sbox/sandbox.py

#create/update virtual environment for testing
update-venv:
	@#operations in order:
	@#make virtual environment
	@#activate virtual environment
	@#install package to be tested in editable form (automatically gets dependencies)
	@#deactivate virtual environment
	@#all above directed to shell (necessary)
	@(\
	virtualenv $(VENV); \
	source $(ACTIVATE); \
	$(VENVPIP) install -e .; \
	deactivate; \
	)

#test using virtual environment
test:
	@#operations in order:
	@#activate virtual environment
	@#read/run scripts in order given by $(TESTDIR)/test_order.txt
	@#deactivate virtual environment
	@#all directed to shell (necessary)
	@(\
	source $(ACTIVATE); \
	while IFS='' read -r NAME; do \
		python $(TESTDIR)/$${NAME}; \
	done < $(TESTDIR)/test_order.txt; \
	deactivate; \
	)

#development sandbox for on the fly testing
sandbox:
	@(\
	source $(ACTIVATE); \
	python $(SANDBOX); \
	deactivate; \
	)

#print TODO notes to terminal
todo:
	@grep -r "TODO" $(PACKNAME) $(TESTDIR) README.md

#remove virtual environment
clean:
	@\rm -rf test_venv


#STEPS TO UPDATE PYTHON PACKAGE
# 1. bump version number
# 2. make sure dist is clear of old version(s) (move to old_dist)
# 3. $ python3 setup.py bdist_wheel
# 4. $ python -m twine upload dist/*

#For a full guide see DZone's "Build your first pip package"

