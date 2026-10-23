#pragma once
#include <algorithm>
#include <vector>
#include <random>
#include "student.h"
#include <cctype>
#include <string.h>

const std::string _names[20] = { "Kevin", "James", "George", "Nick", "Andrew", "Jordan", "Peter", "Alice", "Mina", "Kelly", "Tina", "Robin", "Donald", "Dorothy", "Thomas", "Tara", "Dimitri", "Kostas", "John", "Maria" };
const std::string _surnames1[20] = { "Rhone", "Jack", "Neil", "Kam", "Cave", "Beni", "Nay", "Benji", "Bean", "Daw", "Sawn", "Sonnor", "Kapel", "Dean", "Funk", "Dick", "Sommer", "For", "Pap", "Dim" };
const std::string _surnames2[20] = { "berg", "son", "", "mann", "ing", "ron", "nau", "bar", "ton", "ni", "ka", "ora", "elli", "", "y", "moor", "field", "os", "as", "ah" };

bool isValidID(int id) { return (id / 5000000 == 1);}

bool isString(char* s) { for (int i = 0; i < strlen(s); i++) if (!isalpha(s[i])) return false; return true; }

StudentData createRandomStudent()
{
	static int next_id = 1;
	StudentData s;
	s.m_id = 5000000 + next_id;
	next_id ++;
	std::string str = _names[rand() % 20];
	memcpy(s.m_name, str.c_str(), str.length() + 1);
	str = _surnames1[rand() % 20] + _surnames2[rand() % 20];
	memcpy(s.m_surname, str.c_str(), str.length() + 1);

	return s;
}

bool buildRawDB(const std::string& file)
{
	std::ofstream ofs(file, std::ofstream::out | std::ofstream::binary);
	if (!ofs)
		return false;

	std::vector<StudentData> data;
	for (int i = 0; i < 10000 + rand()/8 ; i++)
	{
		data.push_back(createRandomStudent());
	}

	std::shuffle(data.begin(), data.end(), std::default_random_engine(0));

	for (auto& s : data)
	{
		ofs.write((char*)&s, sizeof(StudentData));
	}
	ofs.close();
	return true;
}