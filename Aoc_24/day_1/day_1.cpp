#include <vector>
#include <fstream>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>

int main()
{
    std::ifstream f("input_1.txt");
    std::vector<int> left;
    std::map<int, int> right;
    std::string s;
    // read the input and split each line into a pair of integers
    while (std::getline(f, s))
    {
        char *c = strtok(&s[0], " ");
        char *c1 = strtok(NULL, " ");
        left.push_back(atoi(c));
        right[atoi(c1)] += 1;
    }
    int sum = 0;
    int i = 0;
    for (; i < left.size(); i++)
    {
        if (right.find(left[i]) != right.end())
        {
            sum += left[i] * right[left[i]];
        }
    }
    std::cout << sum << std::endl;
}