"""
This module contains a short set of tests to see how
crosswalk performs.
"""
import time
import crosswalk
import crosswalk.hosts.chalk.example as direct


# ------------------------------------------------------------------------------
def perform_timing_tests():
    """
    This runs a series of tests to compare how different timing
    results come out based on how much work a function is doing
    and how many times it is called. 
    """
    # -- Balanced call count and function processing
    # -- time
    run_test(
        run_count=1000,
        mul_count=1000,
    )

    # -- Increase in function processing time
    run_test(
        run_count=1000,
        mul_count=100000,
    )

    # -- Very fast function calls but lots more
    # -- of them
    run_test(
        run_count=100000,
        mul_count=10,
    )


# ------------------------------------------------------------------------------
def run_test(run_count, mul_count):

    print('\nTest : Run Count : %s, Mul Count : %s' % (run_count, mul_count))

    s1 = time.time()
    crosswalk.example.mul(mul_count)
    e1 = time.time()

    s2 = time.time()
    crosswalk.example.mul(mul_count)
    e2 = time.time()

    print('\tTime taken for first rerouted call : %s' % (e1-s1))
    print('\tTime taken for second rerouted call : %s' % (e2-s2))

    s3 = time.time()
    for i in range(run_count+1):
        crosswalk.example.mul(mul_count)
    e3 = time.time()

    s4 = time.time()
    for i in range(run_count+1):
        direct.mul(mul_count)
    e4 = time.time()

    s5 = time.time()
    for i in range(run_count+1):
        crosswalk.example.mul(mul_count, xapi='cheese')
    e5 = time.time()

    s6 = time.time()
    for i in range(run_count+1):
        crosswalk.example.bespoke_mul(mul_count)
    e6 = time.time()

    reroute_time = round(e3 - s3, 4)
    direct_time = round(e4 - s4, 4)
    specific_api_time = round(e5 - s5, 4)
    over_implemented_time = round(e6 - s6, 4)

    print('\tTime taken using direct calls : %s' % (direct_time))
    print('\tTime taken using rerouting: %s' % (reroute_time))
    print('\tTime taken utilising a specified api : %s' % (specific_api_time))
    print('\tTime taken for calling an over implemented function : %s' % (over_implemented_time))


if __name__ == '__main__':
    perform_timing_tests()
