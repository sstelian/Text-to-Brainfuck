This project takes a string and generates Brainfuck source code that outputs that string. The brainfuck_generator
module can be run standalone, in which case it expects a string and an output file to be given as command line
arguments. If no file is given, it outputs to console.

Unit tests are based on Pytest and use a Brainfuck interpreter written by Sebastian Kaspari.
    https://github.com/pocmo/Python-Brainfuck

The project was developed by Stelian Saracut in 2018 as a programming exercise for both Brainfuck and Python.