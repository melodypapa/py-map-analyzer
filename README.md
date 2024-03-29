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
map-analyzer -c toml/meths.toml -m map/ghs/ghs.map --excel ghs.xlsx
```

```
map-analyzer -c toml/propa.toml -m map/ghs/propa.map --excel propa.xlsx
```

## 1.3. Change notes

**0.1.0**

1. Parse the green-hill map format.
2. Collect the .a file as the module.
3. Export the report into xlsx file.


**0.1.1**

1. Add the supporting of NXP G32G GCC map format.
2. Read the memory section in the GHS map format.
3. Add the ROM/RAM/Calibration attribute for the memory section.
4. Output the memory section in the excel file.

**0.2.1**

1. Add the section report.
2. Add the section summary.