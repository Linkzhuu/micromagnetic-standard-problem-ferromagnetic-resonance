all: unit-tests

unit-tests:
	make -C tests/unit_tests/

reproduce-figures:
	make -C tests/reproduce_figures/

.PHONY: all unit-tests
