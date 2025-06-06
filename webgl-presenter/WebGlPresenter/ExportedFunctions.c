#include "pch.h"
#include "ExportedFunctions.h"
#include "webui.h"

#include <stdio.h> // For printf, if you use it

WEBGLPRESENTER_API int AddNumbers(int a, int b) {
	return a + b;
}

WEBGLPRESENTER_API void ShowScene(const char* message) {
  // Create new windows
  size_t react_window = webui_new_window();

  // Set window size
  webui_set_size(react_window, 550, 450);

  // Set window position
  webui_set_position(react_window, 250, 250);

  webui_show(react_window, "https://www.seznam.cz");

  // Wait until all windows get closed
  webui_wait();

  // Free all memory resources (Optional)
  webui_clean();
}