#include "lists.h"

/**
 * check_cycle - a function that checks if a linked list has a cycle
 * @list: pointer to head of linked list
 * Return: 1 if cycle exist, 0 if not
 */
int check_cycle(listint_t *list)
{
    listint_t *neko = list;
    listint_t *yuki = list;

    while (neko != NULL && yuki != NULL && yuki->next != NULL)
    {
        neko = neko->next;
        yuki = yuki->next->next;

        if (neko == yuki)
            return (1);
    }

    return (0);
}
