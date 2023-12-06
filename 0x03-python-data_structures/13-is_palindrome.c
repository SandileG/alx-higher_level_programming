#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *temp;
	int count, i;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;
	count = 0;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		count++;
	}

	prev = NULL;
	temp = slow;

	while (temp != NULL)
	{
		temp = temp->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	temp = prev;
	slow = *head;

	for (i = 0; i < count; i++)
	{
		if (slow->n != temp->n)
			return (0);

		slow = slow->next;
		temp = temp->next;
	}

	return (1);
}
