#include "lists.h"

/**
 * is_palindrome - determine if sigly linked list is palindrome
 * @head: pointer point to head of siglylinked list
 * Return: 1 if palindrone, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i = 0, size = 0;

	int array[10240];

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		size++;
	}

	if (size == 1)
		return (1);
	temp = *head;
	while (temp)
	{
		array[i] = temp->n;
		temp = temp->next;
		i++;
	}

	for (i = 0; i <= (size / 2); i++)
	{
		if (array[i] != array[size - 1 - i])
		{
			return (0);
		}
	}
	return (1);
}
