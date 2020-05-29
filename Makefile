# Including commands
start-program:
	poetry run task start

.PHONY: run
run:
	@make -j 3 start-program