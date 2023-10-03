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
	listint_t *current, *runningPtr;


	if (list == NULL)
		return (0);

	/* initialize variables */
	current = list;
	runningPtr = list->next->next;

	while (current != runningPtr)
	{
		if (runningPtr == NULL)
			return (0);

		current = current->next;
		runningPtr = runningPtr->next->next;
	}

	return (1);
}
