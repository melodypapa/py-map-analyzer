# 1. Map Reporter

## 1.1. Introduce

The utility to generate the report for Greenhill (GHS) map file

### 1.1.1. How to create the distribution and upload to pypi
1. Run `python setup.py bdist_wheel` to generate distribution
2. Run `twine check dist/*` to check the validation of distribution
3. Run `twine upload dist/*` to upload to pypi repository
4. Check the website https://pypi.org/project/armodel/ to find out it works or not

And more details can be found at https://packaging.python.org/  

### 1.1.2. Unit test

Run `pip install pytest pytest-cov` to install pytest.

Run `pytest --cov=py_tresos --cov-report term-missing` to verify all the functionality.

## 1.2. CLI

```
map-analyzer -c toml/ghs.toml -m map/ghs/ghs.map --excel ghs.xlsx
```

## 1.3. Change notes

**0.1.0**

1. Parse the green-hill map format.
2. Collect the .a file as the module.
3. Export the report into xlsx file.
