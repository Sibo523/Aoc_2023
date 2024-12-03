#include <regex>
#include <string>
#include <iostream>
#include <fstream>

void processMulExpressions(const std::string &input)
{
    std::regex pattern("mul\\((\\d{1,3}),(\\d{1,3})\\)");

    auto words_begin = std::sregex_iterator(input.begin(), input.end(), pattern);
    auto words_end = std::sregex_iterator();
    int sum = 0;
    for (std::sregex_iterator i = words_begin; i != words_end; ++i)
    {
        std::smatch match = *i;
        int num1 = std::stoi(match[1].str());
        int num2 = std::stoi(match[2].str());
        int result = num1 * num2;
        sum += result;
    }
    std::cout << sum << std::endl;
}

int main()
{
    // Open the file
    std::ifstream file("input.txt");

    // Read entire file content into a string
    std::string content((std::istreambuf_iterator<char>(file)),
                        std::istreambuf_iterator<char>());
    file.close();

    // Process the content
    processMulExpressions(content);

    return 0;
}