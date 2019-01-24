import os.path
import pandas as pd
pkgdir = os.path.dirname(__file__)

# Jhonson & Jhonson
jj = pd.read_csv(f'{pkgdir}/data/jj.csv', index_col=0, parse_dates=True)
jj.index = jj.index.to_period("Q")

# Global temperatures
globaltemp = pd.read_csv(f'{pkgdir}/data/globaltemp.csv', index_col=0, 
                            parse_dates=True)

# CO2
co2 = pd.read_csv(f'{pkgdir}/data/co2.csv', index_col=0, parse_dates=True)
co2.index = co2.index.to_period("M")

# Air Passengers
airpassengers = pd.read_csv(f'{pkgdir}/data/airpassengers.csv', index_col=0, 
                    parse_dates=True)
airpassengers.index = airpassengers.index.to_period("M")

# US Change
uschange = pd.read_csv(f'{pkgdir}/data/uschange.csv', index_col=0, 
                    parse_dates=True)
uschange.index = uschange.index.to_period("Q")

# H02
h02 = pd.read_csv(f'{pkgdir}/data/h02.csv', index_col=0, 
                    parse_dates=True)
h02.index = h02.index.to_period("M")