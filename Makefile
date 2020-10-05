DEST_SRC_DIR    ?= dist_src
DEST_DIR   		?= dist
VERSION			?= $(shell cat VERSION)

build: clean
	@echo "=====Build======"
	git pull
	./create_deb.sh

install: build
	@echo "=====Install======"
	sudo gdebi --non-interactive dist/rpi-ac-control_$(VERSION)_all.deb 

run_test:
	@echo "=====Test======"
	python3 -m pytest -v test/test_rpi_ac_control.py

clean_install_test: purge install run_test

purge:
	@echo "=====Purge======"
	sudo apt purge -y rpi-ac-control || true

clean:
	@echo "=====Clean======"
	rm -rf $(DEST_DIR)
	rm -rf $(DEST_SRC_DIR)
