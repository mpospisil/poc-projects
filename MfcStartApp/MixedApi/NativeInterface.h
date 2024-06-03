// This is the header file for your mixed-mode DLL
#ifdef MIXED_DLL_EXPORTS
#define MIXED_DLL_API __declspec(dllexport)
#else
#define MIXED_DLL_API __declspec(dllimport)
#endif

#include "Api.h"

extern "C" {
  MIXED_DLL_API int NativeAdd(Api* pApi);
}