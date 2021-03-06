[![Run Tests](https://github.com/acdh-oeaw/nerdpool-client/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/nerdpool-client/actions/workflows/test.yml) [![codecov](https://codecov.io/gh/acdh-oeaw/nerdpool-client/branch/master/graph/badge.svg?token=LXKIMGDXXF)](https://codecov.io/gh/acdh-oeaw/nerdpool-client) [![PyPI version](https://badge.fury.io/py/nerdpool-client.svg)](https://badge.fury.io/py/nerdpool-client)

# nerdpool-client

A Python client for downloading data from https://nerdpool-api.acdh-dev.oeaw.ac.at

## install

`pip install nerdpool_client`

## usage

### list data set titles


```python

from nerdpool_client import NerdPoolClient

client = NerdPoolClient()
print(client.data_sets)
# ['RTA', 'RITA', 'MRP', 'Chronik Aldersbach', 'DIPKO']
```

### download samples as .jsonl file

* go to [nerdpool-api](https://nerdpool-api.acdh-dev.oeaw.ac.at/) and create/filter you'r prefered data sample; e.g. all samples from MRP: 

```python

from nerdpool_client import NerdPoolClient

url = "https://nerdpool-api.acdh-dev.oeaw.ac.at/api/ner-sample/?format=json&ner_ent_type__contains=&ner_source__title=MRP"
client = NerdPoolClient()
client.dump_to_jsonl(url)
# 'out.jsonl'
```

### download samples as test.jsonl and eval.jsonl files

* With `file_name_prefix` you can add a custom prefix to the default file names `train.jsonl` and `eval.jsonl`
* The param `split` defines that each `split` sample should be saved into `eval.jsonl` and not into `train.jsonl`

```python
from nerdpool_client import NerdPoolClient

url = "https://nerdpool-api.acdh-dev.oeaw.ac.at/api/ner-sample/?format=json&ner_ent_type__contains=&ner_source__title=MRP"
client = NerdPoolClient()
client.dump_to_train_eval(url, file_name_prefix="mrp__", split=10)
# ['mrp__train.jsonl', 'mrp__eval.jsonl]
```