#include "pch.h"
#include "ExportedFunctions.h"
#include "webui.h"
#include "vfs.h"

#include <stdio.h> // For printf, if you use it

void exit_app(webui_event_t* e) {
  webui_exit();
}

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

  // Bind React HTML element IDs with a C functions
  webui_bind(react_window, "Exit", exit_app);

  

  // VSF (Virtual File System) Example
  //
  // 1. Run Python script to generate header file of a folder
  //    python vfs.py "/path/to/folder" "vfs.h"
  //
  // 2. Include header file in your C project
  //    #include "vfs.h"
  //
  // 3. use vfs in your custom files handler `webui_set_file_handler()`
  //    webui_set_file_handler(react_window, vfs);

  // Set a custom files handler
  webui_set_file_handler(react_window, vfs);
  webui_show(react_window, "index.html");

  //webui_set_default_root_folder("C:\\deve\\poc-projects-2\\webgl-presenter\\WebGlPresenter\\webui-react-example\\build");
  //webui_show(react_window, "index.html");

  //webui_show(react_window, "http://localhost:3000");

  // Wait until all windows get closed
  webui_wait();

  // Free all memory resources (Optional)
  webui_clean();
}