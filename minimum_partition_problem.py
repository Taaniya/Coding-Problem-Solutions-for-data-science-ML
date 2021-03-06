#! /usr/bin/env python

def getPartitions(s, n, s1, s2, lookup=None):
    """
    Divides a given set of positive integers into 2 subsets such that 
    the absolute difference between the sum is minimum and returns this difference.
    
    Parameters:
    ----------------------
    s : list of positive integers
    n : index of the last integer in the list
    s1 : sum of integers in subset 1
    s2 : sum of integers in subset 2
    lookup : dictionary data structure holding precomputed values of difference for a tuple of (n,s1) as key
    
    Returns:
    ----------------------
    (int) Minimum difference between 2 subsets
    eg. 
    
    >> getPartitions([10,25,15,5,20],4, 0, 0)
    >> 5
    
    where,
    subset 1 : [15, 25]
    subset 2 : [10,5, 20]
    
    Reference:
    https://www.techiedelight.com/minimum-sum-partition-problem/
    """ 
    
    if lookup is None:
        lookup = dict()
    key = (n,s1)
      
    # Compute difference when all the elements are divided between 2 subsets    
    if n < 0 :
        diff = abs(s1 - s2)
        return diff

    if  key not in lookup:
        # For every element in the given collection it can either be included in 
        # subset 1 or excluded. Recur in both the possibilities
        inc = getPartitions(s, n-1, s1 + s[n], s2, lookup)
        exc = getPartitions(s, n-1, s1, s2 + s[n], lookup)
        lookup[key] = min(inc, exc)
    
    return lookup[key]
