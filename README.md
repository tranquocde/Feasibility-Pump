

### Stand Alone
In order to find a feasible solution to a given 01MIP instance 
simply run
```
    fp.py -i instance
```

the extension of the instance file will drive the back-end library to 
use the correct loader. 

Available loaders can be obtained using:
```
    fp.py -l
```

To auto-generate json files to test, using :
```
    gen_test.py number_of_constraints
```
To run all the generated json files, using : 
```
    ./run.sh
```