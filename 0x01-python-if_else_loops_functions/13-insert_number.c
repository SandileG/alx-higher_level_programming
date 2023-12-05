#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in the new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
	return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	current = *head;
	prev = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	new->next = current;
	if (prev != NULL)
		prev->next = new;
	else
		*head = new;

	return (new);
}
