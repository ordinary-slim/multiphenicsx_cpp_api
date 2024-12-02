#include <nanobind/nanobind.h>
#include <multiphenicsx/DofMapRestriction.h>

void how_many_dofs(multiphenicsx::fem::DofMapRestriction& res) {
  printf("Number of dofs of restriction = %i\n", res.index_map->size_local());
  printf("Number of dofs of original dofmap = %i\n", res.dofmap()->index_map->size_local());
}

NB_MODULE(sample_project_cpp, m) {
  m.def("how_many_dofs", &how_many_dofs);
}
