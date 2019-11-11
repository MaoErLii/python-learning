# Concept of Python Variables

## A variable in Python represents an entity whose value can change as and when reqired. Conceprually, it is a memory location whice holds the actual valu

## some key facts about Python variables

    ```
      1. Variables don't require decalration, but you must initialize them before use.

      2. example 
          test = 10

          * creation of an object to represent the value 10.
          * if the variable (test) doesn't exist, then it'll get created.
          * Association of the variable with the object, so that it can refer the value.

      3. whenever the expression changes, Python associates a new object (a chunk of memory) to the variable for referencing that value. And the old one goes to the garbage collector.

      4. Python builds a cache and reuses some of the immutable objects, such as small integers and strings

      5. An object is just a region of memory which can hold the following

          * the actual object values.
          * A type designator to reflect the object type
          * The reference counter which determines when it's OK to reclaim the object

      6. An object is just a region of memory which can hold the following

    ```
