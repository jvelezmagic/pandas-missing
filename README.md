Pandas missing
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

``` bash
pip install pandas-missing
```

or

``` bash
conda install --channel jvelezmagic pandas_missing
```

## How to use

``` python
import pandas as pd
import pandas_missing
```

``` python
df = pd.DataFrame.from_dict(
    {
        "number": range(0, 15)
    }
)

df.iloc[3:6, :] = None

df
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>

``` python
df.missing.number_missing()
```

    3

``` python
df.missing.number_complete()
```

    12
