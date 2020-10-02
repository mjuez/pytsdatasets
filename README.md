# Python Time Series Datasets (pytsdatasets)

The **pytsdatasets** is a python package that provides some time series datasets available R distribution and in [**astsa**](https://github.com/nickpoison/astsa) R package.

Datasets are in **[pandas](https://pandas.pydata.org/) DataFrame** format.

This package could be useful for educational and/or scientific purposes.

## Author

- Mario Juez-Gil <[mariojg@ubu.es](mailto:mariojg@ubu.es)>
  Department of Computer Science - Universidad de Burgos - [ADMIRABLE Research Group](http://admirable-ubu.es/)

## Installation

This package can be installed using PIP.

```bash
pip install pytsdatasets
```

## Basic Usage

For example, loading `jj` dataset is as simple as:

```python
import pytsdatasets as tsds
tsds.jj.info()

# >> <class 'pandas.core.frame.DataFrame'>
#    PeriodIndex: 84 entries, 1960Q1 to 1980Q4
#    Freq: Q-DEC
#    Data columns (total 1 columns):
#     #   Column  Non-Null Count  Dtype
#    ---  ------  --------------  -----
#     0   data    84 non-null     float64
#    dtypes: float64(1)
#    memory usage: 1.3 KB
```

### Available datasets

The available datasets are:

- [airpassengers](https://www.rdocumentation.org/packages/datasets/versions/3.6.2/topics/AirPassengers): The classic Box & Jenkins airline data. Monthly totals of international airline passengers, 1949 to 1960.
- [co2](https://www.esrl.noaa.gov/gmd/ccgg/trends/): Monthly mean carbon dioxide (in ppm) measured at Mauna Loa Observatory, Hawaii.
- [globaltemp](http://data.giss.nasa.gov/gistemp/graphs/): Global mean land-ocean temperature deviations (from 1951-1980 average), measured in degrees
centigrade, for the years 1880-2015. This was an update of gtemp, but gtemp_land and gtemp_ocean
are the most recent updates.
- [jj](https://www.rdocumentation.org/packages/datasets/versions/3.6.2/topics/JohnsonJohnson): Johnson and Johnson quarterly earnings per share, 84 quarters (21 years) measured from the first
quarter of 1960 to the last quarter of 1980.
- [uschange](https://www.rdocumentation.org/packages/fpp2/versions/2.2/topics/uschange): Percentage changes in quarterly personal consumption expenditure, personal disposable income, production, savings and the unemployment rate for the US, 1960 to 2016.
- [h02](https://www.rdocumentation.org/packages/fpp/versions/0.5/topics/h02): Total monthly scripts for pharmaceutical products falling under ATC code H02, as recorded by the Australian Health Insurance Commission. Measured in millions of scripts.

## Contribute

Feel free to submit any pull requests 😊

## Acknowlegments

This work was supported by the pre-doctoral grant (EDU/1100/2017) of the Consejería de Educación of the Junta de Castilla y León, Spain, and the European Social Fund.

## License

This work is licensed under [GNU GPL v3](LICENSE).

## Citation policy

Please, cite this work as:

```
@software{pytsdatasets,
  author       = {Mario Juez-Gil},
  title        = {{mjuez/pytsdatasets}},
  month        = oct,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {v1.0},
  doi          = {10.5281/zenodo.4063496},
  url          = {https://doi.org/10.5281/zenodo.4063496}
}
```
