#ifdef  CONLIBUI_DLL_EXPORTS 
/*Enabled as "export" while compiling the dll project*/
#define CONLIBUI_DLL_API __declspec(dllexport)  
#else
/*Enabled as "import" in the Client side for using already created dll file*/
#define CONLIBUI_DLL_API __declspec(dllimport)  
#endif