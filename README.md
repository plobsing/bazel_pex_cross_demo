# Bazel rules_py PEX cross-compilation demo

This is a demonstration of using `py_pex_binary` Bazel rule to build [PEX executables](https://pypi.org/project/pex/)
explicitly targetting specific OSes and architectures (cross-compilation).

## Targets

### :example_bin

`py_binary` lacking any specific cross-compilation provisions. Can be invoked to execute the toy application.

```
bazel run :example_bin
```

### :example_pex

`py_pex_binary` lacking any specific cross-compilation provisions. Can be built to create a PEX bundle targetting the build host's environment.

```
bazel build :example_pex
```

NOTE: PEX bundle is compatible with the Bazel Python interpreter, its version checks may reject the system Python interpreters.
In such situations, it can still be invoked using `bazel run @rules_python//python/bin:python -- $(pwd)/bazel-bin/example_pex.pex`.

### :example_pex_OS_ARCH

`py_pex_binary` targetting a specific operating system and CPU architecture. Builds for `linux_x86`, `linux_arm`, and `macos_arm` work;
the build for `windows_x86` is non-functional due to https://github.com/aspect-build/rules_py/issues/625.

## Patches

A patch to `aspect_rules_py` is required for cross-compilation to work at all:
https://github.com/aspect-build/rules_py/pull/618 .

## Working with the PDM lockfile

The PDM tool has been mapped into this Bazel repo (for Linux/x86 only).
This enables updating the lockfile using the command:

```
bazel run @pdm -- lock --static-urls
```
