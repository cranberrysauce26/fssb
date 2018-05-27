#include <sys/syscall.h>
#include <stdio.h>
int main() {
    printf("mkdirat = %d\n", SYS_mkdirat);
}

/*

potentially unsafe:
getdents 78
getcwd 79
chdir 80
fchdir 81


for sure unsafe:

rename 82
mkdir 83
rmdir 84
creat 85


probably safe:


*/