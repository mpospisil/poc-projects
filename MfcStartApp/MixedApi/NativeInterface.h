// This is the header file for your mixed-mode DLL
#ifdef MIXED_DLL_EXPORTS
#define MIXED_DLL_API __declspec(dllexport)
#else
#define MIXED_DLL_API __declspec(dllimport)
#endif

extern "C" {
  MIXED_DLL_API int NativeAdd(int a, int b);
}