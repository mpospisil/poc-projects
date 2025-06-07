#ifndef MY_FUNCTIONS_H
#define MY_FUNCTIONS_H

// Use a preprocessor macro to handle __declspec(dllexport) for the DLL project
// and __declspec(dllimport) for consumer projects.
#ifdef WEBGLPRESENTER_EXPORTS
#define WEBGLPRESENTER_API __declspec(dllexport)
#else
#define WEBGLPRESENTER_API __declspec(dllimport)
#endif

// Declare your C functions with extern "C" linkage
#ifdef __cplusplus
extern "C" {
#endif

	WEBGLPRESENTER_API int AddNumbers(int a, int b);
	WEBGLPRESENTER_API void OpenWindow();
	WEBGLPRESENTER_API void ShowScene(const char* message);

#ifdef __cplusplus
}
#endif

#endif // MY_FUNCTIONS_H