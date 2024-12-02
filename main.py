from sample_project_cpp import how_many_dofs
from dolfinx import fem, mesh
from mpi4py import MPI
import multiphenicsx.fem

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def main():
    square  = mesh.create_unit_square(MPI.COMM_WORLD, 4, 4)
    cdim = square.topology.dim
    fdim = cdim - 1
    square.topology.create_connectivity(cdim,cdim)
    V = fem.functionspace(square, ("Lagrange", 1),)
    DG0 = fem.functionspace(square, ("Discontinuous Lagrange", 0),)
    active_els  = fem.locate_dofs_geometrical(DG0, lambda x : x[0] <= 0.5 )
    active_dofs = fem.locate_dofs_topological(V, cdim, active_els,remote=True)
    restriction = multiphenicsx.fem.DofMapRestriction(V.dofmap, active_dofs)
    dofs_restriction = how_many_dofs(restriction)

if __name__=="__main__":
    main()
