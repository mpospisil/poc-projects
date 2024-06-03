#include "pch.h"
#include "MixedApi.h"
#include "Api.h"

extern "C" __declspec(dllexport) int NativeAdd(Api * pApi)
{
  //return a + b;
  //return MixedApi::Add(a, b);
  return pApi->Run(10);
}

int MixedApi::Add(int a, int b)
{
  return a + b +  100;
}
