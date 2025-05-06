# Installation

## Stable release

To install My First PH3 Package, run this command in your terminal:

```console
$ pip install my-first-ph3-package
```

This is the preferred method to install My First PH3 Package, as it will always install the most recent stable release.

If you don't have [pip] installed, this [Python installation guide] can guide
you through the process.

````{note}
If you want to use My First PH3 Package as a dependency in a UV-managed project, add it with
```console
$ uv add my-first-ph3-package
```
````

## From sources

The sources for My First PH3 Package can be downloaded from the [Github repo].

You can either clone the public repository:

```console
$ git clone git://github.com/balouf/my-first-ph3-package
```

Or download the [tarball]:

```console
$ curl -OJL https://github.com/balouf/my-first-ph3-package/tarball/main
```

Once you have a copy of the source, you can install it from the package directory with:

```console
$ pip install .
```

[github repo]: https://github.com/balouf/my-first-ph3-package
[pip]: https://pip.pypa.io
[python installation guide]: http://docs.python-guide.org/en/latest/starting/installation/
[tarball]: https://github.com/balouf/my-first-ph3-package/tarball/main
