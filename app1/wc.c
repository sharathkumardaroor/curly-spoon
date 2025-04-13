#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void wc(FILE *file, const char *filename) {
    int lines = 0, words = 0, chars = 0;
    int in_word = 0;
    int c;

    while ((c = fgetc(file)) != EOF) {
        chars++;
        if (c == '\n') {
            lines++;
        }
        if (isspace(c)) {
            if (in_word) {
                words++;
                in_word = 0;
            }
        } else {
            in_word = 1;
        }
    }
    if (in_word) {
        words++;
    }

    printf("%8d%8d%8d %s\n", lines, words, chars, filename);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        // No filename provided, read from stdin
        wc(stdin, "stdin");
        return 0;
    }

    for (int i = 1; i < argc; i++) {
        FILE *file = fopen(argv[i], "r");
        if (file == NULL) {
            perror(argv[i]);
            continue;
        }
        wc(file, argv[i]);
        fclose(file);
    }

    return 0;
}