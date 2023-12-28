#include "cpython.h"


/**
 * print_python_bytes - Prints information about bytes objects.
 * @p: Pointer to a PyObject (Python bytes)
 */
void print_python_bytes(PyObject *p)
{
	/* Check if p is a valid PyBytesObject */
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Get the size of the bytes object */
	Py_ssize_t size = PyBytes_Size(p);

	/* Print bytes object information */
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	/* Attempt to print the first 10 bytes */
	printf("  trying string: %s\n", PyBytes_AsString(p));

	/* Print the first 10 bytes */
	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
	{
		printf("%02x ", PyBytes_AsString(p)[i] & 0xFF);
	}
	printf("\n");
}
