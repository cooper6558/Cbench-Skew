# Cbench-Skew
Compute and plot histogram for Cbench hdf5 output files.

## Method 1
Run Stage 1, computing the histogram and writing to a file.
Then run Stage 2, reading the histogram and plotting it.
```shell
> python -m cbench_skew.stage1 \
      --input data/test.hdf5 \
      --dataset default --bins 20 \
      --output data/histogram.npy

> python -m cbench_skew.stage2 \
      --input data/histogram.npy
```

## Method 2
Run everything at once, bypassing histogram-to-disk.
```shell
> python -m cbench_skew \
      --input data/test.hdf5 \
      --dataset default --bins 20
```

## Method 3
Run the package in a Python script, again bypassing histogram-to-disk.
```python
from cbench_skew.stage1 import hist
from cbench_skew.stage2 import plot


plot(hist('data/test.hdf5', 'default', 20))
```

## Method 4
There is a scheduling script you can use. Right now it just prints the
commands it would run.
```shell
> python -m cbench_skew.schedule --script data/jobs.json
```
