## Proof of Concept -- Plugins

This is an example of a way one could write a program that's easily extendable 
through modules that abide by a simple API.

Basically, the `main` class iterates through the `plugins` folder, and tries 
to load every module it finds. If a module is successfully loaded, it calls 
a `register()` function, which is defined in each module's `__init__` file. 
This function returns two values, a `name` and a function which serves as the 
module's entry point.

The way this is written, you would access the plugin `plug1` by calling:

```
python3 main.py plug1
```

Anything following the name of the module will be passed into the module's 
entry point as an array.

The `utils.py` file contains, for example, functions that may be used by the 
core functionality of the module, but may also be used by the plugins (see the 
`plug2.py` file's successful call to `utils.py`).

One (potentially big) downside -- just as `utils.py` can be accessed by the 
plugin, in this implementation *any* code in the main program can be accessed 
by the plugin. This seems potentially dangerous, though that may be a risk you 
take when using plugins: only use ones you trust! At the moment, I'm not sure 
exactly how to isolate what code the plugins have access to. That would be the 
ideal!
