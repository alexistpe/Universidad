#include <stdio.h> 
#include <unistd.h> 
#include <sys/wait.h>

int main() {
	int pid;
	pid = fork(); 
	if (pid == 0) {
		printf("Hijo iniciado\n"); printf("PID hijo: %d\n", getpid());
		execl("/bin/date", "date", NULL);

		printf("Error al ejecutar date\n");
	} else {
		printf("Padre iniciado\n"); 
		printf("PID padre: %d\n", getpid());
		printf("Esperando al hijo...\n");

		wait(NULL);

		printf("El hijo terminó. Padre finaliza.\n");
	}
return 0;
}

