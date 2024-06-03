#include "pch.h"
#include "MixedApi.h"

extern "C" __declspec(dllexport) int NativeAdd(int a, int b)
{
  //return a + b;
  return MixedApi::Add(a, b);
}

int MixedApi::Add(int a, int b)
{
  return a + b +  100;
}
