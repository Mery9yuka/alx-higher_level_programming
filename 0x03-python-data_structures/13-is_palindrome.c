#include "lists.h"

/**
 * is_palindrome -> checks if a singly linked list is a palindrome
 * @head: Pointer Head
 * Return: Depend Condition
 */

int is_palindrome(listint_t **head)
{
	listint_t *s = *head;
	listint_t *f = *head;
	listint_t *a = NULL;
	listint_t *b;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	while (f != NULL && f->next != NULL)
	{
		f = f->next->next;
		b = s;
		s = s->next;
		b->next = a;
		a = b;
	}
	if (f != NULL)
		s = s->next;
	while (s != NULL)
	{
		if (a->n != s->n)
		{
			is_palindrome = 0;
			break;
		}
		a = a->next;
		s = s->next;
	} 
    b = NULL;
	f = a;
	while (f != NULL)
	{
		a = f->next;
		f->next = b;
		b = f;
		f = b;
	}
	*head = b;
	return (is_palindrome);
}