#pragma once

#include "ConLibUiDll.h"

extern "C" {
	CONLIBUI_DLL_API const wchar_t* GetPropose(const wchar_t* pSearchArg);
	CONLIBUI_DLL_API void FreePropose(const wchar_t* pString);
}
