import numpy as np
import scipy.stats


def acvar(sample, n_lags):

	"""
	Estimate the first n-lags auto-covariance of a sample
	:param sample: list, a sample of transaction price returns
	:param n_lags: int, number of lags
	:return: list, sample auto-covariance
	"""

	# empty output
	acv = []

	# 0-lag auto-covariance
	acv.append(np.cov(sample, sample)[0, 1])

	# i-lag autocovariance
	for i in range(1, n_lags+1):
		acv.append(np.cov(sample[i:], sample[:-i])[0, 1])

	return acv


def c_moment_2(sample):
	""" Estimate the sample second centered moment """
	return np.var(sample)


def c_moment_4(sample):
	""" Estimate the sample fourth centered moment """
	return scipy.stats.kurtosis(sample, fisher=False) * c_moment_2(sample)**2

