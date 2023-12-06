#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the head of the linked list.
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int values[10000] ;
	int count = 0;

	if (*head == NULL)
		return (1);

	while (current != NULL)
	{
		values[count] = current->n;
		current = current->next;
		count++;
	}

	for (int i = 0; i < count / 2; i++)
	{
		if (values[i] != values[count - i - 1])
			return (0);
	}

	return (1);
}
