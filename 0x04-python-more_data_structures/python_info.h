#ifndef PYHTON_INFO_H
#define PYTHON_INFO_H

#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/* Function declarations */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

#endif /* PYHTON_INFO_H */
