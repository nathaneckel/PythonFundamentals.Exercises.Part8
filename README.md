# Part 8

## Accompanying resources
* Slide deck: https://zipcoder.github.io/reveal-slides.data-engineering/zcw_content/python/fundamentals-part8.html

## Exercise 1

### Prep work

Create a file in the same directory as this file. Change permissions so that the file is not accessible. 
```
touch locked_out_file.txt
chmod 000 locked_out_file.txt
```

### Part A 

* Open the program *file_reader.py*.
* Carefully read through the comments and the code.

### Part B

* Open the test class *test_file_reader.py*.
* Execute each test in debug mode to reinforce the flow of each scenario.



## Exercise 2

Create a program called *tree.py*

Given a file path (absolute or relative), the program should write to a file all of the contents of the directory and the child directories bellow it.
The output file should look something like this:

```python
./file1.py
./file2.py
./dir1/file1_in_dir1.txt
./dir1/file2_in_dir1.txt
./dir3/file1_in_dir3.txt
```
