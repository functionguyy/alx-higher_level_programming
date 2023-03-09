#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: a pointer to the list
*
* Return: 0 if there is no cycle or 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *main = list;
	listint_t *check = list;


	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	main = main->next;

	while (main != NULL)
	{
		if (main == check)
		{
			return (1);
		}

		main = main->next;
		if (main == NULL)
		{
			return (0);
		}

		main = main->next;
		check = check->next;
	}

	return (0);
}
