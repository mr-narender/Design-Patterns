//String functions

#include <string>
#include <iostream>
#include "StrFuncs.h"
#include <vector>
#include <algorithm>

string Strfuncs::strip(string line) {
	const string WHITESPACE = " \n\r\t\f\v";   //whitespace characters
	size_t first = line.find_first_not_of(WHITESPACE);
	size_t last = line.find_last_not_of(WHITESPACE) + 1;
	return line.substr(first, last);                //strip whitespaces
}

std::vector<string> Strfuncs::split(string line, string delim) {
	vector<string> tokens;            //create vector of tokens
	size_t start = 0;
	while (start >= 0 && start <= line.length()) {
		start = line.find(delim, 0);
		string val = strip(line.substr(0, start));
		tokens.push_back(val);                  //add each token to vector
		line = strip(line.substr(start + 1, line.length()));
	}
	return tokens;

}

// converts string to all lowercase
std::string Strfuncs::to_Lower(std::string str) {
	std::transform(str.begin(), str.end(), str.begin(), std::tolower);
	return str;
}
