#include "pch.h"
#include "ConLibFunctions.h"
#include <iostream>

extern "C" CONLIBUI_DLL_API const wchar_t* GetPropose(const wchar_t* pSearchArg)
{
  std::wstring* result = new std::wstring(L"Proposed String");
  return result->c_str();
}

extern "C" CONLIBUI_DLL_API void FreePropose(const wchar_t* pString)
{
  delete[] pString;
}