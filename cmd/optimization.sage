# Declare variables and assumptions
var('r p y')
assume(r > 0)
assume(p > 0, p < 1)
assume(y > 0, y < 1)

# Define the function
f(r, p, y) = y*log(p + (1-p)*r) + (1-y)*log((1-p)/r + p)

# First derivative w.r.t. r
df = diff(f, r)

show(df)

# Solve df/dr = 0 for r
sol = solve(df == 0, r)
show(sol)

# plot the function I(y) = f(r, p, y) with r given by sol and p = 0.5
r_star(y) = sol[0]

f_sub(y) = f(r_star(y), 1/2, y)


f_sub_num(y) = numerical_approx(f_sub(y))

plot(f_sub_num(y), 0.01, 0.99, ymin=-5, ymax=5, figsize=6)