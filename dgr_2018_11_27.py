Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/user/RTR105/montecarlo.py ==================
>>> 
>>> 
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/montecarlo.py', 'sys': <module 'sys' (built-in)>, 'random': <module 'numpy.random' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/random/__init__.py'>}
>>> print(random.__doc__)

========================
Random Number Generation
========================

==================== =========================================================
Utility functions
==============================================================================
random_sample        Uniformly distributed floats over ``[0, 1)``.
random               Alias for `random_sample`.
bytes                Uniformly distributed random bytes.
random_integers      Uniformly distributed integers in a given range.
permutation          Randomly permute a sequence / generate a random sequence.
shuffle              Randomly permute a sequence in place.
seed                 Seed the random number generator.
choice               Random sample from 1-D array.

==================== =========================================================

==================== =========================================================
Compatibility functions
==============================================================================
rand                 Uniformly distributed values.
randn                Normally distributed values.
ranf                 Uniformly distributed floating point numbers.
randint              Uniformly distributed integers in a given range.
==================== =========================================================

==================== =========================================================
Univariate distributions
==============================================================================
beta                 Beta distribution over ``[0, 1]``.
binomial             Binomial distribution.
chisquare            :math:`\chi^2` distribution.
exponential          Exponential distribution.
f                    F (Fisher-Snedecor) distribution.
gamma                Gamma distribution.
geometric            Geometric distribution.
gumbel               Gumbel distribution.
hypergeometric       Hypergeometric distribution.
laplace              Laplace distribution.
logistic             Logistic distribution.
lognormal            Log-normal distribution.
logseries            Logarithmic series distribution.
negative_binomial    Negative binomial distribution.
noncentral_chisquare Non-central chi-square distribution.
noncentral_f         Non-central F distribution.
normal               Normal / Gaussian distribution.
pareto               Pareto distribution.
poisson              Poisson distribution.
power                Power distribution.
rayleigh             Rayleigh distribution.
triangular           Triangular distribution.
uniform              Uniform distribution.
vonmises             Von Mises circular distribution.
wald                 Wald (inverse Gaussian) distribution.
weibull              Weibull distribution.
zipf                 Zipf's distribution over ranked data.
==================== =========================================================

==================== =========================================================
Multivariate distributions
==============================================================================
dirichlet            Multivariate generalization of Beta distribution.
multinomial          Multivariate generalization of the binomial distribution.
multivariate_normal  Multivariate generalization of the normal distribution.
==================== =========================================================

==================== =========================================================
Standard distributions
==============================================================================
standard_cauchy      Standard Cauchy-Lorentz distribution.
standard_exponential Standard exponential distribution.
standard_gamma       Standard Gamma distribution.
standard_normal      Standard normal distribution.
standard_t           Standard Student's t-distribution.
==================== =========================================================

==================== =========================================================
Internal functions
==============================================================================
get_state            Get tuple representing internal state of generator.
set_state            Set state of generator.
==================== =========================================================


>>> 
>>> print(random.uniform.__doc__)

        uniform(low=0.0, high=1.0, size=None)

        Draw samples from a uniform distribution.

        Samples are uniformly distributed over the half-open interval
        ``[low, high)`` (includes low, but excludes high).  In other words,
        any value within the given interval is equally likely to be drawn
        by `uniform`.

        Parameters
        ----------
        low : float or array_like of floats, optional
            Lower boundary of the output interval.  All values generated will be
            greater than or equal to low.  The default value is 0.
        high : float or array_like of floats
            Upper boundary of the output interval.  All values generated will be
            less than high.  The default value is 1.0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``low`` and ``high`` are both scalars.
            Otherwise, ``np.broadcast(low, high).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized uniform distribution.

        See Also
        --------
        randint : Discrete uniform distribution, yielding integers.
        random_integers : Discrete uniform distribution over the closed
                          interval ``[low, high]``.
        random_sample : Floats uniformly distributed over ``[0, 1)``.
        random : Alias for `random_sample`.
        rand : Convenience function that accepts dimensions as input, e.g.,
               ``rand(2,2)`` would generate a 2-by-2 array of floats,
               uniformly distributed over ``[0, 1)``.

        Notes
        -----
        The probability density function of the uniform distribution is

        .. math:: p(x) = \frac{1}{b - a}

        anywhere within the interval ``[a, b)``, and zero elsewhere.

        When ``high`` == ``low``, values of ``low`` will be returned.
        If ``high`` < ``low``, the results are officially undefined
        and may eventually raise an error, i.e. do not rely on this
        function to behave when passed arguments satisfying that
        inequality condition.

        Examples
        --------
        Draw samples from the distribution:

        >>> s = np.random.uniform(-1,0,1000)

        All values are within the given interval:

        >>> np.all(s >= -1)
        True
        >>> np.all(s < 0)
        True

        Display the histogram of the samples, along with the
        probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 15, normed=True)
        >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
        >>> plt.show()

        
>>> random.uniform(0,1,5)
array([0.59600442, 0.54290565, 0.97262373, 0.3480284 , 0.6388972 ])
>>> random.uniform(0,0.1,10)
array([0.00053329, 0.06871556, 0.02983455, 0.09571119, 0.05973879,
       0.07805458, 0.09303003, 0.09074212, 0.0975975 , 0.04410835])
>>> random.uniform(0,0.1,10)
array([0.01739538, 0.05506526, 0.05969281, 0.08828224, 0.09470332,
       0.04616106, 0.09009455, 0.00390607, 0.05599024, 0.05666415])
>>> 
>>> 
>>> random.uniform(0,0.1,10)
array([0.09807317, 0.01475379, 0.09864913, 0.03014448, 0.0584003 ,
       0.02680926, 0.05863674, 0.06311689, 0.05316221, 0.06686722])
>>> random.uniform(0,0.1,10)
array([0.07201043, 0.0716319 , 0.05446043, 0.04265734, 0.09930656,
       0.01031986, 0.01366074, 0.07545504, 0.09458957, 0.01778   ])
>>> for 1 in range(10):
	int random.uniform(1,100))
	
SyntaxError: invalid syntax
>>> 
>>> for 1 in range(10):
	int (random.uniform(1,100))
	
SyntaxError: can't assign to literal
>>> for i in range(10):
	int (random.uniform(1,100))

29
53
21
67
42
99
33
40
87
52
>>> type(random.uniform(0,0.1))
<class 'float'>
>>> random.uniform(0,1,5)
array([0.78161123, 0.15593525, 0.12807529, 0.98068451, 0.33602394])
>>> random.seed(1)
>>> random.uniform(0,1,5)
array([4.17022005e-01, 7.20324493e-01, 1.14374817e-04, 3.02332573e-01,
       1.46755891e-01])
>>> 
random.uniform(0,1,5)
array([0.09233859, 0.18626021, 0.34556073, 0.39676747, 0.53881673])
>>> random.uniform(0,1,5)
array([0.41919451, 0.6852195 , 0.20445225, 0.87811744, 0.02738759])
>>> 
>>> 
>>> random.uniform(0,1,5)
array([0.67046751, 0.4173048 , 0.55868983, 0.14038694, 0.19810149])
>>> random.uniform(0,1,5)
array([0.80074457, 0.96826158, 0.31342418, 0.69232262, 0.87638915])
>>> random.uniform(0,1,5)
array([0.89460666, 0.08504421, 0.03905478, 0.16983042, 0.8781425 ])
>>> random.uniform(0,1,5)
array([0.09834683, 0.42110763, 0.95788953, 0.53316528, 0.69187711])
>>> 
