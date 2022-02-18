#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - Function that creates an infinite loop.
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * create_zombie - Function that creates a zombie process.
 * Return: Nothing
 */
void create_zombie(void)
{
	pid_t zombie = fork();

	if (zombie == 0)
		exit(0);
	else
		printf("Zombie process created, PID: %d\n", zombie);
}
/**
 * main - Main function
 * Return: Always 0
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
		create_zombie();
	infinite_while();
	return (0);
}
