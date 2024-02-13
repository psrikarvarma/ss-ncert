#include <stdio.h>

// Function to calculate the expressions recursively and save values to file
void save_values(int n, int limit, FILE *file, int expression) {
    if (n > limit)
        return;

    double value;

    // Calculate the expression based on the given number
    switch (expression) {
        case 3:
            value = (n + 2) / 2.0;
            break;
        case 4:
            value = n * (n + 3) / 4.0;
            break;
        case 5:
            value = (10 - n) / 2.0;
            break;
        case 6:
            value = n * (21 - n) / 4.0;
            break;
        default:
            return;
    }

    // Save the calculated value to the file
    fprintf(file, "%.2f\n", value);

    // Recursive call for the next value
    save_values(n + 1, limit, file, expression);
}

int main() {
    int a;

    // Input for a
    printf("Enter the value of a: ");
    scanf("%d", &a);

    // Open files for writing
    FILE *file3 = fopen("py_3.txt", "w");
    FILE *file4 = fopen("py_4.txt", "w");
    FILE *file5 = fopen("py_5.txt", "w");
    FILE *file6 = fopen("py_6.txt", "w");

    if (file3 == NULL || file4 == NULL || file5 == NULL || file6 == NULL) {
        printf("Error opening files.\n");
        return 1;
    }

    // Save values recursively for each expression
    save_values(0, a, file3, 3);
    save_values(0, a, file4, 4);
    save_values(0, a, file5, 5);
    save_values(0, a, file6, 6);

    // Close files
    fclose(file3);
    fclose(file4);
    fclose(file5);
    fclose(file6);

    printf("Values saved successfully.\n");

    return 0;
}
