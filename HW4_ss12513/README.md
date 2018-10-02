# HOMEWORK 4

## Assignment 1 + Extra Credit : Done by Karan (ks5063)
- A dictionary has been created for 5 distributions.
- An array is created than holds 100 sample sizes from 10 to 2000.
- A nested dictionary is created where the outside dictionary holds the distribution type and the the inner dictionary contains 100 sample distributions of that type.The distribution types are Chi- Squared,Normal, Poisson, Binomial and Lognormal distributions. 
- A scatterplot and histogram are rendered for each distribution type.
- A histogram is rendered for all distributions combined.
- A gaussian is fit to the distribution of means. 

## Assignment 2 : Done by Saloni (ss12513)
- An idea is formulated by observing categorical fields in the data. The idea chosen is that young people are more likely to be subscribers of Citibike.
- NULL HYPOTHESIS : The average age of the subscribers is the same or higher than the average age of the customers. This is the hypotheis to be tested which is measureable.
- ALTERNATIVE HYPOTHESIS: The average age of subscibers is significantly lesser than the average age of the customers.
- A significance level of 0.05 is chosen.
- Environment variable is PUIDATA is set. The dataset is downloaded, unzipped and moved to PUIDATA.
- The dataset is read using python to a dataframe.
- Top few rows of the dataframe is displayed.
- Top few rows of the reducted dataframe is displayed. The fields of interest are usertype and birth year. Age is calculated from the birth year.
- Distribution of the remaining data is plot using bar graph and histogram. 

## Assignment 3 : Saloni has done hypothesis creation and Z-test. Karan has done interpretation of result.
- IDEA: The new bus routes of bus line X8 improves circulation.
- To test this the NULL HYPOTHESIS and ALTERNATIVE HYPOTHESIS are set.
- NULL HYPOTHESIS: The average duration of trips of the new bus routes of bus line X8 is the same or higher than that of the original bus routes, significance level = 0.05.
- ALTERNATIVE HYPOTHESIS: The average duration of the new bus routes of bus line X8 is significantly lower.
- Environment variable is PUIDATA is set. The dataset is downloaded and moved to PUIDATA.
- The times.txt file is read and the journey durations of the sample are stored.
- The population mean and population standard devation are set to 36 and 6 respectively as given by the problem statement. The sample mean is calcluated. 
- Z-statistic is calculated as 2.55639718617. The z-statistic is compared with the significance level and the Null Hypothesis is rejected.  
