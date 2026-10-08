#include <fstream>
#include <string>
#include <random>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include "timer.h"

//#define STAGE1
//#define STAGE2
//#define STAGE3
//#define STAGE4
//#define STAGE5

#include "student.h"
#include "init.h"

#ifdef STAGE1
#include "db.h"  //  <----------------------- TODO: create db.h
#endif 

#ifdef STAGE1
void Stage1()
{
	std::cout << "\n--------------------------------------------------------\n\n";
	std::cout << "STAGE1: Read the first record from the raw database file.\n";
	

	// open the raw database file
	std::ifstream ifs("students.raw", std::ofstream::in | std::ofstream::binary);
	if (!ifs)
	{
		std::cout << "[FAIL] Could not open students.raw raw database file. Exiting.\n";
		return;
	}

	StudentData query;

	// Read a single (the first) record from the raw database file
	bool ok = readStudentRecord(ifs, query); // <----------------------- TODO 
	// Implement a function that takes a reference to an open input stream and reads 
	// a single StudentData record into the second argument.
	// Returns true if the file access and read operation was successful, false otherwise.
	
	if (!ok)
	{
		std::cout << "[FAIL] Failed to read first record from raw database file. Exiting.\n";
		ifs.close();
		return;
	}

	// check validity of results
	if (isString(query.m_name) && isString(query.m_surname) && isValidID(query.m_id))
		std::cout << "[PASS] First record in raw database is (" << query.m_id << ", " << query.m_name << ", " << query.m_surname << ")\n";
	else
		std::cout << "[FAIL] Problem detected in read data: (" << query.m_id << ", " << query.m_name << ", " << query.m_surname << ")\n";

	ifs.close();
}
#endif

#ifdef STAGE2
void Stage2()
{
	std::cout << "\n--------------------------------------------------------\n\n"; 
	std::cout << "STAGE2: Find a single record in the raw database file.\n";
	

	// open the raw database file
	std::ifstream ifs("students.raw", std::ofstream::in | std::ofstream::binary);
	if (!ifs)
	{
		std::cerr << "[FAIL] Could not open students.raw raw database file. Exiting.\n";
		return;
	}

	StudentData query;
	
	// locate a specific record in the raw database file by linear search
	bool found = findStudentByID(ifs, 5000001, query); // <----------------------- TODO
	// implement a function that takes a reference to an open input stream and  
	// searches for a StudentData record whose m_id member matches the integer provided in the second argument.
	// The located StudentData record is stored in the third argument.
	// Returns true if a record with the given ID is found, false otherwise.
	// Notes: Since multiple queries may be performed,
	// a) Before scanning the file for a matching record, make sure to reset the file pointer by calling 
	//    the ifstream::seekg method with value 0.
	// b) After scanning the file for a matching record, make sure to reset all file status flags 
	//    by calling the ifstream::clear method.
	
	if (found)
	{
		std::cout << "[PASS] Found student with id " << query.m_id << ": " << query.m_name << " " << query.m_surname << "\n";
	}
	else
	{
		std::cout << "[FAIL] Could not find student with id 5000001\n";
	}

	ifs.close();
}
#endif

#ifdef STAGE3
void Stage3()
{
	std::cout << "\n--------------------------------------------------------\n\n";
	std::cout << "STAGE3: Object-oriented, non-indexed database access / Multiple queries (slow).\n";

	StudentDataBase db; // <----------------------- TODO
	// Move the functionality of Stage 2 into a StudentDataBase class.

	bool ok = db.open("students.raw"); // <----------------------- TODO
	// Method open prepares the raw database file for reading.
	// Returns true if the file was successfully opened, false otherwise.
	
	if (!ok)
	{
		std::cout << "[FAIL] Could not open raw database file.\n";
		return;
	}

	StudentData student;
	Timer timer;
	
	// Perform 1000 queries in the DB.
	for (int i = 0; i < 1000; i++)
	{
		bool found = db.findByID(5000001+i, student); // <----------------------- TODO
		// the method searches the raw DB for a StudentData record whose m_id matches the first argument.
		// Upon successful match, stores the resulting StudentData into the second argument.
		// Returns true if the record with the requested id is found, false otherwise. 
		// Note: reuse your code 

		if (!found)
		{
			std::cout << "[FAIL] Could not locate record with id " << (5000001 + i) << "in raw database file.\n";
			db.close();
			return;
		}
	}
	timer.query();

	// check validity of a single result
	if (isString(student.m_name) && isString(student.m_surname) && isValidID(student.m_id))
		std::cout << "[PASS] Throughput: " << 1000.0f / timer.to_seconds() << " queries/sec.\n";
	else
		std::cout << "[FAIL] Problem detected in read data: (" << student.m_id << ", " << student.m_name << ", " << student.m_surname << ")\n";

	// close the database
	db.close(); // <----------------------- TODO
	// Method close releases the open file input stream  

}
#endif

#ifdef STAGE4
void Stage4()
{
	std::cout << "\n--------------------------------------------------------\n\n";
	std::cout << "STAGE4: Indexed database access / Multiple queries (fast).\n";
	
	// Build a class to hold a database index from memory to disk raw data.
	// Use the index to query the database instead of the raw file.
	// 
	// The query acceleration index should internally map 
	// all keys (StudentData.m_id values here) present in the raw database file
	// to the corresponding raw file positions, so that it may directly
	// access the appropriate record in a random-access manner instead of 
	// linear file search.
	//
	// Note: The DataBaseIndex class DOES NOT CONTAIN the actual StudentData Records.
	// It ONLY provides indexing to the raw database file data.

	DataBaseIndex dbindex("students.raw"); // <----------------------- TODO
	// The only ctor. Opens the raw DB file and builds an internal index 
	// between StudentData IDs (m_id member) and correponding record positions
	// in the file. Then, it retains the raw data file open for subsequent 
	// queries.

	StudentData student;
	
	Timer timer;
	timer.query();
	
	// Perform N quries to the DB via the replacement query method 
	// equivalent to the SQL statement SELECT * FROM students WHERE m_id = ...
	// using the DataBaseIndex::findByID method.
	//
	const int N = 100000;
	// Warning: if for some reason the following loop is too slow (shouldn't be),
	// decrease N.

	for (int i = 0; i < N; i++)
	{
		bool found = dbindex.findByID(5000001 + i % 2000, student); // <----------------------- TODO
		// The find method is equivalent in functionality to the correponding method 
		// of the StudentDataBase class.

		if (!found)
		{
			std::cout << "[FAIL] Could not locate record with id " << (5000001 + i) << "in indexed database.\n";
			return;
		}
	}
	timer.query();
	
	// check validity of a single result
	std::cout.precision(0);
	if (isString(student.m_name) && isString(student.m_surname) && isValidID(student.m_id))
		std::cout << "[PASS] Throughput: " <<  std::fixed << N / timer.to_seconds() << " queries/sec.\n";
	else
		std::cout << "[FAIL] Problem detected in read data: (" << student.m_id << ", " << student.m_name << ", " << student.m_surname << ")\n";
	
}
#endif

#ifdef STAGE5
void Stage5()
{
	std::cout << "\n--------------------------------------------------------\n\n";
	std::cout << "STAGE5: Database template / Generalized representation.\n";

	// Model a generic database table where a user-defined RECORD is indexed 
	// by a primary key of type KEY.
	// The key is located a certain amount of BYTES from the starting address of the arbitrary,
	// user-defined RECORD

	StudentData student;

	// Calculate the offset of the index key variable we are going to use (m_id here):
	const int offset = (char*)&student.m_id - (char*)&student;
	
	// Create an instance of the database template with signature
	// DataBase < typename RECORD, typename KEY > with
	// StudentData as RECORD and int as KEY types.
	DataBase<StudentData, int> db; // <----------------------- TODO
	// Notes:
	// You can either model the behavior of the simple raw DB of STAGE3 (-0.5 points),
	// or the behavior of the indexed scheme of STAGE4 (full marks)

	// Set the required offset of the key record member, so that
	// the DataBase object can locate and use for comparisons the 
	// proper value of type KEY
	db.setKeyOffset(offset); // <----------------------- TODO
	// setKeyOffset method provides the offset from the start of each DB entry of
	// type RECORD, in BYTES. The DataBase implementation should
	// use this offset to locate the key inside the RECORD memory range.

	db.open("students.raw"); // <----------------------- TODO
	// Method open: 
	// - prepares the raw database file for reading.
	// - optionally, constructs an index (similar to STAGE4) for faster data access.
	// Returns true if the file was successfully opened, false otherwise.

	Timer timer;

	bool found = db.findByID(5000002, student);
	if (found)
		std::cout << "[PASS] Found student with id " << student.m_id << ": " << student.m_name << " " << student.m_surname << "\n";
	else
		std::cout << "[FAIL] Could not find student with id 5000002.\n";
	db.close(); // <----------------------- TODO
	// Method close: 
	// - closes all resources (e.g. open file stream)
}
#endif

int main(int argc, char** argv)
{
	if (!buildRawDB("students.raw"))
	{
		printf("Error creating raw students.raw database file. Exiting.\n");
		exit(-1);
	}
	else
	{
		printf("Created raw database file \"students.raw\".\n");
	}

#ifdef STAGE1	
	Stage1();
#endif	

#ifdef STAGE2	
	Stage2();
#endif	
	
#ifdef STAGE3
	Stage3();
#endif

#ifdef STAGE4
	Stage4();
#endif

#ifdef STAGE5
	Stage5();
#endif

	getchar();

	return 0;
}