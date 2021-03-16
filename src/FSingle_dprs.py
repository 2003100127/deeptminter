__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2020"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import sys
import numpy as np
sys.path.append('../')
from src.SSingle_dprs import single_dprs as psss


class single_dprs(object):

    def __init__(self, msa):
        self.msa = msa
        self.aa_alphabet = psss().get(gap=True)
        self.msa_row = len(self.msa)
        self.msa_col = len(self.msa[0])

    def columns(self):
        A = [0] * self.msa_col
        C = [0] * self.msa_col
        D = [0] * self.msa_col
        E = [0] * self.msa_col
        F = [0] * self.msa_col
        G = [0] * self.msa_col
        H = [0] * self.msa_col
        I = [0] * self.msa_col
        K = [0] * self.msa_col
        L = [0] * self.msa_col
        M = [0] * self.msa_col
        N = [0] * self.msa_col
        P = [0] * self.msa_col
        Q = [0] * self.msa_col
        R = [0] * self.msa_col
        S = [0] * self.msa_col
        T = [0] * self.msa_col
        V = [0] * self.msa_col
        W = [0] * self.msa_col
        Y = [0] * self.msa_col
        omit = [0] * self.msa_col
        for homolog in self.msa:
            for index, base in enumerate(homolog):
                if base == 'A':
                    A[index] += 1
                elif base == 'C':
                    C[index] += 1
                elif base == 'D':
                    D[index] += 1
                elif base == 'E':
                    E[index] += 1
                elif base == 'F':
                    F[index] += 1
                elif base == 'G':
                    G[index] += 1
                elif base == 'H':
                    H[index] += 1
                elif base == 'I':
                    I[index] += 1
                elif base == 'K':
                    K[index] += 1
                elif base == 'L':
                    L[index] += 1
                elif base == 'M':
                    M[index] += 1
                elif base == 'N':
                    N[index] += 1
                elif base == 'P':
                    P[index] += 1
                elif base == 'Q':
                    Q[index] += 1
                elif base == 'R':
                    R[index] += 1
                elif base == 'S':
                    S[index] += 1
                elif base == 'T':
                    T[index] += 1
                elif base == 'V':
                    V[index] += 1
                elif base == 'W':
                    W[index] += 1
                elif base == 'Y':
                    Y[index] += 1
                elif base == '-':
                    omit[index] += 1
        count_array = np.array([A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y, omit])
        faa = count_array / self.msa_row
        fff = {}
        for i, aa in enumerate(self.aa_alphabet):
            fff[aa] = faa[i]
        return fff

    def alignment(self):
        tn = self.msa_row * self.msa_col
        A = 0
        C = 0
        D = 0
        E = 0
        F = 0
        G = 0
        H = 0
        I = 0
        K = 0
        L = 0
        M = 0
        N = 0
        P = 0
        Q = 0
        R = 0
        S = 0
        T = 0
        V = 0
        W = 0
        Y = 0
        omit = 0
        for i in range(self.msa_row):
            for j in range(self.msa_col):
                if self.msa[i][j] == 'A':
                    A += 1
                elif self.msa[i][j] == 'C':
                    C += 1
                elif self.msa[i][j] == 'D':
                    D += 1
                elif self.msa[i][j] == 'E':
                    E += 1
                elif self.msa[i][j] == 'F':
                    F += 1
                elif self.msa[i][j] == 'G':
                    G += 1
                elif self.msa[i][j] == 'H':
                    H += 1
                elif self.msa[i][j] == 'I':
                    I += 1
                elif self.msa[i][j] == 'K':
                    K += 1
                elif self.msa[i][j] == 'L':
                    L += 1
                elif self.msa[i][j] == 'M':
                    M += 1
                elif self.msa[i][j] == 'N':
                    N += 1
                elif self.msa[i][j] == 'P':
                    P += 1
                elif self.msa[i][j] == 'Q':
                    Q += 1
                elif self.msa[i][j] == 'R':
                    R += 1
                elif self.msa[i][j] == 'S':
                    S += 1
                elif self.msa[i][j] == 'T':
                    T += 1
                elif self.msa[i][j] == 'V':
                    V += 1
                elif self.msa[i][j] == 'W':
                    W += 1
                elif self.msa[i][j] == 'Y':
                    Y += 1
                elif self.msa[i][j] == '-':
                    omit += 1
        faa = np.array([
            A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y, omit
        ]) / tn
        fff = {}
        for i, aa in enumerate(self.aa_alphabet):
            fff[aa] = faa[i]
        return fff