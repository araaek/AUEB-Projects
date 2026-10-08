#pragma once
#include <chrono>
#include <string>

class Timer
{
private:
	std::chrono::time_point<std::chrono::high_resolution_clock> m_sample;
	float m_sec = 0.0f;

public:
	void query()
	{
		auto t = std::chrono::high_resolution_clock::now();
		m_sec = (float)std::chrono::duration_cast<std::chrono::milliseconds>(t - m_sample).count();
		m_sample = t;
	}
	operator std::string() { return std::to_string(m_sec) + "ms"; }
	float to_seconds() { return m_sec / 1000.0f; }
	float to_miliseconds() { return m_sec; }
};
