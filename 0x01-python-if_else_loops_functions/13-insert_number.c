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
    listint_t *old = NULL;
    listint_t *numb = *head;

    new = malloc(sizeof(listint_t));

    if (new == NULL)
        return (NULL);
    new->n = number;
    new->next = NULL;

    if (numb == NULL || numb->n >= number)
    {
        new->next = numb;
        *head = new;
        return (*head);
    }
    while (numb && numb->n < number)
    {
        old = numb;
        numb = numb->next;
    }
    new->next = numb;
    old->next = new;
    return (*head);
}