from numpy import *

a = array([0,0], dtype=float)
b = array([1,1], dtype=float)
orders = array([50,50], dtype=int)


from misc import mlinspace

gg = mlinspace(a,b,orders)

f = lambda x,y: x**2 + y**2
g = lambda x,y: x**3 + y**3


# single valued function to interpolate
vals = f(gg[:,0], gg[:,1])



# multi valued function to interpolate
vals2 = g(gg[:,0], gg[:,1])
mvals = row_stack([vals, vals2])


# one single point
point = array([0.5, 0.5])

# many points
points = row_stack([[0.5, 0.5]]*10)


def test_cubic_spline_object():

    from splines import CubicSpline

    cs = CubicSpline(a,b,orders,vals)
    ii = cs(point)
    iii = cs(points)

    print(ii.shape)
    assert(ii.ndim==0)
    assert(iii.ndim==1)

def test_cubic_multi_spline_object():

    from splines import MultiCubicSpline

    cs = MultiCubicSpline(a,b,orders,mvals)
    ii = cs(point)
    iii = cs(points)

    print(ii.shape)
    assert(ii.ndim==1)
    assert(iii.ndim==2)


if __name__ == '__main__':

    test_cubic_spline_object()
    test_cubic_multi_spline_object()
