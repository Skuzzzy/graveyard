#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct linked_list
{
    int size;
    struct node * head;
    struct node * tail;
};

struct node
{
    int data;
    struct node * next;
};

struct node * new_node_noinit()
{
    struct node * inst = (struct node*)calloc(1, sizeof(struct node));
    inst->data = 0;
    inst->next = NULL;
    return inst;
}

struct node * new_node_specified(int data, struct node * next)
{
    struct node * inst = (struct node*)calloc(1, sizeof(struct node));
    inst->data = data;
    inst->next = next;
    return inst;
}

struct linked_list * new_linked_list()
{
    struct linked_list * inst = (struct linked_list*) calloc(1, sizeof(struct node));
    inst->size = 0;
    inst->head = NULL;
    inst->tail = NULL;
    return inst;
}

void append_linked_list(struct linked_list * list, struct node * tail)
{
    if(list->size == 0)
    {
	list->head = tail;
	list->tail = tail;
    }
    else
    {
	list->tail->next = tail;
	list->tail = tail;
    }

    list->size++;
}

void append_linked_list_value(struct linked_list * list, int value)
{
    struct node * inst = new_node_specified(value, NULL);
    append_linked_list(list, inst);
}

void print_linked_list(struct linked_list * list)
{
    struct node * current = list->head;
    for(int index=0; index < list->size; index++)
    {
	printf("%d ", current->data);
	current = current->next;
    }
    printf("\n");
}

void free_node(struct node * node_inst)
{
    free(node_inst);
}

void free_linked_list(struct linked_list * list)
{
    struct node * current = list->head;
    for(int index=0; index < list->size; index++)
    {
	struct node * temp = current;
	current = current->next;
	free(temp);
    }
}

int get_element_from_linked_list(struct linked_list * list, int index)
{
    if(!(index < list->size) || (index < 0))
    {
	return INT_MIN; // Out of bounds
    }
    else
    {
	struct node * current = list->head;
	for(int inx=0; inx < index; inx++)
	{
	    current = current->next;
	}
	return current->data;
    }

}

int main()
{
    struct node * head = new_node_noinit();
    head->data = 5;
    head = new_node_specified(10, head);
    printf("%d\n", head->data);
    printf("%d\n", head->next->data);

    struct linked_list * list = new_linked_list();
    append_linked_list_value(list, 5);
    append_linked_list_value(list, 10);
    append_linked_list_value(list, 20);
    print_linked_list(list);
    printf("%d %d\n", list->head->data, list->tail->data);
    printf("%d", get_element_from_linked_list(list, 5));
    free_linked_list(list);

    return 0;
}
