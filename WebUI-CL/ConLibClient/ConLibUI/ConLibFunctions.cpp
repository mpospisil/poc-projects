#include "pch.h"
#include "ConLibFunctions.h"
#include <iostream>
#include "webui.hpp"

extern "C" CONLIBUI_DLL_API const wchar_t* GetPropose(const wchar_t* pSearchArg)
{
	webui::window my_window;
	my_window.show("<html><head><script src=\"webui.js\"></script></head> C++ Hello World ! </html>");
	webui::wait();

  std::wstring* result = new std::wstring(L"Proposed String");
  return result->c_str();
}

extern "C" CONLIBUI_DLL_API void FreePropose(const wchar_t* pString)
{
  delete[] pString;
}