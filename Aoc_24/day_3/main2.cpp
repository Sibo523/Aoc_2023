#include <regex>
#include <string>
#include <iostream>
#include <fstream>

void processMulExpressions(const std::string &input)
{
    bool should_process = true;

    // Create regex patterns
    std::regex mul_pattern("mul\\((\\d{1,3}),(\\d{1,3})\\)");
    std::regex do_pattern("do\\(\\)");
    std::regex dont_pattern("don't\\(\\)");

    // Get iterators for the input string
    auto begin = input.cbegin();
    auto end = input.cend();
    auto searchStart = begin;
    int sum = 0;
    std::smatch match;
    while (std::regex_search(searchStart, end, match, std::regex("(do\\(\\))|(don't\\(\\))|(mul\\((\\d{1,3}),(\\d{1,3})\\))")))
    {
        std::string found = match[0];

        if (found == "do()")
        {
            should_process = true;
        }
        else if (found == "don't()")
        {
            should_process = false;
        }
        else if (should_process && found.substr(0, 3) == "mul")
        {
            // Process mul expression
            std::smatch mul_match;
            std::regex_match(found, mul_match, mul_pattern);
            int num1 = std::stoi(mul_match[1]);
            int num2 = std::stoi(mul_match[2]);
            sum += (num1 * num2);
        }

        searchStart = match[0].second;
    }
    std::cout << sum << std::endl;
}

int main()
{
    std::ifstream file("input.txt");

    std::string content((std::istreambuf_iterator<char>(file)),
                        std::istreambuf_iterator<char>());
    file.close();

    processMulExpressions(content);
    return 0;
}