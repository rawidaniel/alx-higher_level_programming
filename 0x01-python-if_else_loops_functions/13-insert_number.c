#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inset a new node into sorted singly linked list
 * @head: pointer to pointer of the first node of listint_t list
 * @number: integer to ne included in new node
 *
 * Return: address of the new node or NULL if it fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *prev, *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		free(node);
		return (NULL);
	}
	node->n = number;
	temp = *head;
	while (temp && number > temp->n)
	{
		prev = temp;
		temp = temp->next;
	}

	prev->next = node;
	node->next = temp;

	return (node);
}
