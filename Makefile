CONDA_ENV_PATH=$$(conda info --base)/envs/rl-playground

pre-commit:
	pre-commit run

pre-commit-all:
	pre-commit run --all-files

unittest:
	pytest test -s -v

tree:
	tree -I "*data|*save|.pkl|*.png|*.txt|$(shell cat .gitignore | tr -s '\n' '|' )"

init:
	conda env create -f environment.yaml --force
	mkdir -p ${CONDA_ENV_PATH}/etc/conda/activate.d
	mkdir -p ${CONDA_ENV_PATH}/etc/conda/deactivate.d
	cp scripts/set_conda_env_var.sh ${CONDA_ENV_PATH}/etc/conda/activate.d/
	cp scripts/unset_conda_env_var.sh ${CONDA_ENV_PATH}/etc/conda/deactivate.d/
	${CONDA_ENV_PATH}/bin/pip install -e .
	${CONDA_ENV_PATH}/bin/pre-commit install -f
