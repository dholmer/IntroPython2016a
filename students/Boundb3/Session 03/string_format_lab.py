'''
TO DO : this is the string formating lab assignment

A couple Exercises
Write a format string that will take:

( 2, 123.4567, 10000)

and produce:

'file_002 :   123.46, 1e+04'
Rewrite: "the first 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an arbitrary number of values
Trick: You can pass in a tuple of values to a function with a *:

.. code-block:: ipython
In [52]: t = (1,2,3)

In [53]: �the first 3 numbers are: {:d}, {:d}, {:d}�.format(* t) Out[53]: �the first 3 numbers are: 1, 2, 3�


bonus = Fun with strings
Rewrite: the first 3 numbers are: %i, %i, %i"%(1,2,3)

for an arbitrary number of numbers...(from chapter 4 from class slides


'''