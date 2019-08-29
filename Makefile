DOCKER_IMAGES = $(shell docker images -q navigator)

all: run

.PHONY: build
build: ## Build project
	@docker build --tag=navigator .

.PHONY: run
run:  ## Run the navigator
ifeq ($(strip $(DOCKER_IMAGES)),)
	@make build
endif
	@docker run --rm -it navigator navigate

test: ## Run tests
	@find . -name \*.pyc -delete
	@docker run -it --rm navigator python setup.py test
