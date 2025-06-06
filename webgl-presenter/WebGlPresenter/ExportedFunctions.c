#include "pch.h"
#include "ExportedFunctions.h"


#include <stdio.h> // For printf, if you use it

WEBGLPRESENTER_API int AddNumbers(int a, int b) {
  return a + b;
}

WEBGLPRESENTER_API void ShowScene(const char* message) {
  printf("DLL Message: %s\n", message);
}