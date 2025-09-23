#include <stdio.h>
#include <string.h>
#define MAXN 25
#define MAXLEN 100
#define INF 1000000

typedef struct {
    char potion[MAXLEN];
    int ingCount;
    char ingredients[10][MAXLEN];
} Recipe;

Recipe recipes[50];
int recipeCount = 0;
char potions[50][MAXLEN];
int potionCount = 0;
int memo[50];
int visited[50];

// Find potion index, add if not exists
int getPotionIndex(char *name) {
    for (int i = 0; i < potionCount; i++) {
        if (strcmp(potions[i], name) == 0) return i;
    }
    strcpy(potions[potionCount], name);
    return potionCount++;
}

// Recursive function to compute minimum orbs
int minOrbs(char *potion) {
    int idx = getPotionIndex(potion);
    if (visited[idx]) return memo[idx];
    visited[idx] = 1;
    int found = 0;
    int best = INF;
    for (int i = 0; i < recipeCount; i++) {
        if (strcmp(recipes[i].potion, potion) == 0) {
            found = 1;
            int cost = recipes[i].ingCount - 1;
            for (int j = 0; j < recipes[i].ingCount; j++) {
                cost += minOrbs(recipes[i].ingredients[j]);
            }
            if (cost < best) best = cost;
        }
    }
    if (!found) best = 0; // base item
    memo[idx] = best;
    return best;
}

int main() {
    int n;
    scanf("%d", &n);
    getchar();
    for (int i = 0; i < n; i++) {
        char line[200];
        fgets(line, sizeof(line), stdin);
        line[strcspn(line, "\n")] = 0;
        char *left = strtok(line, "=");
        char *right = strtok(NULL, "=");
        strcpy(recipes[recipeCount].potion, left);
        recipes[recipeCount].ingCount = 0;
        char *tok = strtok(right, "+");
        while (tok) {
            strcpy(recipes[recipeCount].ingredients[recipes[recipeCount].ingCount++], tok);
            tok = strtok(NULL, "+");
        }
        recipeCount++;
    }
    char target[MAXLEN];
    scanf("%s", target);

    int ans = minOrbs(target);
    printf("%d", ans);  // Print just the integer answer

    return 0;
}