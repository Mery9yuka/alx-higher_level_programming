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
    listint_t *numb = *head;
    listint_t *new = 0;

    numb = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;
    if (numb == NULL || numb->n >= number)
    {
        new->next = numb;
        *head = new;
        return (new);
    }
    while (numb && numb->next && numb->next->n < number)
        numb = numb-> next;
    new->next = numb->next;
    numb->next = new;
    return (new);
}