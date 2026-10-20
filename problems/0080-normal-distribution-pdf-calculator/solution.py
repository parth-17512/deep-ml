import math

def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	denominator = std_dev*math.sqrt(2*math.pi)
	e_power_value = ((x-mean)**2)/(2*std_dev**2)
	e_value = math.exp(-e_power_value)
	pdf = e_value/denominator
	return round(pdf, 5)