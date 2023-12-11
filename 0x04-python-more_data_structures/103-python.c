#include "python_info.h"

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *element;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

		if (strcmp(Py_TYPE(element)->tp_name, "bytes") == 0)
		print_python_bytes(element);
	}
}

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	unsigned char *buffer;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	buffer = (unsigned char *)PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", buffer);
	printf("  first 10 bytes: ");

	for (i = 0; i < size && i < 10; i++)
		printf("%02x ", buffer[i]);
	printf("\n");
}
