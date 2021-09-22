# FormData
## _Python package for data conversion_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://www.facebook.com/AgesXpat)
FormData is a data convertion programme written using Python Programming Language.
### _Converts from:_   
- JSON to CSV
- CSV to JSON
- And more coming soon

## Installation

```sh
pip install formdata
```

#### Sample Code

Basic usage:

```sh
import Formdata
data = FormData(obj="json")
print(data.json_csv)
```
'[{"csv": [{"a": "1", " b": "2", "c": "3", " c": "4"}, {"a": "1", " b": "2", "c": "3", " c": "4"}, {"a": "1", " b": "2", "c": "3", " c": "4"}, {"a": "1", " b": "2", "c": "3", " c": "4"}, {"a": "5", " b": "6", "c": "7", " c": "8"}, {"a": "5", " b": "6", "c": "7", " c": "8"}, {"a": "5", " b": "6", "c": "7", " c": "8"}, {"a": "5", " b": "6", "c": "7", " c": "8"}, {"a": "9", " b": "10", "c": "11", " c": "12"}, {"a": "9", " b": "10", "c": "11", " c": "12"}, {"a": "9", " b": "10", "c": "11", " c": "12"}, {"a": "9", " b": "10", "c": "11", " c": "12"}]}]'

```sh
import Formdata
data = FormData(obj="csv")
print(data.csv_json)
```
'
('a', ' b', 'c', ' c')
('9', '10', '11', '12')
('a', ' b', 'c', ' c')
('9', '10', '11', '12')
'
## License
MIT
