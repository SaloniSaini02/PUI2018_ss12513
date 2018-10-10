## Review

a.	The null and alternative hypotheses were framed correctly along with the formula.

b.	The only two important features were extracted which were user type and year of birth. 
    Age was calculated using year of birth. The dropna function could be used as I noticed in my dataset that there were 
    NaN values in the year of birth column. A bar chart showing the average age of the subscribers vs average age of
    customers would give a good overview of the observations.

c.	The data is split by user type into two groups Subscriber and Customer. 
    The average age between these two groups were compared and because age is discrete and not 
    continuous with a mean which is not that high we can say that this data follows Poisson distribution. The test that can be 
    performed on this data is the Mann-Whitney U test. 
