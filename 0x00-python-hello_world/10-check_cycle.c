#include "lists.h"
/**
 * check_cycle - checks if a single linked list has a cycle in it
 * @list: a pointer to the list
 *
 * Return: 0 if there is no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	/* declare variables */
	listint_t *head, *current, *runningPtr;

	/* initialize variables */
	head = list;
	current = list;
	runningPtr = list->next;

	while (current != runningPtr)
	{
		if (runningPtr == NULL)
			return (0);
		if (runningPtr == head)
			return (1);

		current = current->next;
		runningPtr = runningPtr->next;
	}

	return (1);
}
