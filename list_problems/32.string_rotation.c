#include <stdio.h>
#include <string.h>

int main() {

    // Ques -> Check if one string is rotation of another .
    
    char s1[100], s2[100], temp[200];

    printf("Enter first string: ");
    scanf("%s", s1);

    printf("Enter second string: ");
    scanf("%s", s2);

    if (strlen(s1) != strlen(s2)) {
        printf("Not Rotation");
        return 0;
    }

    // s1 + s1
    strcpy(temp, s1);
    strcat(temp, s1);


    // check substring
    if (strstr(temp, s2) != NULL) {
        printf("Rotation");
    } else {
        printf("Not Rotation");
    }

    return 0;
}