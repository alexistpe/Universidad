#include <stdio.h> 
#include <unistd.h> 
#include <sys/wait.h>

int main() {
	int pid1, pid2; pid1 = fork();
	if (pid1 == 0) { 
		printf("Hijo 1 ejecuta uptime\n");
		execl("/usr/bin/uptime", "uptime", NULL);
		return 1;
	}
	pid2 = fork();
	if (pid2 == 0) {
		printf("Hijo 2 ejecuta df - h\n");
		execl("/bin/df", "df", "-h", NULL);
		return 1;
	}
	printf("Padre creó dos hijos\n"); 
	printf("PID hijo 1: %d\n", pid1); 
	printf("PID hijo 2: %d\n", pid2);
	wait(NULL); 
	wait(NULL);
	printf("Ambos hijos terminaron\n");
	return 0;
}

