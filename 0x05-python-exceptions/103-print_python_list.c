#include "cpython.h"

/**
 * print_python_list - Prints information about lists.
 * @p: Pointer to a PyObject (Python list)
 */
void print_python_list(PyObject *p)
{
	/* Check if p is a valid PyListObject */
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	/* Get the size and allocated space of the list */
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	/* Print list information */
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	/* Iterate through each element of the list */
	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *element = PyList_GetItem(p, i);
		/* Check if element is not NULL before accessing tp_name */
		if (element != NULL)
		{
			/* Print information about the element */
			printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		}
		else
		{
			fprintf(stderr, "[ERROR] Failed to get list element at index %ld\n", i);
		}
	}
}
