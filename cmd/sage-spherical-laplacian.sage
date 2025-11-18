var('x y z')
f = function('f')(x,y,z)

dx = lambda g:- z * diff(g, y) + y * diff(g, z)
dy = lambda g:- x * diff(g, z) + z * diff(g, x)
dz = lambda g:- y * diff(g, x) + x * diff(g, y)

S = dx(dx(f)) + dy(dy(f)) + dz(dz(f))
S

L = diff(f, x, x) + diff(f, y, y) + diff(f, z, z)

Lrad = L - S

