#include <stdio.h> #include <unistd.h>

int main() {
int pid;
pid = fork(); if (pid == 0) {
printf("Soy el hijo\n"); printf("PID del hijo: %d\n",
getpid());
printf("PID de mi padre:
%d\n", getppid());
} else {
printf("Soy el padre\n"); printf("PID del padre: %d\n",
getpid());
printf("PID del hijo creado:
%d\n", pid);
}

return 0;
}
