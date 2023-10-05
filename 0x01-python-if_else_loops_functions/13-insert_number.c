#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - function that insert a node in a linked list
 * @head: point to the head the list
 * @number: numb to be inserted
 * Return: address of new node or 0 if fail
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *n1 = *head;
    listint_t *n2;

    n2 = malloc(sizeof(listint_t));
    if (n2 == NULL)
        return (NULL);
    n2->n = number;
    if (n1 == NULL || n1->n >= number)
    {
        n2->next = n1;
        *head = n2;
        return (n2);
    }
    while (n1 && n1->next && n1->next->n < number)
        n1 = n1-> next;

    n1->next = n1->next;
    n1->next = n2;
    return (n2);
}