#include "cpython.h"


/**
 * print_python_float - Prints information about Python float objects
 * @p: Pointer to a PyObject (Python float)
 */
void print_python_float(PyObject *p)
{
	/* Check if p is a valid PyFloatObject */
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	/* Get the float value */
	double value = PyFloat_AsDouble(p);

	/* Print float object information */
	printf("[.] float object info\n");
	printf("  value: %lf\n", value);
}
