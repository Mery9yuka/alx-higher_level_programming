#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - function that insert a node in a linked list
 * @head: point to the head the list
 * @number: num to be inserted
 * Return: the address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new = NULL;
    listint_t *numb = *head;

    new = malloc(sizeof(listint_t));

    if (new == NULL)
        return (NULL);
    new->n = number;
    new->next = NULL;

    if (numb == NULL || numb->n >= number)
    {
        new->next = numb;
        numb = new;
        return (new);
    }
    while (numb && numb->next && numb->next->n < number)
        numb = numb->next;

    new->next = numb->next;
    numb->next = new;
    return (new);
}