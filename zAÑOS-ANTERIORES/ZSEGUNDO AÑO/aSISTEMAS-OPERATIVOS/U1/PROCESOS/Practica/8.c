#include <stdio.h> 
#include <unistd.h> 
#include <sys/wait.h>
int main() {
	int pid;
	int contador = 1;
	pid = fork();
	if (pid == 0) { contador++;
		printf("Hijo 1 - contador: %d\n", contador);
		fork();
		printf("Proceso generado por el hijo - PID: %d\n", getpid());
	} else {
		contador = contador + 5; printf("Padre - contador: %d\n", contador);
		wait(NULL);
		printf("Padre finaliza\n");
	}

	return 0;
}

