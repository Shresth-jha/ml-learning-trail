#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:04:00 2021

@author: paddy
"""

# Skeleton for sparse matrix operations

# add two sparse matrices
def smAdd(sm_a,sm_b):
    """
    Adds two compatible sparse matrices.

    Parameters
    ----------
    sm_a : dictionary
        sm_a represents a sparse matrix (SM)
    sm_b : dictionary
        sm_b represents a SM.

    Returns
    -------
    A new SM, as a dictionary, which is the sum of SMs sm_a and sm_b.

    """
        
    
    # write your code here
    

def smScale(sm_a,k):
    """
    Scales a sparse matrix.

    Parameters
    ----------
    sm_a : dictionary
        sm_a represents a sparse matrix (SM)
    k : number (int or float)
        The scaling factor for sm_a.

    Returns
    -------
    A new SM, as a dictionary, which is sm_a scaled by k.

    """
    
    # write your code here
    
    

def smTrace(sm_a):
    """
    Computes trace of a square sparse matrix.

    Parameters
    ----------
    sm_a : dictionary
        sm_a represents a sparse matrix (SM)

    Returns
    -------
    A number (int or float) representing the trace of the SM sm_a.

    """
    
    # Write your code here
    
  
    
def smPrint(sm_a):
    """
    Displays a sparse matrix, formatted properly.

    Parameters
    ----------
    sm_a : dictionary
        sm_a represents a sparse matrix (SM)

    Returns
    -------
    None.

    """
    



## main program begins here

# Input the SM sm_a and sm_b
# You can either hard-code it here, or,
# read from a file, or,
# ask the user to input the values (tedious!)

# Remember to ask for the dimensions of the matrices first.

# Form the dictionaries representing sm_a, sm_b


# Perform addition
# First check if dimensions are compatible for addition
# If yes, then proceed.
 sm_c = smAdd(sm_a, sm_b)
# Display the result
 smPrint(sm_c)

# perform scaling
# get the input k
 sm_d = smScale(sm_a, k)
# Display the result
 smPrint(sm_d)


# compute trace
# check if matrix is square
# if yes, then find trace
 tr = smTrace(sm_a)
# print the result













    
    
    
    
    
