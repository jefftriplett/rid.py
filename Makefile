.PHONY: git_push
git_push:
	git push origin --all


.PHONY: pypi
pypi:
	python setup.py sdist bdist_wheel


.PHONY: pypi_upload
pypi_upload:
	python setup.py sdist bdist_wheel upload
