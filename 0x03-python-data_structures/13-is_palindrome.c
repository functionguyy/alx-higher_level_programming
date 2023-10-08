#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the pointer of the list to be checked
 *
 * Return: 1 if is a palindrom, 0 if it is not a palindrome
 */
int is_palindrome(listint_t **head)
{
	/* declare variables */
	size_t start, end;
	listint_t *nl_head, *node;

	/* initialize variables */
	start = 0;
	end = 0;
	nl_head = NULL;
	node = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	nl_head = *head;
	end = listint_len(nl_head) - 1;
	while (*head != NULL && start < end)
	{
		/**
		 * get the node at the end of the list
		 * and compare to the node at current loop head
		 * if the value in the nodes are not equal
		 * return 0
		 */
		node = get_nodeint_at_index(nl_head, end);

		if ((*head)->n != node->n)
			return (0);
		start += 1;
		end -= 1;
		*head = (*head)->next;
	}

	return (1);
}
/**
 * listint_len - return the number of elements in a linked list
 * @h: pointer to the linked list
 *
 * Return: the numbers of nodes in a linked list
 */

size_t listint_len(const listint_t *h)
{
	/* declare variable */
	size_t n;

	/* initialize variable */
	n = 0;

	if (!h)
		return (0);

	while (h != NULL)
	{
		n++;
		h = h->next;
	}

	return (n);
}
/**
 * get_nodeint_at_index - returns the nth node of a singly linked list
 * @head: pointer to a singly linked list
 * @index: index of the node to be returned
 *
 * Description: index is the index of the node, starting at 0
 * Return: returns the nth node of a singly linked list
 */
listint_t *get_nodeint_at_index(listint_t *head, size_t index)
{
	/* declare variables */
	size_t count;
	listint_t *nthNode;


	/* initialize variables */
	count = 0;
	nthNode = NULL;

	/* seek the nth node */
	while (head != NULL)
	{
		nthNode = head;
		head = nthNode->next;
		if (count == index)
			return (nthNode);
		count++;
	}

	return (NULL);
}
