#include <vector>
using namespace std;

bool minimo_vector_v2(vector<int> v, int& minimo)
{
  if(v.empty())
    return false;

  minimo = v[0];
  for (size_t i = 1; i < v.size(); ++i)
    if (v[i] < minimo)
      minimo = v[i];

  return true;
}