#!/usr/bin/env python3
import numpy as np
from psrdada import Reader

# Create a reader instace
reader = Reader()

# Connect to a running ringbuffer with key 'dada'
reader.connect(0xdada)

# loop over the pages until EOD is encountered
while not reader.isEndOfData:
    # read the page as numpy array
    page = reader.getNextPage()

    data = np.asarray(page)
    print (np.sum(data))

    reader.markCleared()

reader.disconnect()